#count() - returns the number of times a specified value occurs in a string
s=" I am  a CSE student.I am learning python.It is very easy"
#SYNTAX
#mainsentenceobject.count(searchstring)
#s.count(sesrchstring)
res_count=s.count('s')
print('count()')
print(res_count)

'''
#syntax2
searchsrtring='python'
res_count1=s.count(searchstring)
print('count()')
print('%s is repeated %d times' %(searchstring,res_count1))'''


#search from a particular index
m='helooo how are you'
c=m.count('o',4)
print('count() - searches the string from the goven index')
print(c)

#count('search string',start,end)
n=m.count('o',4,9)#it searches upto 8 
print( 'count() - searches the string from index 4 to (9-1)')
print(n)

