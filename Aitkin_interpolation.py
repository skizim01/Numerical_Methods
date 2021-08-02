x = []
y = []
x0, h, xc, x_max = 6, 1, 7.41, 13
xi = x0


def Vars(w):
    y = 1 / (1 / 3 * w ** 4 + 6)
    return y


def Vars1(x0, x1, y0, y1):
    yo = (y0 * (x1 - xc) - y1 * (x0 - xc)) / (x1 - x0)
    return yo


while x0 <= x_max:
    y.append(Vars(x0))
    x.append(x0)
    x0 += h
p = {}
for i in range(len(x) - 1):
    p[f'p{i}'] = []
for i in range(len(x) - 1):
    if i == 0:
        for q in range(len(x) - 1 - i):
            p[f'p{i}'].append(Vars1(x[q], x[q + 1], y[q], y[q + 1]))
    else:
        for rt in range(len(x) - 1 - i):
            p[f'p{i}'].append(Vars1(x[rt], x[rt + 1 + i], p[f'p{i - 1}'][rt], p[f'p{i - 1}'][rt + 1]))
        if i == len(x) - 2 and abs(p[f'p{i}'][0] - p[f'p{i - 1}'][0]) > 0.00001:
            print('занадто малий проміжок обчислення')

        elif abs(p[f'p{i}'][0] - p[f'p{i - 1}'][0]) < 0.000001:
            print('Відповідь:\n')
            print(f"{p[f'p{i}'][0]:.6}")
            v = p[f'p{i}'][0]
            qwe = i
            break
