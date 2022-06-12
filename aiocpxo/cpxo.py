from .utils import get_package_name_ver, newer_package_ver


def main() -> None:
    info = get_package_name_ver()

    names = [x[0] for x in info]
    versions = [x[1] for x in info]

    name_pad = max(len(x) for x in names)
    ver_pad = max(len(x) for x in versions)

    new_versions = [newer_package_ver(name) for name in names]

    for i, new_ver in enumerate(new_versions):
        if new_ver:
            print(
                f"{names[i]:<{name_pad}}", f"{versions[i]:<{ver_pad}}", " --> ", new_ver
            )


if __name__ == "__main__":
    main()
