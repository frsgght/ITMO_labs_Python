import os

os.system("cls")

ESC = "\x1b"
r = 12
c = 1

for x in range(12):
    print(f"{ESC}[{r};{c+x}H-", end="")

for y in range(10):
    print(f"{ESC}[{r-y};{c}H|", end="")

print(f"{ESC}[{r};{c}H+", end="")

for x in range(9):
    y = x + 1
    print(f"{ESC}[{r-y};{c+x}H*", end="")

print(f"{ESC}[{r+2};1H", end="")