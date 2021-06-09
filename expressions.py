#Expression 1
a=int(input('enter integer value: '))
b=int(input('enter integer value: '))
c=float(input('enter float value: '))
d=int(input('enter long value: '))
result=a+b#expression - what the data type of result?
print('expression 1 result is ',result)
print('type of result is',type(result))


#expression 2 with int variables and long variables

result2=a+b+d
print('type of expression 2 is',type(result2))
print('expression 2 result is ',result2)

#expression 3 with int and float variables
result3=a+b+c
print('type of expression 3 is',type(result3))
print('expression 2 result is ',result3)

#OUTPUT
'''
enter integer value: 12
enter integer value: 35
enter float value: 36.89
enter long value: 250
expression 1 result is  47
type of result is <class 'int'>

type of expression 2 is <class 'int'>
expression 2 result is  297

type of expression 3 is <class 'float'>
expression 2 result is  83.89
'''

#Type promotions in expressions
