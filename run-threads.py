import time
from check_pipx_oudates.lib_thread import main


if __name__ == "__main__":
    START = time.time()
    main()
    STOP = time.time()
    print(f'Total time used: {STOP - START:02f} s')
