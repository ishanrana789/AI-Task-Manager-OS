import spacy
from datetime import datetime, timedelta
import hashlib
import pyotp
from cryptography.fernet import Fernet
import json
from IPython.display import display, clear_output
import ipywidgets as widgets

# Initialize NLP
nlp = spacy.load("en_core_web_sm")

# ======================
# 1. SECURITY MODULE
# ======================
class AuthManager:
    def __init__(self):
        self.users = {}
        self.otp_secrets = {}
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def register_user(self, username, password):
        if username in self.users:
            return "Username already exists!"

        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        otp_secret = pyotp.random_base32()
        self.otp_secrets[username] = otp_secret

        user_data = {"password": hashed_pw, "tasks": []}
        encrypted_data = self.cipher.encrypt(json.dumps(user_data).encode())
        self.users[username] = encrypted_data

        return f"User registered! OTP Secret: {otp_secret}"

    def login(self, username, password, otp):
        if username not in self.users:
            return "User not found!"

        totp = pyotp.TOTP(self.otp_secrets[username])
        if not totp.verify(otp):
            return "Invalid OTP!"

        decrypted_data = json.loads(self.cipher.decrypt(self.users[username]).decode())
        if decrypted_data["password"] != hashlib.sha256(password.encode()).hexdigest():
            return "Invalid password!"

        return "Login successful!"

# ======================
# 2. TASK MANAGER MODULES
# ======================
class TaskParser:
    def parse_task(self, text):
        doc = nlp(text)
        task = {"name": text, "priority": "medium", "deadline": None}

        if "urgent" in text.lower():
            task["priority"] = "high"
        elif "low" in text.lower():
            task["priority"] = "low"

        for token in doc:
            if token.text.lower() == "tomorrow":
                task["deadline"] = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            elif token.text.lower() == "today":
                task["deadline"] = datetime.now().strftime("%Y-%m-%d")

        return task

class AITaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: (x["priority"] != "high", x["deadline"] or "9999-12-31"))

    def get_tasks(self):
        return self.tasks

# ======================
# 3. UI WITH IPYWIDGETS
# ======================
auth = AuthManager()
parser = TaskParser()
scheduler = AITaskScheduler()

# Widgets
username_input = widgets.Text(placeholder="Username")
password_input = widgets.Password(placeholder="Password")
otp_input = widgets.Text(placeholder="OTP")
task_input = widgets.Text(placeholder="Enter task (e.g., 'Urgent: Finish report by tomorrow')")

register_button = widgets.Button(description="Register")
login_button = widgets.Button(description="Login")
add_task_button = widgets.Button(description="Add Task")
logout_button = widgets.Button(description="Logout")

output = widgets.Output()

# Button Actions
def on_register_clicked(b):
    with output:
        clear_output()
        result = auth.register_user(username_input.value, password_input.value)
        print(result)

def on_login_clicked(b):
    with output:
        clear_output()
        result = auth.login(username_input.value, password_input.value, otp_input.value)
        print(result)
        if result == "Login successful!":
            print("\n--- Add Tasks Below ---")

def on_add_task_clicked(b):
    with output:
        clear_output()
        task = parser.parse_task(task_input.value)
        scheduler.add_task(task)
        print(f"Added: {task['name']} (Priority: {task['priority']}, Deadline: {task['deadline']}")
        print("\n--- Current Tasks ---")
        for task in scheduler.get_tasks():
            print(f"{task['priority'].upper()}: {task['name']}")

def on_logout_clicked(b):
    with output:
        clear_output()
        print("Logged out. Ready for a new user.")

register_button.on_click(on_register_clicked)
login_button.on_click(on_login_clicked)
add_task_button.on_click(on_add_task_clicked)
logout_button.on_click(on_logout_clicked)

# Layout
auth_box = widgets.VBox([
    widgets.HBox([username_input, password_input, otp_input]),
    widgets.HBox([register_button, login_button])
])
task_box = widgets.VBox([
    task_input,
    widgets.HBox([add_task_button, logout_button])
])

display(auth_box, task_box, output)
