#coding utf-8

# 비트 연산자 테스트
print('bit test1')
a = 0b100       # Var
a = a | 0b110   # 100 | 110 = 110
print(a)
print(bin(a))
print()

print('bit test2')
b = 1           # Var
b = ~b          # 0001 -> 1 1110 ?
print(bin(b))
print(bin(b & 0xFF))
print(b & 0xFF)
print()

# 시프트 연산
print('bit shift')
c = 8       # 0000 1000
c1 = c << 2 # 0010 0000
c2 = c >> 1 # 0000 0100
print(c1)
print(c2)

# 문자열과 인덱스 다뤄보기
print('string test')
str_ = 'Hello world \'Python!\''
print(str_)         # 모든 문자열 출력
print(str_[1])      # 인덱스 1에 속한 문자 출력
print(str_[:5])     # 인덱스 0 ~ 5 까지의 문자 출력
print(str_[6:11])   # 인덱스 6 ~ 11 까지의 문자 출력
print(str_[12:])    # 인덱스 12 ~ 끝부분까지 문자 출력
