# -----------------------------------------------------------------------------------------------
# 연산자(operator) => 산술(+,-,* ..), 비교(>,< ..), 논리(:), 멤버(in), 대입(=)
# 객체의 연산
# - list + list                                     \ list * 정수 
# - tuple + tuple => 각각은 안바뀌고 더한게 새로 생김  \ tuple * 정수
# - str + str                                        \ str * 정수
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# 평면에 점을 나타내는 데이터 타입의 클래스
# - 좌표 (x, y) => 속성
# - 점 찍기 => 메서드
# -----------------------------------------------------------------------------------------------
class Point:
    # 인스턴스 속성
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 인스턴스 메서드
    def drawPoint(self):
        print(f'({self.x}, {self.y}) 점 찍기')
    # 덧셈 연산시 자동 호출되는 콜백 메서드
    def __add__(self,other): return self.x + other.x , self.y + other.y # return 뒤에 괄호 치든 안치든 똑같이 나옴
    # 뺄셈 연산시 ..
    def __sub__(self,other): return self.x - other.x , self.y - other.y
# 객체 생성
white1=Point(7,7)
black1=Point(8,8)

# 메서드 호출
white1.drawPoint()
black1.drawPoint()

# Point인스턴스 (=객체) 덧셈하기
result=white1+black1
print(f'result : ',result)
result=white1-black1
print(f'result : ',result)

