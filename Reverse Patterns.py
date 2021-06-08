#REVERSE PATTERN

        
n=int(input('enter row value: '))
for i in range(n):
   for j in range(n,i,-1):
       print(j,end=" ")
   print()


'''OUTPUT
6 5 4 3 2 1 
6 5 4 3 2 
6 5 4 3 
6 5 4 
6 5 
6 
'''



#Pattern 1
n=int(input('enter number of rows: '))
for i in range(1,n+1):
    k=1
    for j in range(i):
        print(k,end=' ')
        k+=1
      
    print()


'''OUTPUT
enter number of rows: 7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7
'''



#pattern 2
k=int(input('enter number of rows: '))
for i in range(1,k+1):
      for j in range(1,i+1):
        print(j,end=' ')
      print()
    
for i in range(k-1,0,-1):
      for j in range(1,i+1):
         print(j,end=' ')
      print()

'''OUTPUT
enter number of rows: 7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
