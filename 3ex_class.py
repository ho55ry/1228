# ------------------------------------------------------------------------------------------------
# 객체지향언어 => 정보은닉(캡슐화)
# - 속성/필드 => 비공개(private)
# - 메서드 => 비공개 => 공개가능한 것만 공개(public)
# -----------------------------------------------------------------------------------------------
# BMI 지수 => 키, 몸무게 이용해서 계산
# -----------------------------------------------------------------------------------------------
class A:
    # 속성 2개 가지는 클래스
    def __init__(self,height,weight):
        self.__height=height
        self.__weight=weight
        self.bmi=weight*10000/(height*height)

    # 비공개 속성 제어 메서드 get/set
    def get__height(self): return self.__height
    def get__weight(self): return self.__weight
    def set__height(self,height): self.__height=height
    def set__weight(self,weight): self.__weight=weight

    # 몸무게 증감 메서드
    def diet(self,value): self.__weight=self.__weight+value

    # 키 증감 메서드
    def grow(self,value): self.__height=self.__height+value


# 인스턴스 생성
bsk=A(205,100)

# 인스턴스 속성 확인
print(f'bsk.bmi : ',bsk.bmi)    
print(bsk.__dict__)

