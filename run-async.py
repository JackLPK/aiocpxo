import asyncio
import time
from check_pipx_oudates.lib_async import main


if __name__ == "__main__":
    START = time.time()
    asyncio.run(main())
    STOP = time.time()
    print(f'Total time used: {STOP - START:02f} s')
