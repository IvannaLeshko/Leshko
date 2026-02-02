import math

x = float(input('Введіть число:'))

numerator = math.exp(-x) - 4 * math.log10(x)
denominator = math.log(x) - math.cos(abs(x + 1))

y = numerator / denominator

print('Результат: ' + str(y))