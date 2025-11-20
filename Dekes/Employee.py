#Пример 1

# class Person:
#     def __init__(self, name):
#         self.__name = name
#     def getname(self):
#         return self.__name
#     def display_info(self):
#         print(f"Name, {self.getname()}")
# class Employee(Person):
#     def __init__(self, name, time):
#         super().__init__(name)
#         self.__time = time
#     def work(self):
#         print(f"{self.__name} works {self.__time} hours")
# class Employee:
#     def work(self):
#         print("Employee works")
#
# class Student:
#     def study(self):
#         print("Student studies")
# class WorkingStudent(Employee, Student):
#     pass
#
# def main():
#     tom = WorkingStudent()
#     tom.work()
#     tom.study()
# # Пример 1
# #     tom = Employee("Tom", 10)
# #     tom.work()
# #     tom.getname()
# #     tom.display_info()
# if __name__ == "__main__":
#     main()


class NPC:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def str(self) -> str:
        return f"{self.name} (HP: {self.hp})"

    def attack(self) -> int:
        """Базовая атака NPC — по умолчанию 0."""
        return 0


class Swordsman(NPC):
    def __init__(self, name: str, hp: int, min_damage: int, max_damage: int):
        super().__init__(name, hp)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self) -> int:
        import random
        return random.randint(self.min_damage, self.max_damage)


class Mage(NPC):
    def __init__(self, name: str, hp: int, mana: int):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self) -> int:
        """Атака мага — зависит от уровня маны."""
        if self.mana <= 0:
            return 0
        self.mana -= 10  # условно маг тратит 10 маны
        return 25        # фиксированный урон, можно менять

