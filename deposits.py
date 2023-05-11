per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))

for i in per_cent:
    per_cent[i] *= (money /100)
deposit = list(per_cent.values())
print('Умноженный список: ' + str(deposit))
print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))