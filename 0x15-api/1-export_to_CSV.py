#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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
    employee_username = user_data.get("username")
    
    # Prepare data for CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow(
                    [employee_id, employee_username, task.get("completed"), task.get("title")]
                    )
    
    print(f"Data exported to {csv_filename}")

