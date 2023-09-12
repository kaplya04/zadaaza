stroka = input("Введите строку: ")
sl = {}
for a in stroka:
    sl[a] = stroka.count(a)
for a in sl:
    print(a, sl)