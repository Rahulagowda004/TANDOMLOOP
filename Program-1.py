#Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
class calculator:
    def __init__(self):
        self.a = float(input("enter the first number: "))
        self.b = float(input("enter the second number"))
        self.operation = (str(input("enter the arithematic operation: "))).lower()
        
    def add(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "the number should be greater than zero in order to divide"

if __name__ == "__main__":
    try:
        object = calculator()
        if object.operation == "addition" or object.operation == "add":
            print(object.add())
        elif object.operation == "subtraction" or object.operation == "sub":
            print(object.subtraction())
        elif object.operation == "multiplication" or object.operation == "mul":
            print(object.multiplication())
        elif object.operation == "division" or object.operation == "div":
            print(object.division())
        else:
            print("Please enter a valid operation to use the calculator")
    except Exception as e:
        print(f"error is {e}")
