# Q1. 다음은 Calculator 클래스이다
# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val

#     위 클래스를 상속하는 UpgradeCalculator를 만들고
#     값을 뺄 수 있는 minus 메소드를 추가하시오

#     cal = UpgradeCalculator()
#     cal.add(10)
#     cal.minus(7)

#     print(cal.value) # 10에서 7을 뺀 3 출력

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
        
        
class UpgradeCalculator(Calculator):
    def minus(self, val) :
       self.value -= val
    
    
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)