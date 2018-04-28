import time
import sys

def delay_print(s):
    for c in s:
             sys.stdout.write(c)
             sys.stdout.flush()
             time.sleep(0.25)
    print(' ')

#delay_print("Salam duste man")
