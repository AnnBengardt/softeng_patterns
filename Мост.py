
# Сущность сотрудника - он может быть пм или тимлодом, который в свою очередь может быть сеньор разрабом или миддлом
class Employee:
    def be_senior(self, items):
        pass

    def be_middle(self, items):
        pass

# в нашем случае класс пм и тимлида выступают дочерними классами Сотрудника
class ProjectManager(Employee):
    def be_senior(self, projects):
        print("This developer is senior and manages projects: ", projects, "\n")

    def be_middle(self, projects):
        print("This developer is middle and manages projects: ", projects, "\n")

class TeamLead(Employee):
    def be_senior(self, teams):
        print("This developer is senior and leads teams: ", teams, "\n")

    def be_middle(self, teams):
        print("This developer is middle and leads teams: ", teams, "\n")

# Класс разработчика, в ините подаётся объект класса Сотрудник - это и есть главный момент Моста
# Связываем 2 родительских абстракции, чтобы потом комбинировать вместе конкретные дочерние классы
# Также когда подклассов гораздо больше и они все могут быть скомибинрованы - без моста пришлось бы писать декартово произведение классов-комбинаций
# Т. е. в этом случае пришлось бы делать отдельные классы SeniorProjectManager, MiddleProjectManager и т.д.
class Developer:
    def __init__(self, employee):
        self.employee = employee

    def display_description(self):
        pass

    def add_objects(self, new_objects):
        pass

# Senior Developer
class Senior(Developer):
    def __init__(self, employee, objects):
        super().__init__(employee)
        self.objects = objects

    def display_description(self):
        self.employee.be_senior(self.objects)

    def add_objects(self, new_objects):
        self.objects.append(new_objects)

# Middle Developer
class Middle(Developer):
    def __init__(self, employee, objects):
        super().__init__(employee)
        self.objects = objects

    def display_description(self):
        self.employee.be_middle(self.objects)

    def add_objects(self, new_objects):
        self.objects.append(new_objects)


if __name__ == "__main__":

    pm = ProjectManager()
    tl = TeamLead()

    # Мост между сеньором и пм
    senior1 = Senior(pm, ["Project X", "Project Y"])
    senior1.display_description()
    senior1.add_objects("Project A")
    senior1.display_description()

    # Мост между сеньором и тимлидом
    senior2 = Senior(tl, ["Team X", "Team Y"])
    senior2.display_description()
    senior2.add_objects("Team A")
    senior2.display_description()

    # Мост между миддлом и тимлидом
    middle = Middle(tl, ["Team X", "Team Y"])
    middle.display_description()
    middle.add_objects("Team A")
    middle.display_description()

    # и так далее: получаем декартово произведение всех параметров
    # в данном случае комбинаций всего 4, истинное удобство этого паттерна видно на большем числе комбинируемых классов
