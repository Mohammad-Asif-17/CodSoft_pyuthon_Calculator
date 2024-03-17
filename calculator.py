class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def initialization(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def addition(self):
        result = self.num1 + self.num2
        print(f"Sum of {self.num1} and {self.num2} = {result}")

    def subtraction(self):
        result = self.num1 - self.num2
        print(f"Subtraction of {self.num1} and {self.num2} = {result}")

    def multiplication(self):
        result = self.num1 * self.num2
        print(f"Multiplication of {self.num1} and {self.num2} = {result}")

    def division(self):
        if self.num2 != 0:
            result = self.num1 / self.num2
            print(f"Division of {self.num1} and {self.num2} = {result}")
        else:
            print("Error! Division by 0 is not allowed")

    def Modulo_division(self):
        result = num1

def main():
    calculator = Calculator(None,None)

    while True:
        print("Choose an option:")
        print("1. To Addition")
        print("2. Sustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. To exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculator.initialization()
            calculator.addition()
        elif choice == '2':
            calculator.initialization()
            calculator.subtraction()
        elif choice == '3':
            calculator.initialization()
            calculator.multiplication()
        elif choice == '4':
            calculator.initialization()
            calculator.division()
        elif choice == '5':
            print("Exiting....")
            exit()
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()