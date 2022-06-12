import asyncio

from .utils import get_package_name_ver


async def newer_package_ver(package_name: str):
    """Returns newer version else None"""
    cmd = " ".join(["pipx", "runpip", package_name, "list", "-o"])

    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout_raw, stderr_raw = await proc.communicate()

    stdout, stderr = (
        stdout_raw.decode("utf-8").strip(),
        stderr_raw.decode("utf-8").strip(),
    )

    if stderr:
        print("Error:", stderr)

    for line in stdout.split("\n"):
        if package_name in line:
            fields = [x.strip() for x in line.split(" ") if x]  # if x to skip ''
            return fields[2]

    return None


async def amain() -> None:
    info = get_package_name_ver()

    name_pad = max(len(x[0]) for x in info)
    ver_pad = max(len(x[1]) for x in info)

    async def inner(name, ver):
        new_ver = await newer_package_ver(name)

        if new_ver:
            print(f"{name:<{name_pad}}", f"{ver:<{ver_pad}}", " --> ", new_ver)

    await asyncio.gather(*(inner(name, ver) for name, ver in info))


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    # asyncio.run(amain())
    main()
