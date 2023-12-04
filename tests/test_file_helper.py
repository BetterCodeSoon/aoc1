from pathlib import Path
from utils import file_helper

CURRENT_FILE = Path(__file__)
PROJECT_ROOT = CURRENT_FILE.parent.parent


def get_testfile_path():
    return PROJECT_ROOT / "resources" / "testfile1.txt"


class TestFileHelper:

    def test_read_file_lines(self):
        file_content = file_helper.read_file_lines(get_testfile_path())
        assert file_content == ['123\n', '\n', '456\n', '789']

