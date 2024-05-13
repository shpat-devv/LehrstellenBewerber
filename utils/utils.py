import sys
import time

def waiting_animation(wait_time):
    symbols = ['|', '/', '-', '\\']
    while wait_time > 0:
        for symbol in symbols:
            sys.stdout.write(f'\rloading {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
            wait_time -= 1
    sys.stdout.write('\rDone!     ')
    sys.stdout.flush()