""" Version using threading """
import threading
import logging

from check_pipx_oudates.lib import get_top_lvl_pkgs, check_pkg


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(asctime)s:%(message)s'
    )


def thread_A(pkg: str):
    """ Wrap into thread. """
    logging.debug(f'thread start: {pkg}')
    check_pkg(pkg)
    logging.debug(f'thread end: {pkg}')


def main():
    """ main with threads """
    print('Outdated Top Level packages:')
    threads = []
    top_lvl_pkgs = get_top_lvl_pkgs()

    for pkg in top_lvl_pkgs:
        thr = threading.Thread(target=thread_A, args=(pkg, ), name=f'thr-{pkg}')
        threads.append(thr)
        thr.start()

    for thr in threads:
        logging.debug(f'join: {thr.name}')
        thr.join()
