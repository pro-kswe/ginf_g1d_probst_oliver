import csv
import os
import re


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
        student_path = f"../98_repos_sus/{course_name}_{student_name}"
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
        student_readme_filepath = f"../98_repos_sus/{course_name}_{student_name}/README.md"
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
                student_path = f"../98_repos_sus/{course_name}_{student_name}"
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
                    # Load dirs again if user corrected names on-the-fly
                    directories = collect_structure_specifications(number)
                    student_file_names = sorted(os.listdir(student_path))
                    student_dir_names = list(
                        filter(lambda filename: os.path.isdir(f"{student_path}/{filename}"), student_file_names)
                    )
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
                            print(f"Den Ordner {student_dir_name} gibt es nicht.")
                            python_files = {}
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


def check_clean_code_rules(course_name):
    student_names = collect_student_names(course_name)
    for student_name in student_names:
        print()
        print()
        print(f"====== CHECKING CLEAN-CODE-REGELN von {student_name} ======")
        answer = input("Überspringen? (Format Y/N oder leerlassen)? ")
        if answer != "Y":
            student_path = f"../98_repos_sus/{course_name}_{student_name}"
            try:
                student_file_names = sorted(os.listdir(student_path))
                student_dir_names = list(
                    filter(lambda filename: os.path.isdir(f"{student_path}/{filename}"), student_file_names)
                )
                for student_dir_name in student_dir_names:
                    student_dir_path = f"{student_path}/{student_dir_name}"
                    student_file_names = sorted(os.listdir(student_dir_path))
                    student_python_file_names = list(
                        filter(
                            lambda filename:
                            os.path.isfile(f"{student_dir_path}/{filename}") and filename.endswith(".py"),
                            student_file_names
                        )
                    )
                    for student_python_file_name in student_python_file_names:
                        print(f"=== {student_dir_name}: {student_python_file_name} ===")
                        with open(f"{student_path}/{student_dir_name}/{student_python_file_name}", "r",
                                  encoding="utf-8") as f:
                            file_content = f.read()
                            f.seek(0)
                            file_lines = f.read().splitlines()
                            f.seek(0)
                            file_lines_with_new_lines = f.read().splitlines(keepends=True)

                        error_counter = 0
                        print("LEERZEILE NACH IMPORT...")
                        error_counter += check_import_blank_line(file_lines, student_dir_name, student_python_file_name)
                        print("LEERZEILE AM ENDE...")
                        error_counter += check_trailing_blank_line(file_lines_with_new_lines, student_dir_name,
                                                                   student_python_file_name)
                        print("LEERZEICHEN NACH KOMMA BEI ARGUMENTEN...")
                        error_counter += check_space_after_comma_in_arguments(file_lines, student_dir_name,
                                                                              student_python_file_name)
                        print()

                        if error_counter > 0:
                            print(f"Es gibt {error_counter} Fehler.")
                            press_enter_to_continue()
                            is_file_printed = input("Dateiinhalt anzeigen? Y/N oder leerlassen? ")
                            if is_file_printed == "Y":
                                print(file_content)
            except Exception as e:
                print(f"[{student_name}]{e}")
                press_enter_to_continue()
            print()
            print()


def check_space_after_comma_in_arguments(file_lines, directory, file_name):
    error_counter = 0
    if not file_lines:
        print(f"Leere Datei {file_name} kein Leerzeichen möglich.")
        error_counter += 1
    else:
        # Findet Kommas, die NICHT korrekt mit genau einem Leerzeichen gefolgt sind
        no_space_for_multiple_arguments_pattern = re.compile(r",(?=[^\s])|,(?=\s{2,})")
        for i, file_line in enumerate(file_lines, start=1):
            if no_space_for_multiple_arguments_pattern.search(file_line):
                error_counter += 1
                print(f"- {directory}/{file_name} in Zeile {i}: falscher Abstand nach Komma.")
    return error_counter


def check_trailing_blank_line(file_lines_with_new_lines, directory, file_name):
    error_counter = 0

    if not file_lines_with_new_lines:
        print(f"Leere Datei {file_name} keine Leerzeile möglich.")
        error_counter += 1
    else:
        last_line = file_lines_with_new_lines[len(file_lines_with_new_lines) - 1]
        if last_line.rstrip() == "" and len(file_lines_with_new_lines) > 1:
            last_line = file_lines_with_new_lines[len(file_lines_with_new_lines) - 2]
        if last_line == "\n":
            print(f"- {directory}/{file_name} zu viele Leerzeilen am Ende.")
            error_counter += 1
        else:
            if not last_line.endswith("\n"):
                print(f"- {directory}/{file_name} keine Leerzeile am Ende.")
                error_counter += 1
    return error_counter


def check_import_blank_line(file_lines, directory, file_name):
    # Finde die letzte Importzeile
    # \s is whitespace \S negated
    import_pattern = re.compile(r"^\s*(import)\s+\S+")
    last_import_command_index = None
    error_counter = 0

    for i, line in enumerate(file_lines):
        if import_pattern.match(line):
            last_import_command_index = i

    if last_import_command_index is None:
        print(f"Es gibt in {file_name} keine import-Befehle.")
        error_counter += 1
    else:
        # Prüfen, was nach dem letzten Import kommt
        if last_import_command_index + 1 >= len(file_lines):
            print(f"- {directory}/{file_name} endet und hat keine Leerzeile.")
            error_counter += 1

        next_line = file_lines[last_import_command_index + 1]

        if next_line.strip() == "":
            # Prüfen, ob genau EINE Leerzeile folgt
            if last_import_command_index + 2 < len(file_lines) and file_lines[
                last_import_command_index + 2].strip() == "":
                print(f"- MEHR als eine Leerzeile in {directory}/{file_name}.")
                error_counter += 1
        else:
            print(f"- KEINE Leerzeile in {directory}/{file_name} nach import.")
            error_counter += 1
    return error_counter


print("WILLKOMMEN ZUM KORREKTURTOOL")
course = ask_for_course_name()
aktion = 0
while aktion != 9:
    print("==== AUSWAHL ====")
    print("1: CHECK GITHUB REPO VORHANDEN")
    print("2: KOPIERE MARKDOWN")
    print("3: CHECK STRUKTUR")
    print("4: CHECK CLEAN-CODE-REGELN")
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
            check_clean_code_rules(course)
        elif aktion == 6:
            preprocess_csv_export(course)
        elif aktion == 9:
            print("AUF WIEDERSEHEN.")
        else:
            print("Unbekannte Aktion. Erneute Eingabe.")
    except Exception as ex:
        print(ex)
    print()
