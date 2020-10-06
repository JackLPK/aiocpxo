import asyncio
import sys
# from pprint import pprint
from check_pipx_oudates.lib import get_top_lvl_pkgs, CMD, pkg_is_od


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy())


G_SAMPLE = {}

async def run(cmd, key:str):
    """ run cmd, store stdout to G_SAMPLE """
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    stdout = stdout.decode('utf-8').replace('\r', '').split('\n')
    stderr = stderr.decode('utf-8').replace('\r', '').split('\n')

    if proc.returncode != 0:
        print('error')
        raise Exception(f'Return code: {proc.returncode}')

    G_SAMPLE[key] = stdout
    return stdout


async def check_pkg(pkg: str):
    """ [Async Version]Check(display) if this package has new version """
    lines = await run(' '.join(CMD.pipx_runpip_pkg_list_oudate(pkg)), pkg)
    od_pkgs = pkg_is_od(pkg, lines)
    if od_pkgs:
        print(f'{pkg}:')
        print(od_pkgs)


async def main():
    top_lvl_pkgs = get_top_lvl_pkgs()
    tasks = []
    for pkg in top_lvl_pkgs:
        tasks.append(check_pkg(pkg))

    await asyncio.gather(*tasks)
