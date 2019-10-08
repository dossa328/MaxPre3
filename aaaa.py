out = 0
for i in range(30):
    i2 = i
    k = 30-i-i2
    if out <= k*i:
        out = k*i

print(out)