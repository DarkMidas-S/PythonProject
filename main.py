# Завдання 1
# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

def file_stats(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    kilkist_simvoliv = len(text)
    kilkist_ryadkiv = text.count("\n") + 1 if text else 0
    kilkist_cyfr = sum(ch.isdigit() for ch in text)
    kilkist_golosnyh = sum(ch.lower() in "aeuio" for ch in text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Кількість символів: {kilkist_simvoliv}\n")
        f.write(f"Кількість рядків: {kilkist_ryadkiv}\n")
        f.write(f"Кількість цифр: {kilkist_cyfr}\n")
        f.write(f"Кількість голосних літер: {kilkist_golosnyh}\n")


# Завдання 2
# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.

def count_word_in_file(word, filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return text.split().count(word.lower())


# Завдання 3
# Є текстовий файл. Видаліть з нього останній рядок.

def delete_last_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if lines:
        lines = lines[:-1]
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)


# Виконання завдань
if __name__ == "__main__":
    # Завдання 1
    file_stats("input.txt", "stats.txt")
    print("Статистика збережена у stats.txt")

    # Завдання 2
    word = input("Введіть слово: ")
    filename = input("Введіть назву файлу: ")
    print("Кількість слова у файлі:", count_word_in_file(word, filename))

    # Завдання 3
    delete_last_line("input.txt")
    print("Останній рядок видалено з input.txt")