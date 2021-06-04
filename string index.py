#for with string
'''name=input('enter name: ')#if taken python
print(name)
#indexing
#0 to n-1
print(name[0])#p=0,y=1,t=2,h=3,o=4,n=5
size=len(name)#size of name as python has 6 letters
print('size of',name,'is',size)#6'''



#output
'''enter name: varun gupta
varun gupta
v
size of varun gupta is 11'''

#access string elements
name=input('enter name: ')
size=len(name)
print('size of',name,'is',size)
for i in name:
 print(i,end=' ')


#another way of accessing strings elements using index
for i in range(size): #length of string
    print('\n',name[i])#i=0,i=1,i=2.......i=size-1


'''output
enter name: varun
size of varun is 5
v a r u n 
 v

 a

 r

 u

 n
 '''
