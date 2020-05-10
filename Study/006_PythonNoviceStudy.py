#coding utf-8

### Tuple (Value, ...)          ... 소괄호로 된 것이 튜플.
### (you can't change values)   ... 튜플은 데이터 변경 불가능.
print('[Tuple Test]')
tup1 = ('abc', 'H', 123, True, 3.14)
print(tup1)
print()

## 튜플에 또 다른 튜플 정의 가능.
tup2 = (('index0', 3), 'index1', ('index2', False, 3.14), '3boy')
print(tup2[0])      #{'index0', 3}
print(tup2[0][0])   # index0
print(tup2[0][1])   # 3
print(tup2[1])      # index1
print(tup2[2][1])   # False
print()

tup3 = (0, 1, 2, 3, 4, 5, 6, 7)
print(tup3[:4])     # 0 ~ 3
print(tup3[2:5])    # 2 ~ 4
print(tup3[5:])     # 5 ~ 7

tup4_1 = ('Hello ', 'Hola ')
tup4_2 = ('My name is', 'I\'m fine')
print(tup4_1 + tup4_2)
print(tup4_1 * 2)
print()


### Dictionary { Key : Value, ...}  ... 중괄호로 된 것이 딕셔너리
print('[Dictionary Test]')
dict1 = {'no1' : 321, 'no2' : 999, 'no3' : 3.14}
print(dict1)            # {'no1': 321, 'no2': 999, 'no3': 3.14}
print(dict1['no3'])     # 3.14

dict1['no2'] = 888
print(dict1['no2'])     # 888

dict1['no4'] = 12345    # add dict.
print(dict1['no4'])

dict1.pop('no1')       # pop no1
del dict1['no3']       # del no3
print(dict1)

print()

## Parent ~ Child   .. 딕셔너리 안에 또 다른 딕셔너리 정의 가능.
dict2 = {0 : {0 : 'A', 1 : 'B'}, 1 : 'C', 2 : {0 : 'D', 1 : 'E', 2 : 'F'}}
print(dict2)
print(dict2[0][0])  # A
print(dict2[0][1])  # B
print(dict2[1])     # C
print(dict2[2][0])  # D
print()

### Change type.
print('[Change type test]')
val = 65
print(val)
print(chr(val))
print('Value : ' + str(val))
print(float(val))
print()


## Tuple <---> List     ... 튜플 <---> 리스트
val2 = (100, 200, 300, 400, 500)
print('Before : ' + str(val2))

## Compile error!
# val2[0] = 300
val2_temp = list(val2)
val2_temp[2] = 365
val2 = tuple(val2_temp)
print('After : ' + str(val2))

## 데이터를 특정 타입으로 변환시킴
print(isinstance(val2[0], int))
print(isinstance(val2[0], float))
print()
