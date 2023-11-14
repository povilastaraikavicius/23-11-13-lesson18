# class Calculator:

#     def __init__(self) -> None:
#          print("Testas")

#     def add_two_numbers(self, number_a:int,number_b:int)->int:
#         return number_a + number_b

#     def divide_two_numbers(self, number_a:int,number_b:int)->int:
#         return number_a / number_b

#     def multiply_two_numbers(self, number_a:int,number_b:int)->int:
#         return number_a * number_b

#     def substract_two_numbers(self, number_a:int,number_b:int)->int:
#         return number_a - number_b


# calc = Calculator()

# print(calc.add_two_numbers(5,2))
# print(calc.divide_two_numbers(5,2))
# print(calc.multiply_two_numbers())
# print(calc.substract_two_numbers())

# class Car:
#     pass


# class People:
#     def __init__(self, name: str, surname: str) -> None:
#         self.n = name
#         self.surname = surname

#     def get_name_and_surname(self) -> str:
#         return self.n + " " + self.surname

# if __name__ == "__main__":

#     person = People(name="Saulius", surname="Anusas")

#     print(person.n)
#     print(person.get_name_and_surname())

# Create a class which represents your family. Class should take your mom,dad,sister ,broters names and ages.
# Create instance methods that would return :
#  - All names and ages as dict data structure
#  - The sum of all ages
#  - Would print the names depending on your relatives(sister,brother etc)
#  - Would list all family members from youngest to oldest (Choose return type by yourself.)


class Family:
    def __init__(
        self,
        mom_name: str,
        mom_age: int,
        dad_name: str,
        dad_age: int,
        sister_name: str,
        sister_age: int,
        brother_name: str,
        brother_age: int,
    ) -> None:
        self.mom_name = mom_name
        self.mom_age = mom_age
        self.dad_name = dad_name
        self.dad_age = dad_age
        self.sister_name = sister_name
        self.sister_age = sister_age
        self.brother_name = brother_name
        self.brother_age = brother_age

    def family_in_dict(self) -> dict:
        family_in_dict: dict = {
            self.mom_name: self.mom_age,
            self.dad_name: self.dad_age,
            self.sister_name: self.sister_age,
            self.brother_name: self.brother_age,
        }
        return family_in_dict

    def sum_of_ages(self) -> int:
        sum_of_ages = self.mom_age + self.dad_age + self.sister_age + self.brother_age
        return sum_of_ages

    def sorted_by_age_family_list(self) -> list:
        family_dict = self.family_in_dict()
        sorted_family = sorted(family_dict.items(), key=lambda x: x[1])
        return sorted_family


my_family = Family("Gendrika", 40, "Jonas", 45, "Viktorija", 20, "Andrius", 18)

print(my_family.family_in_dict())
print("Sum of Ages:", my_family.sum_of_ages())
print(
    my_family.mom_name + "\n",
    my_family.dad_name + "\n",
    my_family.sister_name + "\n",
    my_family.brother_name + "\n",
)
print(my_family.sorted_by_age_family_list())


# class Car:
#     def __init__(self, model: str, made_date: int, engine_capacity: float) -> None:
#       self.model = model
#       self.made_date = made_date
#       self.engine_capacity = engine_capacity

#     def ger_car_name(self)->str:
#      return self.model

# car = Car(model="mercedes", made_date = 1997, engine_capacity = 2.3)
# print (car.ger_car_name())
