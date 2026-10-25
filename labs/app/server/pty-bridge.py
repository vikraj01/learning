"""Run bash in a real terminal (a pty) and pipe it to the lab server.

stdin  -> keys typed in the browser
stdout <- what bash prints
fd 3   -> resize messages, one per line: "<cols> <rows>"

Usage: python3 pty-bridge.py <cols> <rows> <rcfile>
"""
import fcntl
import os
import pty
import select
import signal
import struct
import sys
import termios

cols, rows, rcfile = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]

pid, master = pty.fork()
if pid == 0:
    os.execvp("bash", ["bash", "--rcfile", rcfile, "-i"])


def set_size(c, r):
    fcntl.ioctl(master, termios.TIOCSWINSZ, struct.pack("HHHH", r, c, 0, 0))


def write_all(fd, data):
    while data:
        n = os.write(fd, data)
        data = data[n:]


set_size(cols, rows)
CONTROL = 3
watch = [0, master, CONTROL]
pending = b""

while True:
    try:
        ready, _, _ = select.select(watch, [], [])
    except InterruptedError:
        continue

    if master in ready:
        try:
            data = os.read(master, 65536)
        except OSError:
            break
        if not data:
            break
        write_all(1, data)

    if 0 in ready:
        data = os.read(0, 65536)
        if not data:
            break
        write_all(master, data)

    if CONTROL in ready:
        data = os.read(CONTROL, 1024)
        if not data:
            watch.remove(CONTROL)
            continue
        pending += data
        while b"\n" in pending:
            line, pending = pending.split(b"\n", 1)
            try:
                c, r = (int(x) for x in line.split())
                set_size(c, r)  # the kernel tells bash (SIGWINCH)
            except ValueError:
                pass

try:
    os.kill(pid, signal.SIGHUP)
except ProcessLookupError:
    pass
