import os


def ask_for_course_name():
    return input("Kurs (format: ginf{W}_XYZ)? ")


def ask_for_exam_number():
    return input("Pruefungsnummer (format: XY)? ")


def ask_for_task_file_name():
    return input("Dateiname (format: XYZ.XYZ)? ")


def press_enter_to_continue():
    input("Mit ENTER geht es weiter...")


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


def create_student_abgaben_dirs(course_name, exam_number):
    abgaben_path = f"../97_pruefungen/{exam_number}/abgaben"
    if not os.path.isdir(abgaben_path):
        print(f"ERROR: {abgaben_path} gibt es nicht.")
        press_enter_to_continue()
    else:
        student_names = collect_student_names(course_name)
        for index in range(len(student_names)):
            student_name = student_names[index]
            student_path = f"{abgaben_path}/{index + 1}_{student_name}"
            os.mkdir(student_path)


def create_task_file(course_name, exam_number, task_file_name):
    abgaben_path = f"../97_pruefungen/{exam_number}/abgaben"
    if not os.path.isdir(abgaben_path):
        print(f"ERROR: {abgaben_path} gibt es nicht.")
        press_enter_to_continue()
    else:
        student_names = collect_student_names(course_name)
        error_counter = 0
        student_count = len(student_names)
        for index in range(student_count):
            student_name = student_names[index]
            student_path = f"{abgaben_path}/{str(index + 1).zfill(2)}_{student_name}"
            if not os.path.isdir(student_path):
                print(f"[{student_name}] ERROR: {student_path} gibt es nicht.")
                error_counter += 1
                press_enter_to_continue()
            else:
                exam_question_file_path = f"{student_path}/{task_file_name}"
                try:
                    with open(exam_question_file_path, mode="x"):
                        pass
                except Exception as ex:
                    error_counter += 1
                    print(ex)

        if student_count - error_counter != student_count:
            print(f"ERROR: Es gab Fehler beim Erstellen...")
            print(f"Anzahl Fehler: {error_counter}")
            print(f"Anzahl SuS: {student_count}")
            press_enter_to_continue()
        else:
            print("Alle erstellt")


print("WILLKOMMEN ZUM PRUEFUNGSTOOL")
course = ask_for_course_name()
exam_number = ask_for_exam_number()
aktion = 0
while aktion != 9:
    print("==== AUSWAHL ====")
    print("1: ORDNER FUER DIE ABGABEN ERSTELLEN")
    print("2: DATEI FUER EINE AUFGABE ERSTELLEN (FUER ALLE SUS)")
    print("9: EXIT")
    try:
        aktion = int(input("Aktion? "))
        if aktion == 1:
            create_student_abgaben_dirs(course, exam_number)
        elif aktion == 2:
            file_name = ask_for_task_file_name()
            create_task_file(course, exam_number, file_name)
        elif aktion == 9:
            print("AUF WIEDERSEHEN.")
        else:
            print("Unbekannte Aktion. Erneute Eingabe.")
    except Exception as ex:
        print(ex)
    print()
