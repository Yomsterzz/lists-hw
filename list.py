
for row in range(0,len(matrix)):
    for column in range(0,len(matrix[0])):
        print(matrix[row][column])

for row in range(0,len(matrix)):
    for column in range(0,len(matrix[0])):
        print(matrix[row][column],end=" ")
    print()

sizeofmatrix = int(input("How many rows will be in our square matrix? "))
matrix2 = []

for rows in range(sizeofmatrix):
    templist = []
    for column in range(sizeofmatrix):
        data = input("Enter a numerical data point: ")
        templist.append(data)
    matrix2.append(templist)

for row in range(len(matrix2)):
    for column in range(len(matrix2[0])):
        print(matrix2[row][column],end=" ")
    print()
matrixA = [
    [42,314,64],
    [934,21,23],
    [9,936,834]
]
matrixB = [
    [24,413,46],
    [439,12,32],
    [90,639,438]
]
additionresult =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

