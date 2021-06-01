n=int(input('enter the number: '))
i=1
iterations = 0
while(i<=n//2):
    iterations=iterations+1
    if(n%i==0):
        print(i,end=' ')
        
    i=i+1
print(n)
print('total iterations are ',iterations)

#output
#enter the number: 8
#1
#2
#4
#8
#total iterations are 8


'''a=int(input('enter the number: '))
i=1
iterations = 0
while(a>=i):
    iterations=iterations+1
    if(a%i==0):
        print(i,end=' ')
        
    i=i+1   
print('\n')
print('total iterations are ',iterations)

#output
#enter the number: 8
#1 2 4 8 
#total iterations are  8
'''
