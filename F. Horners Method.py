def horner(x, coef):
    if len(coef) == 1:
        return coef[0]
    return coef[0] + x * horner(x, coef[1:])


n = int(input())
x = float(input())
coef = []
for i in range(n + 1):
    coef.append(float(input()))

print(horner(x, coef))