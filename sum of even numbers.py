#sum of even numbers
n=int(input('enter starting number: '))
e=int(input('enter ending number: '))
sum1=0
for n in range(n, e+1):
   if(n%2==0):
     sum1=sum1+n
     print('number is',n,'and sum is',sum1)

print('\nsum is',sum1)
print('\nprogram executed')




#output

'''
==== RESTART: C:/Users/VARUN/Desktop/python programs/sum of even numbers.py ====
enter starting number: 1
enter ending number: 10
number is 2 and sum is 2
number is 4 and sum is 6
number is 6 and sum is 12
number is 8 and sum is 20
number is 10 and sum is 30

sum is 30

program executed
'''
