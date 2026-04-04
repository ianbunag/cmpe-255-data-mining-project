import os
import joblib
import re
from pathlib import Path

dump_directory = os.path.join(os.path.dirname(__file__), 'serialize_dump')

def dump_to_file(variable, name: str):
    if not os.path.exists(dump_directory):
        os.makedirs(dump_directory)

    file_path = os.path.join(dump_directory, sanitize_name(name) + '.joblib')

    joblib.dump(variable, file_path)

    if not os.path.exists(file_path):
        print(f"Error: The dump file {file_path} was not created.")

def load_from_file(name: str):
    file_path = os.path.join(dump_directory, sanitize_name(name) + '.joblib')

    if os.path.exists(file_path):
        return joblib.load(file_path)
    else:
        print(f"Error: The dump file {file_path} was not found.")
        return None


def get_files(prefix: str) -> list[str]:
    matched_names = []

    for root, dirs, current_files in os.walk(dump_directory):
        for file in current_files:
            stem = Path(file).stem
            if stem.startswith(prefix):
                matched_names.append(stem)

    matched_names.sort()
    return matched_names

def sanitize_name(name: str):
    name = name.lower()
    name = re.sub(r'[^a-z0-9_]+', '_', name).strip('_')

    return name