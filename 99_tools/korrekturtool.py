import csv
import os


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


def collect_structure_specifications(number):
    structure_filename = f"templates/struktur_{number}.txt"
    directories = {}
    try:
        with open(structure_filename) as file:
            while line := file.readline():
                file_structure = line.rstrip().split(":")
                dir_name = file_structure[0]
                file_names = file_structure[1].split(",")
                directories[dir_name] = sorted(file_names)
            return directories
    except Exception as e:
        print(e)
        press_enter_to_continue()
        return directories


def check_github_repo_exists(course_name):
    student_names = collect_student_names(course_name)
    student_count = len(student_names)
    error_counter = 0
    for student_name in student_names:
        student_path = f"../{course_name}_{student_name}"
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
    else:
        print("Alle GitHub-Repos OKAY")


def copy_markdown(course_name):
    answer = input("Initialer Markdown Inhalt? (Format Y/N oder leerlassen)? ")
    if answer == "Y":
        src_filepath = f"templates/initial.md"
        mode = "w"
    else:
        number = input("Bewertungsnummer (format X)? ")
        src_filepath = f"templates/bewertung_{number}.md"
        mode = "a"
    with open(src_filepath) as src_file:
        markdown = src_file.read()
    print("====== MARKDOWN START ======")
    print(markdown)
    print("====== MARKDOWN ENDE ======")
    press_enter_to_continue()
    student_names = collect_student_names(course_name)
    student_count = len(student_names)
    error_counter = 0
    for student_name in student_names:
        student_readme_filepath = f"../{course_name}_{student_name}/README.md"
        if not os.path.isfile(student_readme_filepath):
            print(f"[{student_name}] ERROR: {student_readme_filepath} gibt es nicht.")
            error_counter += 1
            press_enter_to_continue()
        else:
            with open(student_readme_filepath, mode) as dest_file:
                dest_file.write(markdown)
    if student_count - error_counter != student_count:
        print(f"ERROR: Einige SuS haben Fehler...")
        press_enter_to_continue()
    else:
        print("Alle README-Dateien angepasst.")


def check_structure(course_name):
    number = input("Bewertungsnummer (format X)? ")
    student_names = collect_student_names(course_name)
    directories = collect_structure_specifications(number)
    if len(directories) != 0:
        for student_name in student_names:
            print()
            print()
            print(f"====== CHECKING STRUKTUR von {student_name} ======")
            answer = input("Überspringen? (Format Y/N oder leerlassen)? ")
            if answer != "Y":
                student_path = f"../{course_name}_{student_name}"
                try:
                    student_file_names = sorted(os.listdir(student_path))
                    student_dir_names = list(
                        filter(lambda filename: os.path.isdir(f"{student_path}/{filename}"), student_file_names)
                    )
                    print("ORDNER")
                    error_counter = 0
                    for student_dir_name in student_dir_names:
                        if student_dir_name not in directories:
                            print(f"Der Ordner {student_dir_name} ist nicht korrekt.")
                            error_counter += 1
                            press_enter_to_continue()
                    for directory in directories:
                        if directory not in student_dir_names:
                            print(f"Der Ordner {directory} ist nicht vorhanden.")
                            error_counter += 1
                            press_enter_to_continue()
                    if error_counter == 0:
                        print("Keine Fehler.")
                    print("DATEIEN")
                    error_counter = 0
                    for student_dir_name in student_dir_names:
                        print(f"im Ordner {student_dir_name}...")
                        student_dir_path = f"{student_path}/{student_dir_name}"
                        student_file_names = sorted(os.listdir(student_dir_path))
                        student_python_file_names = list(
                            filter(
                                lambda filename:
                                os.path.isfile(f"{student_dir_path}/{filename}") and filename.endswith(".py"),
                                student_file_names
                            )
                        )
                        if student_dir_name in directories:
                            python_files = directories[student_dir_name]
                        else:
                            print(f"Der Ordner {student_dir_name} gibt es nicht.")
                            dir_name = input("Wie lautet der korrekte Ordnername? ")
                            python_files = directories[dir_name]
                        for student_python_file_name in student_python_file_names:
                            if student_python_file_name not in python_files:
                                print(f"Die Python-Datei {student_python_file_name} ist nicht korrekt.")
                                press_enter_to_continue()
                        for python_file in python_files:
                            if python_file not in student_python_file_names:
                                print(f"Die Python-Datei {python_file} ist nicht vorhanden.")
                                press_enter_to_continue()
                    if error_counter == 0:
                        print("Keine Fehler.")
                except Exception as e:
                    print(f"[{student_name}]{e}")
                    press_enter_to_continue()
                print()
                print()
    else:
        print("Keine Strukturinformationen gefunden.")


print("WILLKOMMEN ZUM KORREKTURTOOL")
course = ask_for_course_name()
aktion = 0
while aktion != 9:
    print("==== AUSWAHL ====")
    print("1: CHECK GITHUB REPO VORHANDEN")
    print("2: KOPIERE MARKDOWN")
    print("3: CHECK STRUKTUR")
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
        elif aktion == 6:
            preprocess_csv_export(course)
        elif aktion == 9:
            print("AUF WIEDERSEHEN.")
        else:
            print("Unbekannte Aktion. Erneute Eingabe.")
    except Exception as ex:
        print(ex)
    print()
