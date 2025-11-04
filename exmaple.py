def yoll(v, c):
    if v >= c:
        return v+c
    elif c > v:
        return c**v
    else:
        return c*v


r = yoll(5, 5)
print(f"Вывод ответа: {r=}")
a = r*1000
print(f"Ответ:{a}")
