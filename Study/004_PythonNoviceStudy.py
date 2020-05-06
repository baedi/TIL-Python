#coding utf-8

# string replace, length, find func test
strv = 'Hello Python!'
print(strv, end='')                             # 개행 문자 제가 방법
print(len(strv))

strv = strv.replace(strv, 'Ahahahaha!')
print(strv + '\tLEN : ' + str(len(strv)))       # 다른 요소들과 함께 출력하기
print()

strv2 = 'ABCDEFG123456'
print(strv2 + '\tLEN : ' + str(len(strv2)) + '\n')

strv2 = strv2.replace('DEF', 'face')            # 다른 문자열로 변경하기
print(strv2)
print(len(strv2))

# 특정 문자 찾기 혹은 특정 인덱스에서 특정 문자 찾기
print('Find index : ' + str(strv2.find('G')))
print('Find index : ' + str(strv.find('aha', 4, 9)))
print()

# List (배열)
idx = ['Hak eng', 12345, 3.14, True, 'L']
print(idx[0])
print(idx[1])
print(idx[2])
print(idx[3])
print(idx[4])
print()

# List - change (배열 - 일부 인덱스의 내용 수정 및 추가)
idx[1:3] = [6.321, False, 5] # index 1 ~ 2 (change), index 3(add)
print(idx[0])
print(idx[1])
print(idx[2])
print(idx[3])
print(idx[4])
print()

# List - copy (배열 - 얼마만큼 복사할 것인지 결정)
idx2 = ['Company', 5]
idx2 = idx2 * 2
print(idx2[2])
print(idx2[3])
print()

# List - combine (배열 - 다른 배열과 결합)
idx = idx + idx2
print(idx[0])
print(idx[1])
print(idx[2])
print(idx[3])
print(idx[4])
print(idx[5])
print(idx[6])
print(idx[7])
