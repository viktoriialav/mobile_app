from pathlib import Path

import my_expenses_tests


def abs_path_from_root(path: str):
    return Path(my_expenses_tests.__file__).parent.parent.joinpath(path).absolute().__str__()


def define_app_path(app_path):
    new_app_path = app_path if (app_path.startswith('/') or app_path.startswith('bs://') or app_path.startswith(
        'C:\\')) else abs_path_from_root(app_path)
    return new_app_path
