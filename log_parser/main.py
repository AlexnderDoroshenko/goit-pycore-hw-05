"""
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.



Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.



Для виконання завдання візьміть наступний приклад лог-файлу:

2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
"""
import sys
from collections import defaultdict
from pathlib import Path, PurePath

# Function to parse a single log line into components
def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into timestamp, log level, and message components.

    Args:
        line (str): A single line from the log file.

    Returns:
        dict: A dictionary containing parsed components:
        {'timestamp': 'YYYY-MM-DD HH:MM:SS', 'level': 'LOG_LEVEL', 'message': 'Log message'}
    """
    parts = line.strip().split(' ', maxsplit=3)
    timestamp = ' '.join(parts[:2])
    level = parts[2]
    message = parts[3]
    return {
        'timestamp': timestamp,
        'level': level,
        'message': message
    }

# Function to load logs from a file
def load_logs(file_path: str) -> list:
    """
    Loads log entries from a specified log file.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a parsed log entry.
    """
    logs = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        sys.exit(1)
    return logs

# Function to filter logs by a specific logging level
def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters log entries by a specific logging level.

    Args:
        logs (list): List of log entries (dictionaries).
        level (str): Logging level to filter by (e.g., 'INFO', 'DEBUG', 'ERROR', 'WARNING').

    Returns:
        list: Filtered list of log entries that match the specified logging level.
    """
    return list(filter(lambda d: d['level'] == level, logs))

# Function to count logs by logging level
def count_logs_by_level(logs: list) -> dict:
    """
    Counts log entries by logging level.

    Args:
        logs (list): List of log entries (dictionaries).

    Returns:
        dict: A dictionary where keys are logging levels ('INFO', 'DEBUG', 'ERROR', 'WARNING')
        and values are the counts of log entries for each level.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

# Function to display log counts in a formatted table
def display_log_counts(counts: dict):
    """
    Displays log counts in a formatted table.

    Args:
        counts (dict): A dictionary where keys are logging levels ('INFO', 'DEBUG', 'ERROR', 'WARNING')
        and values are the counts of log entries for each level.

    Prints:
        Formatted table displaying logging levels and their corresponding counts.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.ljust(17)}| {count}")

# Test function to validate log analysis functions
def test_log_analysis():
    """
    Tests log analysis functions:
        parse_log_line()
        load_logs()
        filter_logs_by_level()
        count_logs_by_level()
        display_log_counts()
    """
    # Test parsing a log line
    log_line = "2024-01-22 08:30:01 INFO User logged in successfully."
    parsed_log = parse_log_line(log_line)
    assert parsed_log == {
        'timestamp': '2024-01-22 08:30:01',
        'level': 'INFO',
        'message': 'User logged in successfully.'
    }, "Parsing log line failed"

    # Test loading logs from a file
    file_path = Path(__file__).resolve()
    test_file_path = PurePath(file_path.parent, "test_logs.log")
        
    logs = load_logs(test_file_path)
    assert len(logs) == 10, "Loading logs failed"
    assert logs[0]['message'] == "User logged in successfully.", "Log message mismatch"

    # Test filtering logs by level
    filtered_logs = filter_logs_by_level(logs, 'DEBUG')
    assert len(filtered_logs) == 3, "Filtering logs by level failed"
    assert filtered_logs[0]['level'] == 'DEBUG', "Filtered log level mismatch"

    # Test counting logs by level
    counts = count_logs_by_level(logs)
    assert counts['INFO'] == 4, "Counting logs by level (INFO) failed"
    assert counts['DEBUG'] == 3, "Counting logs by level (DEBUG) failed"

    # Test display log counts
    import io
    import sys
    output = io.StringIO()
    sys.stdout = output
    display_log_counts(counts)
    sys.stdout = sys.__stdout__  # Restore stdout
    
    # Calculate the number of actual data rows
    printed_output = output.getvalue().strip().split('\n')[2:]  # Subtracting header and separator row
    assert len(printed_output) == len(counts), "Displaying log counts failed"

    print("All tests passed successfully!")
    
# Uncomment the line below to run the tests
# test_log_analysis()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file> [<log_level>]")
        sys.exit(1)
    # get arguments
    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    # get logs
    logs_list = load_logs(log_file)
    # count logs records by its level
    counts = count_logs_by_level(logs_list)
    # display log counts
    display_log_counts(counts)
    # display filtered log details by its level
    if log_level:
        filtered_logs = filter_logs_by_level(logs_list, log_level.upper())
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log_line in filtered_logs:
            print(f"{log_line["timestamp"]} - {log_line["message"]}")
