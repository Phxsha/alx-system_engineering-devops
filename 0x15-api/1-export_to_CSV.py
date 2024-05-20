#!/usr/bin/python3
"""
Fetch and export TODO list progress for a given employee ID
using the JSONPlaceholder API to a CSV file.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get the TODO list progress for the given employee ID.
    """
    # Fetch employee details
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos'
        f'?userId={employee_id}'
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if the employee exists
    if user_response.status_code != 200:
        print("Employee not found")
        return

    # Parse JSON responses
    user = user_response.json()
    todos = todos_response.json()

    # Extract employee details
    employee_name = user.get('username')

    # Write to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([
                employee_id,
                employee_name,
                todo.get('completed'),
                todo.get('title')
            ])


if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Get employee ID from the argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Get and export the employee's TODO list progress
    get_employee_todo_progress(employee_id)
