#program where loop is initiated at 5
'''i=5
while i<100 :
    print(i,end=' ')
    i+=10
else:
    print('\n')
    print('program executed')

 
output
5 15 25 35 45 55 65 75 85 89
program executed '''

i=1
while(i<=100):
   if(i%10==5):
       print(i,end=' ')
   i+=1     
else:
    print('\n')
    print('program is terminated')
    

'''output::::
5 15 25 35 45 55 65 75 85 95 
program is terminated'''



