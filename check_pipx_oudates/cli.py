import asyncio
import time
import sys

from check_pipx_oudates.lib_thread import main


def cli():
    """ Entry point, cli """
    try:
        mode = sys.argv[1]
    except IndexError:
        mode = 'async'

    START = time.time()
    
    if 'async'.startswith(mode):
        from check_pipx_oudates.lib_async import main
        asyncio.run(main())
        print('Mode: Asyncio')
        
    elif mode in 'threads':
        from check_pipx_oudates.lib_thread import main
        main()
        print('Mode: Threading')
        
    elif 'sync'.startswith(mode):
        from check_pipx_oudates.lib import main
        main()
        print('Mode: Synchronous')
        
    else:
        print(
            'Usage: \n'
            '  python3 -m check_pipx_oudates async \n'
            '  python3 -m check_pipx_oudates threads\n'
            '  python3 -m check_pipx_oudates sync\n'
            'See performance.\n'
        )
        
    STOP = time.time()
    print(f'Total time used: {STOP - START:02f} s')
