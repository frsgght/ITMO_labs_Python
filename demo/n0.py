import time

CSI = '\x1b['
ZERO = f"{CSI}0G"
ERASE = f"{CSI}2K"

def draw_progress(task_num, width):
    for n in range(task_num):
        for filled in range(width):
            bar = f"{'#' * filled}{'-' * (width - filled-1)}" #progressbar logic
            print(f"{ZERO}{ERASE}{n}:{bar}", end = "", flush = True)
            time.sleep(0.1)
        print('')


draw_progress(14, 18)
