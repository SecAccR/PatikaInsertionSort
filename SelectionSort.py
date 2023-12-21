arrNumbers = [7, 3, 5, 8, 2, 9, 4, 15, 6]

intLenNumbers = len(arrNumbers)
i = 0

print(arrNumbers)
print()

for i in range(intLenNumbers-1):
    lowValue = arrNumbers[i]
    lowPosition = i
    j = i + 1
    for j in range(j, intLenNumbers):
        if (arrNumbers[j] < lowValue):
            lowValue = arrNumbers[j]
            lowPosition = j
    arrNumbers[lowPosition] = arrNumbers[i]
    arrNumbers[i] = lowValue
    print(arrNumbers)
