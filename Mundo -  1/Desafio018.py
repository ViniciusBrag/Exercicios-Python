from math import tan, cos, sinh, radians
a = float(input('Digite um angulo: '))
print('O cosseno do angulo de {} é {:.1f}'.format(a, cos(radians(a))))
print(('O seno do angulo de {} é {:.1f} '.format(a, sinh(radians(a)))))
print('A tangente de {} é {:.1f}'.format(a, tan(radians(a))))


