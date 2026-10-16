import time

CSI = '\x1b['
ZERO = f"{CSI}0G"
ERASE = f"{CSI}2K"
RESET = f"{CSI}0m"
SIZE = 11

def draw_line(offset, filled, colour):
    offset_part = f"{' '*offset}"
    filled_part = f"{CSI}48;5;{colour}m{' ' * filled}"
    line = f"{ERASE}{offset_part}{filled_part}{RESET}"
    print(line)


def draw_romb(size, colour):
    center = size//2
    offset = center
    filled = 1

    for line in range(size):
        draw_line(offset, filled, colour)

        if line < center:
            offset = offset - 1
            filled = filled + 2
        else:
            offset += 1
            filled -= 2


def animate():
    colors = range(1, 231)
    while True:
        for color in colors:
            draw_romb(SIZE, color)
            print(f"{CSI}{SIZE}A{ZERO}", end="", flush=True)
            time.sleep(0.15)


animate()