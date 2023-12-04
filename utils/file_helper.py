from pathlib import Path

CURRENT_FILE = Path(__file__)
PROJECT_ROOT = CURRENT_FILE.parent.parent


def get_resource_path(filename):
    return PROJECT_ROOT / "resources" / filename


def read_file_lines(filename):

    with open(filename, "r") as file:
        return file.readlines()
