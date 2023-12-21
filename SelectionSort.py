def selectionSort(numbers : list):
    print(numbers)
    print()

    lenNumbers = len(numbers)
    i = 0

    for i in range(lenNumbers-1):
        lowValue = numbers[i]
        lowValuePosition = i
        j = i + 1
        for j in range(j, lenNumbers):
            if (numbers[j] < lowValue):
                lowValue = numbers[j]
                lowValuePosition = j
        numbers[lowValuePosition] = numbers[i]
        numbers[i] = lowValue
        print(numbers)

selectionSort([7, 3, 5, 15, 2, 8, 4, 6, 9])
