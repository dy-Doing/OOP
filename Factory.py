def program():
    number_a = float(input('input number A:'))
    operate = input('input operator (+ - * /):')
    str_b = input('input number B:')
    number_b = float(str_b)
    result = 0

    try:

        if operate == '+':
            result = number_a + number_b

        if operate == '-':
            result = number_a - number_b

        if operate == '*':
            result = number_a * number_b

        if operate == '/':
            if str_b != '0':
                result = number_a / number_b
            else:
                result = '除数不能为0'

        print('result:{}'.format(result))
    except:
        print('wrong input')


program()

# ------------------VERSION V1.0-----------------------
class Operation:
    def __init__(self):
        self.__result = 0

    def GetResult(self, number_a, number_b, operate):
        if operate == '+':
            self.__result = number_a + number_b

        if operate == '-':
            self.__result = number_a - number_b

        if operate == '*':
            self.__result = number_a * number_b

        if operate == '/':
            self.__result = number_a / number_b

        return self.__result
def Main():
    try:
        number_a = float(input('input number A:'))
        operate = input('input operator (+ - * /):')
        str_b = input('input number B:')
        number_b = float(str_b)
        result = Operation().GetResult(number_a, number_b, operate)
        print('result:{}'.format(result))
    except Exception:
        print('wrong input')
Main()

# ------------------VERSION V2.0-----------------------
from abc import ABCMeta, abstractmethod
class Operation:
    def __init__(self):
        self.__number_a = 0
        self.__number_b = 0

    def GetNumberA(self):
        return self.__number_a

    def SetNumberA(self, number_a):
        self.__number_a = number_a

    def GetNumberB(self):
        return self.__number_b

    def SetNumberB(self, number_b):
        self.__number_b = number_b

    number_a = property(GetNumberA, SetNumberA)
    number_b = property(GetNumberB, SetNumberB)

    @abstractmethod
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def __init__(self):
        super().__init__()

    def GetResult(self):
        result = 0
        result = self.number_a + self.number_b
        return result

class OperationSub(Operation):
    def __init__(self):
        super().__init__()

    def GetResult(self):
        result = 0
        result = self.number_a - self.number_b
        return result

class OperationMul(Operation):
    def __init__(self):
        super().__init__()

    def GetResult(self):
        result = 0
        result = self.number_a * self.number_b
        return result

class OperationDiv(Operation):
    def __init__(self):
        super().__init__()

    def GetResult(self):
        result = 0
        if self.number_b == 0:
            raise ValueError("除数不能为0")
        result = self.number_a / self.number_b
        return result

class OperationFactory:
    def CreateOperate(self, operate):
        oper = 0
        if operate == '+':
            oper = OperationAdd()
        if operate == '-':
            oper = OperationSub()
        if operate == '*':
            oper = OperationMul()
        if operate == '/':
            oper = OperationDiv()
        return oper


oper = OperationFactory().CreateOperate('/')
oper.number_a = 2
oper.number_b = 0
result = oper.GetResult()
print(result)
