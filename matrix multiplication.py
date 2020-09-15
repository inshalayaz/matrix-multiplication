def creat_matrix(no_rows,no_cols):
    Matrix = []
    for i in range(1,int(no_rows)+1):
        row = []
        print('Row ' + str(i))
        for j in range(1,int(no_cols)+1):
            value = int(input("Enter Value {}:  ".format(j) )) 
            row.append(value)
        Matrix.append(row)
    return Matrix

rows_A = input("Enter no. of rows for Matrix A: ")
row_col_A_B = input("Enter column of matrix A and row of matrix B: ")
col_B = input('Enter column of matrix B: ')
print('Enter Matrix A: ')
matrix_A = creat_matrix(rows_A,row_col_A_B)
print("Enter Matrix B: ")
matrix_B = creat_matrix(row_col_A_B,col_B)
#print(matrix_A,matrix_B)
#print(type(rows_A))
#print(matrix_A)
# Multiplication Part
ans = []
for i in range(0,int(rows_A)):
    result = []
    for j in range(0,int(col_B)):
        sum = 0
        for k in range(0,int(row_col_A_B)):
            #print("{} {}".format(matrix_A[i][k],matrix_B[k][j]))
            product = matrix_A[i][k]*matrix_B[k][j]
            sum +=product
        result.append(sum)
    ans.append(result)
print(ans)
           
