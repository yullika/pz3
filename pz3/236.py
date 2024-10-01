import Levenshtein
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


rat = fuzz.ratio('Привет МАИ', 'ривет И') #обычное сравнение
print(rat)

a = fuzz.partial_ratio('Привет МАИ', 'Пивет МАИ!') #частичное сравнение
print(a)

a1 = fuzz.token_sort_ratio('Привет наш МАИ', 'МАИ наш любимый Привет') #Сравнение по токену
print(a1)

a2 = fuzz.token_set_ratio('Привет наш МАИ', 'МАИ МАИ наш наш наш ПриВЕт')#Сравнение по токену/2
print(a2)

rat1 = fuzz.WRatio('Привет наш МАИ', '!ПриВЕт наш МАИ!')  #Продвинутое обычное сравнение
print(a)
names = ['Игорь', 'Марина', 'Алексей', 'Вика', 'Юля', 'Рома', 'Света', 'Оля']
k = process.extract('Юля', names, limit=2)
print(k)

rat_3 = Levenshtein.distance('Алексей', 'Рома')

print(rat_3)