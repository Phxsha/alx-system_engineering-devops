#!/usr/bin/python3
"""
Fetch and export TODO list progress for a given employee ID
using the JSONPlaceholder API to a JSON file.
"""

import json
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

    # Construct JSON data
    json_data = {str(employee_id): []}
    for todo in todos:
        json_data[str(employee_id)].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_name
        })

    # Write to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Get employee ID from the argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Get and export the employee's TODO list progress
    get_employee_todo_progress(employee_id)
