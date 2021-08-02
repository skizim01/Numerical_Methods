"""
Чисельне диференціювання функції,
основане на першій та другій 
інтерполяційних формулах Ньютона
"""
def Vars(w):
    q = 1 / (1/3 * w **4 + 6)
    return q


a, b, x1, x2, h = 6, 14, 6, 13, 1
x0 = a
x, y = [], []
fx2c = [1, 1, 11.0 / 12.0, 5.0 / 6.0, 137.0 / 180.0, 7.0 / 10.0]
p = {}


def Vars(w):
    q = 1 / (1/3 * w **4 + 6)
    return q


for i in range(b - a):
    p[f'delta{i + 1}y'] = []
for i in range(b - a + 1):
    y.append(Vars(x0))
    x.append(x0)
    x0 += 1
for i in range(b - a):
    if i == 0:
        for c in range(len(x) - 1):
            p[f'delta{i + 1}y'].append(y[c + 1] - y[c])
    else:
        for c in range(len(x) - 1 - i):
            p[f'delta{i + 1}y'].append(p[f'delta{i}y'][c + 1] - p[f'delta{i}y'][c])
            suma, s = [], []
for i in range(b - a):
    S = 0
    if i == 0:
        s.append(y[-1] - y[0])
        for c in p[f'delta{i + 1}y']:
            S += c
        suma.append(S)
    else:
        s.append(p[f'delta{i}y'][-1] - p[f'delta{i}y'][0])
        for c in p[f'delta{i + 1}y']:
            S += c
        suma.append(S)
    # for c in range
for i in range(len(x)):
    if x[i] == x1:
        nx1: int = i
    elif x[i] == x2:
        nx2 = i
snx1, snx2 = [], []


def AddSnx(x, nx1):
    lens = len(p[f'delta{i + 1}y'])

    if x >= lens - 1:
        x -= 1
        AddSnx(x, nx1)
    else:
        nx1.append(p[f'delta{i + 1}y'][x])


for i in range(b - a):
    AddSnx(nx2, snx2)
    AddSnx(nx1, snx1)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


fx1, fx2, e = 0, 0, 1
u = 1
for i in snx1:
    fx1 += i * (1 / e) * u
    e += 1
    u = u * (-1)
for i in range(len(snx2) - 3):
    fx2 += snx2[i + 1] * fx2c[i]
for i in range(8):
    string = f'delta{i+1}y:'

    for c in p[f'delta{i + 1}y']:
        if i % 2 == 1:
            string += " "
        string += f"   {toFixed(c, 6)};"
    print(string)
string1 = f'Сума            -            '
string2 = f'Контрольна сума - '
for c in range(8):
    if i == 0:
        string2 += "      "
    string2 += f" {toFixed(s[c], 6)};"
for c in range(8):
    string1 += f" {toFixed(suma[c], 6)};"

print(f"{string1}\n{string2}\nF'({x1})={toFixed(fx1, 6)}\nF''({x2})={toFixed(fx2, 6)}")
