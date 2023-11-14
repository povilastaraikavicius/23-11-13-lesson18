class Family:
    def __init__(
        self,
        sister_name: str,
        brother_name: str,
        mother_name: str,
        father_name: str,
        sister_age: int,
        brother_age: int,
        mother_age: int,
        father_age: int,
    ) -> None:
        self.sister_name = sister_name
        self.brother_name = brother_name
        self.mother_name = mother_name
        self.father_name = father_name
        self.sister_age = sister_age
        self.brother_age = brother_age
        self.mother_age = mother_age
        self.father_age = father_age

    def family_data(self) -> dict:
        family_dictionary: dict = {
            self.sister_name: self.sister_age,
            self.brother_name: self.brother_age,
            self.mother_name: self.mother_age,
            self.father_name: self.father_age,
        }
        return family_dictionary

    def age_sum(self) -> int:
        return self.sister_age + self.brother_age + self.mother_age + self.father_age

    def return_sister_name(self) -> str:
        return self.sister_name

    def return_brother_name(self) -> str:
        return self.brother_name

    def return_mother_name(self) -> str:
        return self.mother_name

    def return_father_name(self) -> str:
        return self.father_name

    def sorted_by_age_family_list(self) -> list:
        family_dict: dict = self.family_data()
        return sorted(family_dict)


family_info = Family(
    sister_name="Evelina",
    brother_name="Andrius",
    mother_name="Irena",
    father_name="Juozas",
    sister_age=31,
    brother_age=12,
    mother_age=55,
    father_age=54,
)

print(family_info.family_data())
print(family_info.age_sum())
print(family_info.return_sister_name())
print(family_info.return_brother_name())
print(family_info.return_mother_name())
print(family_info.return_father_name())
print(family_info.sorted_by_age_family_list())