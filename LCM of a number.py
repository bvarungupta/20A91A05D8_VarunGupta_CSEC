'''a=int(input("enter number:"))
b=int(input("enter number:"))
i=a
while a!=0 and b!=0:
    if(i%a==0 and i%b==0):
        print(f"lcm of {a} and {b} is {i}")
        break
    i+=1'''


a=int(input("enter first number: "))  #2 #a should always be bigger than b
b=int(input("enter second number: ")) #3
c=b #3
while True: #if we need common multiples c+=1 should be in next line
    if c%a==0 and c%b==0: #2%3==0 false...4,5,6-LCM
        print('LCM of ',a,' and ',b,' is ',c)
        break #if continue is given it goes into infinite loop as incrementing is not happening
    c+=1
     


#OUTPUT
'''
enter first number: 10
enter second number: 3
LCM of  10  and  3  is  30

enter first number: 3
enter second number: 10
LCM of  3  and  10  is  30
'''
          
       
