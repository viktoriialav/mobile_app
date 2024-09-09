from pathlib import Path

import mobile_app_tests


def abs_path_from_root(path: str):
    return Path(mobile_app_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
