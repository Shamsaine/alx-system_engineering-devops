#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee data
employee_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )

if employee_response.status_code != 200:
    print("Error fetching employee data")
    sys.exit(1)

employee_data = employee_response.json()

employee_name = employee_data.get('name')

# Fetch TODO list data
todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )

if todos_response.status_code != 200:
    print("Error fetching TODO list data")
    sys.exit(1)

todos_data = todos_response.json()

total_tasks = len(todos_data)
done_tasks = [task for task in todos_data if task.get('completed')]
number_of_done_tasks = len(done_tasks)

# Print the TODO list progress
print(f"Employee {employee_name} is done with tasks(
        {number_of_done_tasks}/{total_tasks}
        ):")

for task in done_tasks:
    print(f"\t {task.get('title')}")
