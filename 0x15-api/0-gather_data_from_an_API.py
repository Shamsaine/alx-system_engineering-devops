#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    
    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch TODO list for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={
    employee_id
    }"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Extract employee name
    employee_name = user_data.get("name")
    
    # Calculate the number of completed tasks and the total number of tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    
    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks(
            {number_of_done_tasks}/{total_tasks}
            ):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

