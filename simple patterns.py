#PATTERNS

'''1.rows
2.columns

solution:
1.use nested for loop
2.rows condition will be in outerloop
3.colums condtion will be in innerlooop
4.print output
5.after inner loop completion print blank line'''


rows=int(input('enter number of rows: '))
cols=int(input('enter number of columns: '))
for i in range(rows):         #rows specified
    for j in range(cols):     #columns specified
        print('*',end='')
    print('\n') #required for pattern



'''
enter number of rows: 7
enter number of columns: 6

******

******

******

******

******

******

******
