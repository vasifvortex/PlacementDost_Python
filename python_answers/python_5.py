class Calculator:
    def addition(self, x, y):
        return x + y
    def subtraction(self, x, y):
        return x - y
    def multiplication(self, x, y):
        return x * y
    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
calculator = Calculator()
result = calculator.addition(7, 5)
print("7 + 5 =", result)
