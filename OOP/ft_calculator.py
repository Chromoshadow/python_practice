# class calculator:

#     def __init__(self, numbers):
#         self.numbers = list(numbers)

#     def get_numbers(self):
#         return self.numbers

#     def set_numbers(self, numbers):
#         self.numbers = numbers

#     def __repr__(self):
#         return f"{self.numbers}"

#     def __add__(self, object) -> None:
#         if isinstance(object, int):
#             self.numbers = [n + object for n in self.numbers]
#             print(self.numbers)

#     def __mul__(self, object) -> None:
#         if isinstance(object, int):
#             self.numbers = [n * object for n in self.numbers]
#             print(self.numbers)

#     def __sub__(self, object) -> None:
#         if isinstance(object, int):
#             self.numbers = [n - object for n in self.numbers]
#             print(self.numbers)

#     def __truediv__(self, object) -> None:
#         if isinstance(object, int) and object != 0:
#             self.numbers = [n / object for n in self.numbers]
#             print(self.numbers)

# --------------------------------------------------------------

class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(sum(x * y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print([x + y for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print([x - y for x, y in zip(V1, V2)])

