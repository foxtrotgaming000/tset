import time
spin = ['-', '\\', '|', '/']

try:
    while True:
        for e in range(len(spin)):
            print('\rSpin > [' + spin[e] + ']', end='')
            time.sleep(0.157)
except KeyboardInterrupt:
    print('\r\n:)',)
