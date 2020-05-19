### Library (라이브러리)
import random

### Var (전역변수)
counter = [1, 2, 3]
counter2 = [(0, 0, 0), (12, 25, 134), (255, 255, 0)]


# for i in [LIST] :: for문을 이용하여 리스트의 값을 하나씩 가져오기
print('[for test1]')
for temp in counter : print('%d' % (temp))
print('\n')


# for (i1, i2, i3) in [LIST] :: for문을 이용하여 리스트 세트값을 하나씩 가져오기
print('[for test2]')
for (v1, v2, v3) in counter2 : print('%d %d %d' % (v1, v2, v3))
print('\n')


# for i in range(arg1)
print('[for test3]')
for count in range(5) : print('index : %d' % (count))
print('\n')


# for i in range(arg1, arg2)
print('[for test4]')
for count in range(3, 15) : print('index : %d' % (count))
print('\n')


# random.randint :: 시작값 ~ 종료값 중에서 난수를 발생시킴
print('[random test1]')
avrScore = 0    # 평균을 구하기 위한 변수
times = 100     # 반복횟수

for count in range(times) :
    temp = random.randint(0, 100)  # 0 ~ 100
    avrScore = avrScore + temp

print('result : %.2f\n' % (avrScore / 100.0))


# random.shuffle :: 리스트에 있는 목록들의 순서를 섞음
print('[random test2]')
student = ['SangHo', 'DongHwa', 'TaeYun', 'Kawashi', 'Johnson', 'Alabia']
random.shuffle(student)

for count in range(len(student)) :
    print('index %d : %s' % (count, student[count]))
print('\n')


# random.choice :: 리스트에 있는 목록들 중 무작위 선택
print('[random test3]')
junk = [True, 123, 'Hwai', 0.123, False, 'DDANG']

for count in range(10):
    print(random.choice(junk))
