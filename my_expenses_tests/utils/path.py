from pathlib import Path

import my_expenses_tests


def abs_path_from_root(path: str):
    return Path(my_expenses_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
