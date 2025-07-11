import os, sys
from contextlib import contextmanager

if os.name == 'nt':
    import msvcrt
    @contextmanager
    def suppress_input():
        while msvcrt.kbhit():
            msvcrt.getch()
        yield
else:
    import termios, tty
    @contextmanager
    def suppress_input():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            yield
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)