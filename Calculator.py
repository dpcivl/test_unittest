class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    # 제곱 기능 추가
    def power(self, a, b):
        return a ** b
    
    # 제곱근 기능 추가
    def sqrt(self, a):
        if a < 0:
            raise ValueError("음수를 입력 받았다.")
        
        return a ** 0.5