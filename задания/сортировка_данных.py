import time
import random
# Пузырьковый алгоритм


def buble(p):
    s = len(p)
    start = time.time()
    for i in range(s):
        for j in range(0, s-i-1):
            if p[j] > p[j+1]:
                p[j], p[j+1] = p[j+1], p[j]
    end = time.time()
    otime = end - start
    return p, otime
# Сортировка выбором


def sb(p):
    s = len(p)
    start = time.time()
    for i in range(s):
        min_index = i
        for j in range(i+1, s):
            if p[j] < p[min_index]:
                min = j
        p[i], p[min_index] = p[min_index], p[i]
    end = time.time()
    otime = end - start
    return p, otime
# Сортировка вставками


def vs(p):
    s = len(p)
    start = time.time()
    for i in range(1, s):
        u = p[i]
        j = i-1
        while j >= 0 and p[j] > u:
            p[j+1] = p[j]
            j -= 1
        p[j+1] = u
    end = time.time()
    otime = end - start
    return p, otime


# Список с int
print("Целые числа")
n = 300
for i in range(8):
    w = [random.randint(1, 1000) for _ in range(n)]
    r, t = buble(w.copy())
    r1, t1 = sb(w.copy())
    r2, t2 = vs(w.copy())
    print(f"Пузырьковый метод: время {t:.5f}, размер массива: {n} ")
    print(f"Сортировка выбором:  время {t1:.5f}, размер массива: {n}")
    print(f"Сортировка вставками: время {t2:.5f}, размер массива: {n}")
    n += 100
# Список со string
print("Строки")
n = 300
words = ["солнце", "луна", "яблоко", "корень", "яхта",
         "кукла", "номер", "почта", "хамелеон", " мама"]
for i in range(8):
    l = [random.choice(words) for _ in range(n)]
    m, ti = buble(l.copy())
    m1, ti1 = sb(l.copy())
    m2, ti2 = vs(l.copy())
    print(f"Пузырьковый метод: время {ti:.5f}, размер массива: {n} ")
    print(f"Сортировка выбором:  время {ti1:.5f}, размер массива: {n}")
    print(f"Сортировка вставками: время {ti2:.5f}, размер массива: {n}")
    n += 100
# Список с float
print("Вещественные числа")
n = 300
for i in range(8):
    o = [random.uniform(1, 1000) for _ in range(n)]
    u, tim = buble(o.copy())
    u1, tim1 = sb(o.copy())
    u2, tim2 = vs(o.copy())
    print(f"Пузырьковый метод: время {tim:.5f}, размер массива: {n} ")
    print(f"Сортировка выбором:  время {tim1:.5f}, размер массива: {n}")
    print(f"Сортировка вставками: время {tim2:.5f}, размер массива: {n}")
    n += 100
