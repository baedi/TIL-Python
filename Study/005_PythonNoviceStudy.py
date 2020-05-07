#coding utf-8

### List - append( )
# 리스트에 자료 추가하는 함수
print('List - append( )')
list1 = [10, 30.0, 'Fifteen']
print('before : ' + str(list1))
list1.append(True)
list1.append('Hello')
print('after : ' + str(list1) + '\n')


### List - extend( )
# 리스트에 여러 자료 추가하는 함수
print('List - extend( )')
list2 = [100, True, False]
print('before : ' + str(list2))
list2.extend(['Plus', 'Minus', 1234])
print('after : ' + str(list2) + '\n')


### List - del, pop
# 리스트의 특정 값을 지우기 or POP (맨 뒤에 있는 자료 꺼내기)
list3 = [10, 20, 30, 40, 50]
print('before : ' + str(list3))
list3.pop() # 리스트에 있는 맨 뒤의 값이 50이라면 50을 반환하지 않을까?
list3.pop()
print('after1 : ' + str(list3))

del list3[1]
print('after2 : ' + str(list3))


### List - reverse, sort
# 리스트 정렬
list4 = [37, 58, 5, 1, 3.14, 'Play', 'Hand', 'arm', True, False]
list4.reverse()     # 해당 리스트를 역순으로
print('list4 reverse : ' + str(list4))

## Compile error! (not supported between instances of 'str' and 'bool'
# sort( ) 정렬 함수 사용할 경우 해당 리스트에 문자열이나 부울식이 포함된 것은 정렬 불가
# list4.sort()
# print('list4 sort : ' + str(list4))

# 크기 순으로 리스트 정렬하기 (reverse를 이용하면 역순 정렬 가능)
list5 = [12, 55, 3.6, 1.7, 0, -12, 356]
list5.sort()
print('list5 sort : ' + str(list5))
list5.sort(reverse = True)
print('list5 sort(reverse) : ' + str(list5))
