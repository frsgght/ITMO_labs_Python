f = open("sequence.txt")
s1 = 0
s2 = 0

for i in f:
    a = float(i.strip())

    if 0 <= a <= 5:
        s1 += 1
    elif -5 <= a < 0:
        s2 += 1

f.close()

scale = 20
if s1 + s2 > 0:
    x1 = round(scale * (s1 / (s2 + s1)))
    x2 = scale - x1
    txt1 = str(x1 / scale*100) + '%'
    txt2 = str(x2 / scale*100) + '%'
    ESC = "\x1b"
    print(f"{ESC}[42m{txt1 + ' ' * (x1-len(txt1))}{ESC}[41m{txt2 + ' ' * (x2-len(txt2))}{ESC}[0m")
    print(f"{ESC}[32m◆ -5<=x<=0{ESC}[0m")
    print(f"{ESC}[31m◆ 0>=x>=5{ESC}[0m")

f.close()