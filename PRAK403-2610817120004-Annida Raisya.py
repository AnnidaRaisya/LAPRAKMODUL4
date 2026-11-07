data = input().split()
a = int(data[0])
b = int(data[1])

if a < b:
    i = a
    j = b
    while i <= b and j >= a:
        print(f"{i} {j}", end=" ")
        if i < b:
            print(" - ", end=" ")
        i += 1
        j -= 1
	
else:
    i = a
    j = b
    while i >= b and j <= a:
        print(f"{i} {j}", end=" ")
        if i > b:
            print(" - ", end=" ")
        i -= 1
        j += 1
	
print()
