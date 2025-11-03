def sum_range():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    lo, hi = min(num1, num2), max(num1, num2)
    summ = sum(range(lo, hi + 1))
    print(f"Сумма от {lo} до {hi} = {summ}")


# ************************************************

def sum_even():
    summ = sum(num for num in range(1, 101) if num % 2 == 0)
    print(f"Сумма чётных: {summ}")


# ************************************************

def print_chars():
    text = input("Введите строку: ")
    for ch in text:
        print(ch)


# ************************************************

def filter_list():
    nums = input("Введите целые числа через пробел: ").split()
    nums = [int(num) for num in nums]
    evens = [num for num in nums if num % 2 == 0]
    print(f"Чётные числа: {evens}")


# ************************************************

def filter_capitalized():
    items = input("Введите строки через запятую: ").split(',')
    items = [s.strip() for s in items]
    res = [s for s in items if s[:1].isupper()]
    print(f"Строки с заглавной буквы: {res}")


# ************************************************

def filter_contains_python():
    items = input("Введите строки через запятую: ").split(',')
    items = [s.strip() for s in items]
    res = [s for s in items if 'Python' in s]
    print(f"Строки со словом 'Python': {res}")
