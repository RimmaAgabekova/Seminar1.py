# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int(input("Введите общее количество журавликов S  "))

kat = int((S//3)*2)
pet = int(kat//2)
ser = int(pet)
print(f" Катя - {kat}, Петя - {pet}, Сергей - {ser}")