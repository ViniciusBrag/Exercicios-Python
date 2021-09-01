print('=' * 4, 'Desafio ', '=' * 4)
from time import sleep
from datetime import date
import emoji

print('CON')
sleep(1.2)
print('TA')
sleep(1.2)
print('GEMMMM')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)

print(emoji.emojize('Feliz {} :boom:', use_aliases=True).format(date.today().year))
