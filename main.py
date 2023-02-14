import utils

STUDENTS_PATH = "students.json"
PROFESSIONS_PATH = "professions.json"


def main():

    #загрузка данных до старта
    students = utils.load_students(STUDENTS_PATH)
    professions = utils.load_students(PROFESSIONS_PATH)

    if len(students) == 0 or len(professions) == 0:
        print("Не удалось загрузить списки студентов или профессий")


    #получаем от пользователя номер студента
    print("Введите номер студента")
    user_input = input()

    #проверяем числовой ввод
    if not user_input.isdigit():
        print("Это не номер")

    student = utils.get_student_by_pk(students, int(user_input))


    #проверяем существование студента
    if student is None:
        print("Нет такого студента")

    print("Студент", student["full_name"])
    print("Знает", student["skills"])


    #получаем от пользователя профессию
    print("Введите профессию")
    user_input = input()

    profession = utils.get_profession_by_title(professions, user_input)

    if profession is None:
        print("Нет такой профессии")


    #считаем соответствие студента профессии
    fitness = utils.check_fitness(student["skills"], profession["skills"])

    has = ", ".join(fitness["has"])
    lacks = ", ".join(fitness["lacks"])
    fit_percent = fitness["fit_percent"]


    #выводим результаты
    print(f"Пригодность {fit_percent}%")
    print(f"{student['full_name']} знает {has}")
    print(f"{student['full_name']} не знает {lacks}")


if __name__ == '__main__':
    main()