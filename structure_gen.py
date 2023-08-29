from pathlib import Path
import json


def generate_project_structure(data, path=Path(".")):
    for item, value in data.items():
        directory_path = path / item
        directory_path.mkdir(exist_ok=True)
        init_file_path = directory_path / "__init__.py"
        init_file_path.touch()

        if value:
            generate_project_structure(value, path=directory_path)


# Пример входного JSON файла
json_data = {
    "generic": {
        "helpers": {},
        "checkers": {}
    },
    "tests": {
        "grpc": {},
        "http": {}
    },
    "data": {},
    "config": {},
    "modules": {
        "http": {},
        "grpc": {}
    }
}

generate_project_structure(json_data)
