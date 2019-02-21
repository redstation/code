def bubble_Sort(numberslist):
    for numbers in range(len(numberslist)-1,0,-1):
        for x in range(numbers):
            if numberslist[x] > numberslist[x+1]:
                implementation = numberslist[x]
                numberslist[x] = numberslist[x+1]
                numberslist[x+1] = implementation


numberslist = [ 30, 1, 35, 11, 13, 23, 41, 34, 24, 9, 77, 7, 99]
bubble_Sort(numberslist)
print(numberslist)
