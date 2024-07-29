#!/usr/bin/python3
"""
This module fetches TODO list progress for a given employee ID using a REST API.
"""
import requests
import sys

def fetch_todo_list(employee_id):
    """
    Fetches and prints the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={
    employee_id
    }"
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    
    print(f"Employee {employee_name} is done with tasks(
            {number_of_done_tasks}/{total_tasks}
            ):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    fetch_todo_list(employee_id)

