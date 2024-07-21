"""
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.



Вимоги до завдання:

Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.


Рекомендації для виконання:

Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа чітко відокремлені пробілами.
Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.


Критерії оцінювання:

Правильність визначення та повернення дійсних чисел функцією generator_numbers.
Коректність обчислення загальної суми в sum_profit.
Чистота коду, наявність коментарів та відповідність стилю кодування PEP8.


Приклад використання:

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



Очікуване виведення:

Загальний дохід: 1351.46
"""
from re import findall
from types import GeneratorType

TEST_STRING = """
Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""

def generator_numbers(text: str):
    """
    The function takes a series as an argument and rotates the generator,
    which iterates over all active numbers in the text.

    Args:
        text (str): Incomming text string.
    """
    # define regex to find numbers which have spaces before and after in string 
    regex = r'(?<=\s)-?\d+(?:\.\d+)?(?=\s)'
    # find all numbers
    numbers = findall(regex, text)
    # generate float numbers
    for n in numbers:
        yield float(n)

def sum_profit(text: str, func: generator_numbers) -> int:
    """
    Function must use the generator_numbers generator to calculate the total sum of the numbers
    in the input string and accept it as an argument when called.

    Args:
        text (str): Incomming text string.
        func (generator_numbers): generator_numbers function

    Returns:
        int: Total numbers sum.
    """
    return sum([num for num in generator_numbers(text=text)])

# Test function with test cases
def test_sum_profit():
    # Test case 1: Check for correct sum profit
    expected_sum = 1351.46
    actual_sum = sum_profit(TEST_STRING, generator_numbers)
    assert expected_sum == actual_sum, \
        f"Test sum_profit function is failed, expected total: '{expected_sum}', actual total: '{actual_sum}'"
    print("Sum profit test passed.")
    
def test_generator_numbers():
    # Test case 2: Check for correct generator work
    gen = generator_numbers(TEST_STRING)
    expected_numbers = [1000.01, 27.45, 324.0]
    assert isinstance(gen, GeneratorType), f"Function generator_numbers returns incorrect type '{type(gen)}'"
    for number in gen:
        assert isinstance(number, float), f"Value type is not float, type is '{type(number)}'"
        assert number in expected_numbers, f"Number '{number}' is not in expected numbers: \n{expected_numbers}"
    print("Generator numbers tests passed.")
    
# Uncomment the line below to run the test function
# test_sum_profit()
# test_generator_numbers()
