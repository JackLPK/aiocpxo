import subprocess
from typing import List, Optional, Tuple


# TODO: spawn new shell and check
# def check_pipx_installed() -> None:
#     """Check pipx installed"""
#     if not shutil.which("vim"):
#         print("Error: pipx not found. Please ensure it is installed correcly.")
#         sys.exit(-1)


def get_package_name_ver() -> List[Tuple[str, str]]:
    """Returns package names and current version"""
    response = subprocess.run(
        # fmt: off
        ["pipx", "list"],
        capture_output=True, encoding="utf-8"
    )
    response.check_returncode()

    packages = []

    for line in response.stdout.split("\n"):
        line = line.strip()

        if line.startswith("package"):
            splitted = line.split(" ")
            packages.append((splitted[1], splitted[2][:-1]))  # strip last coma

    return packages


def newer_package_ver(package_name: str) -> Optional[str]:
    """Returns newer version else None"""
    response = subprocess.run(
        # fmt: off
        ["pipx", "runpip", package_name, "list", "-o"],
        capture_output=True, encoding='utf-8'
    )
    response.check_returncode()
    for line in response.stdout.split("\n"):
        if package_name in line:
            fields = [x.strip() for x in line.split(" ") if x]  # if x to skip ''
            return fields[2]

    return None
