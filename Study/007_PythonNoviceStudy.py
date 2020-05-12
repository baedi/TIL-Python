#coding utf-8

### % test
integer = 1234
string_ = 'Hello world'
float_ = 50.25

print('number %d %s, %f' % (integer, string_, float_))

string_ = 'Ahahaha! %d is stupid' % (integer)
print(string_ + '\n')


### input() test
string_ = input('Name : ')
print(string_ + '\n')



### if, elif, else
input_value = input('number input : ')

if int(input_value) == 100 :
    print('A++')
    
elif int(input_value) > 70 :
    print('B')
    
else :
    print('F')
    
    
### while( ) test
temp = 10

while temp > 0 :
    print('count : ' + str(temp))
    temp = temp - 1
    

print('while is exit...')

    
