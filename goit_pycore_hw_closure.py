"""
Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного контексту, тобто з області, де вона була оголошена.

Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.



Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати вираз: 
𝐹
𝑛
=
𝐹
𝑛
−
1
+
𝐹
𝑛
−
2
F 
n
​
 =F 
n−1
​
 +F 
n−2
​
 .

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.



Вимоги до завдання:

Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
Використання рекурсії для обчислення чисел Фібоначчі.


Рекомендації для виконання:

В якості рекомендації ми надамо псевдо код завдання.

☝ Псевдокод - це спосіб запису алгоритму або програмного коду, який використовується для опису ідеї або процесу у вигляді, зрозумілому для людей. Він не призначений для безпосереднього виконання на комп'ютері, але допомагає розробникам чітко зрозуміти та спланувати, як буде працювати програма чи алгоритм. Головна його мета - передати ідею алгоритму чітко та просто.


Ось псевдокод для функції caching_fibonacci, яка обчислює числа Фібоначчі з використанням кешування:

ФУНКЦІЯ caching_fibonacci
    Створити порожній словник cache

    ФУНКЦІЯ fibonacci(n)
        Якщо n <= 0, повернути 0
        Якщо n == 1, повернути 1
        Якщо n у cache, повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Повернути cache[n]

    Повернути функцію fibonacci
КІНЕЦЬ ФУНКЦІЇ caching_fibonacci



Функція caching_fibonacci створює внутрішню функцію fibonacci і словник cache для зберігання результатів обчислення чисел Фібоначчі. Кожен раз, коли викликається fibonacci(n), спочатку перевіряється, чи вже збережено значення для n у cache. Якщо значення є у кеші, воно повертається негайно, що значно зменшує кількість рекурсивних викликів. Якщо значення відсутнє у кеші, воно обчислюється рекурсивно і зберігається у cache. Функція caching_fibonacci повертає внутрішню функцію fibonacci, яка тепер може бути використана для обчислення чисел Фібоначчі з використанням кешування.



Критерії оцінювання:

Коректність реалізації функції fibonacci(n) з урахуванням використання кешу.
Ефективне використання рекурсії та кешування для оптимізації обчислень.
Чистота коду, включаючи читабельність та наявність коментарів.


Приклад використання:

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
"""

def caching_fibonacci() -> int:
    """
    The caching_fibonacci function inverts the internal fibonacci function so
    that it can now be used to calculate Fibonacci numbers using caching methods.

    Returns:
        int: Fibonacci number
    """
    # create empty cache dictionary
    cache = {}
    
    def fibonacci(n: int) -> int:
        """
        Function calculates the nth Fibonacci numbers. 
        If the number is already in the cache, 
        the function can rotate the value from the cache.

        Args:
            n (int): Fibonacci number
            
        Returns:
            int: Fibonacci number
        """
        # case n = 0 
        if n <= 0:
            return 0
        # case n = 1
        elif n == 1:
            return 1
        # case n already in cache
        elif n in cache:
            return cache[n]
        # case not in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# Test function with test cases
def test_caching_fibonacci():
    # getting fibonaccs funtion 
    c_f = caching_fibonacci()
    # Test case 1: n = 0
    assert 0 == c_f(0), f"The test is failed for n = 0, result is '{c_f(0)}'"
    # Test case 2: n = 1
    assert 1 == c_f(1), f"The test is failed for n = 1, result is '{c_f(1)}'"
    # Test case 3: n = 10
    assert 55 == c_f(10), \
        f"The test is failed for n = 10, result '{c_f(10)}' not equal to 55"
    # Test case 4: n = 15
    assert 610 == c_f(15), \
        f"The test is failed for n = 15, result '{c_f(15)}' not equal to 610"
    print("All test cases passed successfully")

# Uncomment the line below to run the test function
# test_caching_fibonacci()
