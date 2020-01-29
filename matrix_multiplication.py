def matrix_multiplication():
    print('Enter number of rows of matrices:')
    m=int(input())
    print('Enter number of columns of matrices')
    n=int(input())
    matrix1=[[0,0],[0,0]]
    matrix2=[[0,0],[0,0]]
    res=[[0,0],[0,0]]
    if m==n:
        print('Enter the first array elements')
        for i in range (0,m):
            for j in range (0,n):
                print ('entry in row: ',i+1,' column: ',j+1)
                matrix1[i][j] = int(input())

        print('Enter the second array elements')
        for i in range (0,m):
            for j in range (0,n):
                print ('entry in row: ',i+1,' column: ',j+1)
                matrix2[i][j] = int(input())        

        print('The product of the two matrices : ')
        for i in range (0,m):
            for j in range (0,n):
                for k in range (0,n):
                    res[i][j] += matrix1[i][k]*matrix2[k][j]
    else:
        print('Number of rows and columns must be equal')

    print(res)

matrix_multiplication()
