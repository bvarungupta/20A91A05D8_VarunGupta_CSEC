#Nested for loop inside another for loop

#OUTER LOOP
for i in range(4): #iterations are from 0 to 3
    #INNER LOOP
    for j in range(2):#iterations are from 0 to 1 based on i value
        print('i value is',i,' and j value is',j)




#OUTPUT
'''
i value is 0  and j value is 0
i value is 0  and j value is 1
i value is 1  and j value is 0
i value is 1  and j value is 1
i value is 2  and j value is 0
i value is 2  and j value is 1
i value is 3  and j value is 0
i value is 3  and j value is 1
'''



#STEP BY STEP ITERATIONS
'''i-0
   j=0
     print 0,0

        at step 2, the control goes to J loop
        j is inctermented
        1<2 true
        print 0,1
        2<2 false
        
        control goes to I loop which is to the outer loop

and i=1
     j=0

     and so on.............

'''     
