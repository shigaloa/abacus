class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        total = 0
        for item in self.operands:
            total += item
        print(total)

    def subtract(self):
        difference = 0
        for item in self.operands:
        difference -= item
        print(difference)

   def division(self):
        quotient = 1
        for item in self.operands:
        quotient /= item
        print(quotient)

    def multiply(self):
        sum = 1
        for item in self.operands:
        sum *= item
        print(sum)
