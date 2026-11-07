n, kelipatan = map(int, input().split())

total = 0

for i in range(1, n + 1):
    jumlah = 0
    hasil = []

    for j in range(i, 0, -1):
        hasil.append(f"({j} * {kelipatan})")
        jumlah += j * kelipatan

    print(" + ".join(hasil), "=", jumlah)
    total += jumlah

print(total)