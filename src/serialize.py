import os
import joblib
import re

dump_directory = os.path.join(os.path.dirname(__file__), 'serialize_dump')

def dump_to_file(variable, name):
    if not os.path.exists(dump_directory):
        os.makedirs(dump_directory)

    file_path = os.path.join(dump_directory, sanitize_name(name) + '.joblib')

    joblib.dump(variable, file_path)

    if not os.path.exists(file_path):
        print(f"Error: The dump file {file_path} was not created.")

def load_from_file(name):
    file_path = os.path.join(dump_directory, sanitize_name(name) + '.joblib')

    if os.path.exists(file_path):
        return joblib.load(file_path)
    else:
        print(f"Error: The dump file {file_path} was not found.")
        return None

def sanitize_name(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9_]+', '_', name).strip('_')

    return name