from time import perf_counter

import click

from .cpxo import main as run_sync
from .cpxo_async import main as run_async
from .cpxo_thread import main as run_thread
# from .utils import check_pipx_installed


@click.command()
@click.option("--time", "-T", is_flag=True, default=False, help="time program")
@click.option("--asynchronous", "-a", is_flag=True, default=False, help="use asyncio version")
@click.option("--thread", "-t", is_flag=True, default=False, help="number of threads")
def cli(time: bool, asynchronous: bool, thread: int) -> None:
    """Entry point for program"""
    # check_pipx_installed()

    START = perf_counter()

    if asynchronous:
        run_async()

    elif thread:
        run_thread()

    else:
        run_sync()

    STOP = perf_counter()
    if time:
        print(f"Total time used: {STOP - START:.3f} s")


def shortcut_async() -> None:
    """ A shortcut entry point """
    # check_pipx_installed()
    run_async()


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
