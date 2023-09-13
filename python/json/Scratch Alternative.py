#Este archivo crea un diccionario filtered_data para hacer una lista solo de filtered todos y obtener solo un objeto json
import json
import requests
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# Define a dictionary to hold the filtered data.
filtered_data = {
    "filtered_todos": []
}

# Populate the filtered_todos list.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

filtered_data["filtered_todos"] = list(filter(keep, todos))

# Write filtered data to file.
with open("filtered_data_file_Alternative.json", "w") as data_file:
    json.dump(filtered_data, data_file, indent=2)
