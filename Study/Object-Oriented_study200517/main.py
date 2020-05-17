from absClass import *

ref_ = GamePlay()   # 인스턴스 생성
ref_.info()
ref_.play(3)
ref_.loop()

# ref_가 NOT NULL인지 확인
if ref_ is not None :
    print('ref_ is not NULL!')
    ref_ = None

print('\n')

ref_ = MainMenu()   # 다른 클래스로 인스턴스 생성
ref_.info()
ref_.play(5)
ref_.loop()
