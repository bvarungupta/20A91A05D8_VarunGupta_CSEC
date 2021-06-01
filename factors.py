a=int(input('enter the number: '))
i=1
while(a>=i):
    if(a%i==0):
        print(i,end=',')
    i=i+1

    
    '''output
    enter the number 10
    1,2,5,10
    '''
