def zip_analog(a, b):
    return ((a[i], b[i]) for i in range(min(len(a), len(b))))

res = zip_analog("abcd", (10, 20, 30, 40))

print(*res)
