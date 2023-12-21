def insertionSort(numbers : list):
    print(numbers)
    print()

    lenNumbers = len(numbers)
    i = 0

    for i in range(lenNumbers-1):
        if (numbers[i] > numbers[i+1]):
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            print(numbers)
            j = i
            while(j > 0):
                if (numbers[j] < numbers[j-1]):
                    temp = numbers[j-1]
                    numbers[j-1] = numbers[j]
                    numbers[j] = temp
                print(numbers)
                j -= 1

insertionSort([22, 27, 16, 6, 18, 2])
