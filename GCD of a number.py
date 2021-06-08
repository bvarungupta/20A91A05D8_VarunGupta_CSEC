#Greatest Common Divisor

a=int(input("enter first number: "))#5    #10
b=int(input("enter second number: "))#10  #5
if a>b: #10>5
    a,b=b,a #5 10 #when a is smaller than bigger it is swapped
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        print('GCD of',a,'and',b,'is',i)
        break



#OUTPUT
'''    
enter first number: 5
enter second number: 10
GCD of  5 and 10 is 5

enter first number: 10
enter second number: 5
GCD of 5 and 10 is 5
'''
