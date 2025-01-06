from flask import Flask
import os

app = Flask(__name__)

# Path to the persistent file
PV_PATH = "/data/hello_count.txt"

# Ensure the directory exists
os.makedirs(os.path.dirname(PV_PATH), exist_ok=True)

# Function to read the current count from the file
def read_count():
    if os.path.exists(PV_PATH):
        with open(PV_PATH, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

# Function to write the count to the file
def write_count(count):
    with open(PV_PATH, "w") as f:
        f.write(str(count))

@app.route("/")
def hello_world():
    # Read the current count
    count = read_count()
    # Increment the count
    count += 1
    # Write the updated count back to the file
    write_count(count)
    # Return the "Hello World" message along with the count
    return f"Hello, World! This page has been visited {count} times.\n"

@app.route("/api/visits")
def api_visits():
    count = read_count()
    return jsonify({"visits": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
