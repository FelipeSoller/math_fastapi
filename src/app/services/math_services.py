class NumbersService:
    def __init__(self):
        self.number = Number()

    def sum(self, numbers: list[int]) -> int:
        result = 0

        for number in numbers:
            result = self.number.sum(result, number)

        return result

    def average(self, numbers: list[int]) -> float:
        quantity = len(numbers)

        if quantity == 0:
            raise ValueError("A lista de números não pode estar vazia")
        return self.number.divide(self.sum(numbers), quantity)

class Number:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b