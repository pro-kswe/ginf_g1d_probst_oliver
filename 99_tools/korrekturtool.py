import shutil
import os
import difflib
import csv


def ask_for_course_name():
    return input("Kurs (format: ginf{W}_XYZ)? ")


def press_enter_to_continue():
    input("Mit ENTER geht es weiter...")


def preprocess_csv_export(course_name):
    with open(f"kurse/{course_name}.txt", "w") as coursewriter:
        with open("export.csv", mode="r", encoding="utf-8-sig") as exportfile:
            exportreader = csv.DictReader(exportfile, delimiter=";")
            for row in exportreader:
                name = f"{row["Name"]} {row["Vorname"]}"
                name_lower = name.lower()
                name_lower_without_spaces = name_lower.replace(" ", "_")
                coursewriter.write(name_lower_without_spaces)
                coursewriter.write("\n")


def collect_student_names(course_name):
    students_filename = f"kurse/{course_name}.txt"
    student_names = []
    try:
        with open(students_filename) as file:
            while line := file.readline():
                student_names = student_names + [line.rstrip()]
        return student_names
    except Exception as e:
        print(e)
        press_enter_to_continue()
        return []


def collect_structure_specifications(assignment_id):
    structure_filename = f"portfolio/{assignment_id}_structure.txt"
    try:
        with open(structure_filename) as file:
            line = file.readline()
            file_structure = line.rstrip().split(":")
            dir_name = file_structure[0]
            file_names = file_structure[1].split(",")
            return dir_name, sorted(file_names)
    except Exception as e:
        print(e)
        press_enter_to_continue()
        return "", []


def check_github_repo_exists(course_name):
    student_names = collect_student_names(course_name)
    student_count = len(student_names)
    path = f"/Users/pro/PycharmProjects/{course_name}_probst_oliver/98_abgaben"
    error_counter = 0
    for student_name in student_names:
        student_path = f"{path}/{course_name}_{student_name}"
        if not os.path.isdir(student_path):
            print(f"[{student_name}] ERROR: {student_path} gibt es nicht.")
            error_counter += 1
            press_enter_to_continue()
        else:
            content = os.listdir(student_path)
            if len(content) == 0:
                print(f"[{student_name}] ERROR: {student_path} ist leer.")
                error_counter += 1
                press_enter_to_continue()
    if student_count - error_counter != student_count:
        print(f"ERROR: Einige SuS haben Fehler...")
        press_enter_to_continue()


def copy_markdown(course_name):
    assignment_id = input("Abgabe (format XX)? ")
    number_of_exercises_to_check = int(input("Anzahl Übungen für Detail-Check? "))
    exercises_to_check = []
    for number in range(1, number_of_exercises_to_check + 1):
        file_name_of_exercise = input("Python-Dateiname? ")
        exercises_to_check.append((number, file_name_of_exercise))
    src = f"portfolio/{assignment_id}_abgabe_kriterien.md"
    path = f"/Users/pro/PycharmProjects/{course_name}_probst_oliver/98_abgaben"
    dirs = os.listdir(path)
    dirs = list(filter(lambda v: v != ".DS_Store", dirs))
    dirs = list(filter(lambda v: v != "01", dirs))
    dirs = list(filter(lambda v: v != "02", dirs))
    dirs = list(filter(lambda v: v != "03", dirs))
    dirs = list(filter(lambda v: v != "04", dirs))
    dirs = list(filter(lambda v: v != "05", dirs))
    student_dirs = list(filter(lambda v: v.startswith(f"{course_name}"), dirs))
    if len(student_dirs) != len(dirs):
        print("Einige SuS haben einen falschen Datei/Ordnernamen")
        print(f"{len(student_dirs)}:{student_dirs}")
        print(f"{len(dirs)}:{dirs}")
        press_enter_to_continue()
    for student_dir in student_dirs:
        dest = f"{path}/{student_dir}/{assignment_id}_abgabe_bewertung.md"
        try:
            shutil.copy(src, dest)
            inplace_change(dest, "1 Punkt", "1/1 Pkt.")
            inplace_change(dest, "2 Punkte", "2/2 Pkt.")
            inplace_change(dest, "3 Punkte", "3/3 Pkt.")
            inplace_change(dest, "4 Punkte", "4/4 Pkt.")
            inplace_change(dest, "5 Punkte", "5/5 Pkt.")
            inplace_change(dest, "6 Punkte", "6/6 Pkt.")
            inplace_change(dest, "7 Punkte", "7/7 Pkt.")
            inplace_change(dest, "8 Punkte", "8/8 Pkt.")
            for i in range(len(exercises_to_check)):
                number = exercises_to_check[i][0]
                file_name = exercises_to_check[i][1]
                inplace_change(dest, f"[U{number}-XYZ.py]", file_name)
        except Exception as e:
            print(f"[{student_dir}]{e}")
            press_enter_to_continue()


def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def check_structure(course_name):
    assignment_id = input("Abgabe (format IJ)? ")
    student_names = collect_student_names(course_name)
    assignment_dir_name, file_names = collect_structure_specifications(assignment_id)
    if assignment_dir_name != "" and file_names != []:
        path = f"/Users/pro/PycharmProjects/{course_name}_probst_oliver/98_abgaben"

        for student_name in student_names:
            student_path = f"{path}/{course_name}_{student_name}"
            try:
                student_dir_names = sorted(os.listdir(student_path))
                if assignment_dir_name not in student_dir_names:
                    print(
                        f"[{student_name}] ERROR: {assignment_dir_name} Ordner nicht in {student_dir_names} gefunden.")
                    press_enter_to_continue()
            except Exception as e:
                print(f"[{student_name}]{e}")
                press_enter_to_continue()
            student_assignment_path = f"{path}/{course_name}_{student_name}/{assignment_dir_name}"
            try:
                student_file_names = sorted(os.listdir(student_assignment_path))
                student_python_file_names = list(
                    filter(lambda v: v.endswith(".py") or v.endswith(".png"), student_file_names)
                )
                for i in range(0, len(file_names)):
                    spec_file_name = file_names[i]
                    if spec_file_name not in student_python_file_names:
                        print(
                            f"[{student_name}] ERROR: {spec_file_name} Datei nicht in {student_python_file_names} gefunden.")
                        press_enter_to_continue()
            except Exception as e:
                print(f"[{student_name}]{e}")
                press_enter_to_continue()


def clean_structure(course_name):
    assignment_id = input("Abgabe (format IJ)? ")
    student_names = collect_student_names(course_name)
    assignment_dir_name, file_names = collect_structure_specifications(assignment_id)
    if assignment_dir_name != "" and file_names != []:
        path = f"/Users/pro/PycharmProjects/{course_name}_probst_oliver/98_abgaben"
        for student_name in student_names:
            student_assignment_path = f"{path}/{course_name}_{student_name}/{assignment_dir_name}"
            if os.path.isdir(student_assignment_path):
                student_file_names = sorted(os.listdir(student_assignment_path))
                for student_file_name in student_file_names:
                    if student_file_name.startswith("._") and (
                            student_file_name.endswith(".py") or student_file_name.endswith(".png")):
                        student_file_path = f"{student_assignment_path}/{student_file_name}"
                        try:
                            os.remove(student_file_path)
                        except Exception as e:
                            print(f"[{student_name}]{e}")
                            press_enter_to_continue()
            else:
                print(f"{student_assignment_path} gibt es nicht.")


def compare_file(course_name):
    assignment_id = input("Abgabe (format IJ)? ")
    student_names = collect_student_names(course_name)
    assignment_dir_name, file_names = collect_structure_specifications(assignment_id)
    if assignment_dir_name != "" and file_names != []:
        path = f"/Users/pro/PycharmProjects/{course_name}_probst_oliver/98_abgaben"
        assignment_file_name = input("Dateiname? ")

        for student_name in student_names:
            student_assignment_path = f"{path}/{course_name}_{student_name}/{assignment_dir_name}/{assignment_file_name}"
            spec_assignment_path = f"/Users/pro/PycharmProjects/turtle-uebungen/{assignment_dir_name}/{assignment_file_name}"
            try:
                with open(student_assignment_path) as file_student:
                    file_student_text = file_student.readlines()

                with open(spec_assignment_path) as file_spec:
                    file_spec_text = file_spec.readlines()

                res = list(difflib.unified_diff(file_student_text, file_spec_text, fromfile='SuS', tofile='Vorgabe',
                                                lineterm=''))
                if len(res) != 0:
                    print(f"[{student_name}] ERROR: {assignment_file_name} ist nicht identisch mit der Vorgabe.")
                    for line in res:
                        print(line)
                    press_enter_to_continue()
            except Exception as e:
                print(f"[{student_name}]{e}")


print("WILLKOMMEN ZUM KORREKTURTOOL")
course = ask_for_course_name()
aktion = 0
while aktion != 9:
    print("==== AUSWAHL ====")
    print("1: CHECK GITHUB REPO VORHANDEN")
    print("2: KOPIERE MARKDOWN")
    print("3: CHECK STRUKTUR")
    print("4: CLEAN STRUKTUR")
    print("5: VERGLEICHE DATEI")
    print("6: SCHULNETZ EXPORT VERARBEITEN")
    print("9: EXIT")
    try:
        aktion = int(input("Aktion? "))
        if aktion == 1:
            check_github_repo_exists(course)
        elif aktion == 2:
            copy_markdown(course)
        elif aktion == 3:
            check_structure(course)
        elif aktion == 4:
            clean_structure(course)
        elif aktion == 5:
            compare_file(course)
        elif aktion == 6:
            preprocess_csv_export(course)
        elif aktion == 9:
            print("AUF WIEDERSEHEN.")
        else:
            print("Unbekannte Aktion. Erneute Eingabe.")
    except Exception as ex:
        print(ex)
    print()
