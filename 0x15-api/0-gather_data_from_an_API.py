#!/usr/bin/python3
"""
Fetch and display TODO list progress for a given employee ID
using the JSONPlaceholder API.
"""

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

    # Extract employee name
    employee_name = user.get('name')

    # Calculate task progress
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the result in the specified format
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get employee ID from the argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Get and display the employee's TODO list progress
    get_employee_todo_progress(employee_id)
