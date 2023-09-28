from pathlib import Path

EXCLUDED_FOLDERS = [".idea", ".pytest_cache", "__pycache__", "venv", "venv_clients", ".git", "allure-results", "images",
                    ".gitignore"]


def parse_project_structure(path=Path("."), indent=0, include_files=True, is_last=True, excluded_files=[],
                            folder_descriptions={}):
    structure = ""

    items = list(path.iterdir())
    if include_files:
        items = sorted(items, key=lambda x: (x.is_file(), x))
        EXCLUDED_FOLDERS.extend(excluded_files)
        items = [item for item in items if item.name not in EXCLUDED_FOLDERS]

    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)

        if item.is_file():
            structure += f"{'│   ' * indent}{'└── ' if is_last_item else '├── '}{item.name}\n"
        elif item.is_dir():
            folder_name = item.name
            structure += f"{'│   ' * indent}{'└── ' if is_last_item else '├── '}{folder_name}"

            if folder_name in folder_descriptions:
                structure += f" ({folder_descriptions[folder_name]})"

            structure += "\n"
            structure += parse_project_structure(
                path=item,
                indent=indent + 1,
                include_files=include_files,
                is_last=is_last_item,
                excluded_files=excluded_files,
                folder_descriptions=folder_descriptions
            )

    return structure


# Пример использования:
project_path = Path("/Users/vmenshikov/PycharmProjects/pvz-qa-api")  # Укажите путь к вашему проекту
include_files = True  # Установите значение False, чтобы отображать только папки
excluded_files = [
    ".gitignore",
    "__init__.py"
]  # Укажите файлы, которые нужно исключить
folder_descriptions = {
    "routes": "Описание папки 1",
    "utilities": "Описание папки 1",
    "clients": "Описание папки 1",
}
project_structure = parse_project_structure(
    path=project_path,
    include_files=include_files,
    excluded_files=excluded_files,
    folder_descriptions=folder_descriptions
)

with open("project_structure.md", "w") as f:
    f.write('```\n' + project_structure + '```')
