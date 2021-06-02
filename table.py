#table using for loop and customizing
'''n=int(input('enter number: '))
s=int(input('enter start point: '))
e=int(input('enter end point: '))
for i in range(s,e+1):#e+1 so that the last number in range is not excluded
 print(n,'*',i,'=',n*i)#* and = are in quotes because we ned the to be printed.
'''


'''output
enter number: 22
enter start point: 7
enter end point: 14
22 * 7 = 154
22 * 8 = 176
22 * 9 = 198
22 * 10 = 220
22 * 11 = 242
22 * 12 = 264
22 * 13 = 286
22 * 14 = 308'''

#using while loop

'''n=int(input('enter number: '))
s=int(input('enter start point: '))
e=int(input('enter end point: '))
while i<=e:
    i+=1
    print(n,'*',i,'=',n*i)'''

#when starting point is smaller than ending point e>s
'''n=int(input('enter number: '))
s=int(input('enter start point: '))
e=int(input('enter end point: '))
 
for i in range(e,s-1,-1):
               print(n,'*',i,'=',n*i)'''


#when starting point is smaller than ending point e>s
'''output
enter number: 5
enter start point: 2
enter end point: 10
5 * 10 = 50
5 * 9 = 45
5 * 8 = 40
5 * 7 = 35
5 * 6 = 30
5 * 5 = 25
5 * 4 = 20
5 * 3 = 15
5 * 2 = 10
'''


#custom input when ending is bigger than ending ///
#ending is bigger then starting
n=int(input('enter number: '))#5
s=int(input('enter start point: '))#3#6
e=int(input('enter end point: '))#6#3

if s<e:#3<6//#6<3--false 
    for i in range(s,e+1):#(3,4,5,6)
        print(n,'*',i,'=',n*i)
else:
    for i in range(s,e-1,-1):#(6,5,4,3)
      print(n,'*',i,'=',n*i)

#output
#when ending > starting      
'''enter number: 5
enter start point: 4
enter end point: 10
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50'''
#when ending < starting
'''enter number: 5
enter start point: 10
enter end point: 4
5 * 10 = 50
5 * 9 = 45
5 * 8 = 40
5 * 7 = 35
5 * 6 = 30
5 * 5 = 25
5 * 4 = 20'''
