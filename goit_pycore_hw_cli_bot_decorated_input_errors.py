"""
Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



Вимоги до завдання:

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


Рекомендації для виконання:

В якості прикладу додамо декоратор input_error для обробки помилки ValueError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner
"""
from typing import Dict
from io import StringIO 
from unittest.mock import patch

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me your name and phone please."
        except IndexError:
            return "To many names, try the all command to investigate."
        except KeyError:
            return "Give me the correct name please, try the all command to investigate."

    return inner


def parse_input(user_input: str) -> tuple:
    """
    Parses the user input into a command and its arguments.
    
    Parameters:
    - user_input (str): The raw input string from the user.
    
    Returns:
    - tuple: A tuple where the first element is the command (str) and the rest are arguments (list of str).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Adds a new contact to the contacts dictionary.
    
    Parameters:
    - args (tuple): A tuple containing the name and phone number of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A message indicating the contact was added.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Changes the phone number of an existing contact.
    
    Parameters:
    - args (tuple): A tuple containing the name and new phone number of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A message indicating the contact was updated or not found.
    """
    name, phone = args
    if contacts:
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
    return "Contact not found."


def show_phone(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Retrieves the phone number of a specified contact.
    
    Parameters:
    - args (tuple): A tuple containing the name of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: The phone number of the contact or a message indicating the contact was not found.
    """
    name, *_ = args
    if contacts:
        if name in contacts:
            return contacts[name]
    return "Contact not found."

def show_all(contacts: Dict[str, str]) -> str:
    """
    Returns a string representation of all contacts.
    
    Parameters:
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A string representation of the contacts dictionary.
    """
    return str(contacts)

def main():
    """
    The main function of the assistant bot. It initializes the contacts dictionary and processes user commands.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command.lower() in ["close", "exit", "quit", "q"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
            
# add block with tests for the functions
def test_functions():
    contacts = {}
    assert add_contact(("John", "123456"), contacts) == "Contact added."
    assert add_contact(("Alice", "987654"), contacts) == "Contact added."
    assert add_contact(("John", "098765"), contacts) == "Contact added."
    assert change_contact(("John", "098765"), contacts) == "Contact updated."
    assert change_contact(("Bob", "123456"), contacts) == "Contact not found."
    assert show_phone(("John",), contacts) == "098765"
    assert show_phone(("Alice",), contacts) == "987654"
    assert show_phone(("Bob",), contacts) == "Contact not found."
    assert show_all(contacts) == "{'John': '098765', 'Alice': '987654'}"
    assert add_contact(("John"), contacts) == "Give me your name and phone please."
    assert change_contact(("098765"), contacts) == "Give me your name and phone please."
    print("All function tests passed.")
    
def test_main():
    # Define test data as a list of tuples, where each tuple contains a user input and the expected output.
    test_data = [
        ("hello", "How can I help you?"),  # Test greeting
        ("add John 123456", "Contact added."),  # Test adding a new contact
        ("phone John", "123456"),  # Test retrieving a contact's phone number
        ("change John 098765", "Contact updated."),  # Test changing a contact's phone number
        ("phone John", "098765"),  # Test retrieving the updated phone number
        ("all", "{'John': '098765'}"),  # Test displaying all contacts
        ("wrong_command", "Invalid command."),  # Wrong command
        ("close", "Good bye!")  # Test closing the application
    ]
    # Patch the input function to simulate user input based on the test data.
    with patch("builtins.input", side_effect=[i[0] for i in test_data]):
        # Patch sys.stdout to capture the output of the main function.
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()  # Call the main function to process the simulated user input.
            # Assert that the captured output matches the expected output defined in the test data.
            expected_output = f"Welcome to the assistant bot!\n{'\n'.join([i[1] for i in test_data])}".strip().split('\n')
            actual_output = fake_out.getvalue().strip().split('\n')
            assert actual_output == expected_output, \
                "Test main function is failed output is not equal to expected"
    print("The main function tests passed.")
            
# Uncomment the line below to run the tests
# test_functions()
# test_main()
            
if __name__ == "__main__":
    main()
