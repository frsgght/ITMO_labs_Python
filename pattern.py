ESC = "\x1b"

def printrow(num, n, x):
    if num <= 2:
        left_offset = 4 - num
        mid_offset = 5 - 2*num
        fill = 1 + 2* num
        s = f"{ESC}[0m{" " * left_offset*x}{ESC}[42m{" " * fill*x}{ESC}[0m{" " * mid_offset*x}{ESC}[42m{" " * fill*x}{ESC}[0m{" " * left_offset*x}"
        print(s*n)
    if 2 < num <= 5:
        left_offset = abs(4-num)
        fill = 15- left_offset*2
        s = f"{ESC}[0m{" " * left_offset*x}{ESC}[42m{" " * fill*x}{ESC}[0m{" " * left_offset*x}"
        print(s*n)
    if num > 5:
        left_offset = num-4
        mid_offset = 1 + 2*(num-6)
        fill = 5 - 2* (num-6)
        s = f"{ESC}[0m{" " * left_offset*x}{ESC}[42m{" " * fill*x}{ESC}[0m{" " * mid_offset*x}{ESC}[42m{" " * fill*x}{ESC}[0m{" " * left_offset*x}"
        print(s*n)


n = 1
x= 3
for i in range(9):
    printrow(i, n, x)