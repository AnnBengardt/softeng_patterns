class Database:
  """
  базовый класс базы данных
  """

  def __init__(self, name: str, admin: str, columns: list):
    self.name = name
    self.admin = admin
    self.columns = columns
    self.rows = []

  def load_data(self, data: list):
    for row in data:
        adding = {}
        for i, item in enumerate(row):
            adding[self.columns[i]] = item
        self.rows.append(adding)
    print("Data loaded successfully to: ", self.name)


class SystemDatabaseDecorator:
  """
  класс декоратор - системная база данных
  получает на вход базу данных, сохраняет все её атрибуты и методы, чтобы их можно было вызывать через декоратор напрямую, без обращения к self.model
  если атрибута/метода нет ни у декоратора, ни у базового класса - вызывает AttributeError
  данный декоратор динамически добавляет функционал создания бэкапа для админов баз данных
  """
  def __init__(self, model):
    self.model = model
    self.model_attributes = [attribute for attribute in self.model.__dict__.keys()]
    self.model_methods = [m for m in dir(self.model) if not m.startswith('_') and m not in self.model_attributes]

  def __getattr__(self, func):
    if func in self.model_methods:
      def method(*args):
        return getattr(self.model, func)(*args)
      return method
    elif func in self.model_attributes:
      return getattr(self.model, func)
    else:
      raise AttributeError

  def create_backup(self, filename, username):
    if username == self.admin:
      with open(filename, "w") as file:
          file.write(";".join(self.columns)+"\n")
          for row in self.rows:
              file.write(";".join(row)+"\n")
      print("Backup of a system database created")
    else:
      print("Creating backup of the system database not permitted for the user ", username)


class PersonalDatabaseDecorator:
  """
  класс декоратор - личная база данных
  получает на вход базу данных, сохраняет все её атрибуты и методы, чтобы их можно было вызывать через декоратор напрямую, без обращения к self.model
  если атрибута/метода нет ни у декоратора, ни у базового класса - вызывает AttributeError
  данный декоратор динамически добавляет функционал создания бэкапа и полного удаления данных для всех пользователей
  """
  def __init__(self, model):
    self.model = model
    self.model_attributes = [attribute for attribute in self.model.__dict__.keys()]
    self.model_methods = [m for m in dir(self.model) if not m.startswith('_') and m not in self.model_attributes]

  def __getattr__(self, func):
    if func in self.model_methods:
      def method(*args):
        return getattr(self.model, func)(*args)
      return method
    elif func in self.model_attributes:
      return getattr(self.model, func)
    else:
      raise AttributeError

  def create_backup(self, filename):
    with open(filename, "w") as file:
        file.write(";".join(self.columns)+"\n")
        for row in self.rows:
            file.write(";".join(row.values())+"\n")
    print("Backup of a personal database created")

  def delete_data(self):
    self.rows = []
    print("Data succesfully deleted")


if __name__ == "__main__":
    db = Database("main", "admin", ["first name", "last name"])

    sys_db = SystemDatabaseDecorator(db)
    sys_db.load_data([["Ivan", "Ivanov"], ["John", "Smith"], ["Kate", "Muller"]])
    sys_db.create_backup("backup.txt", "user1")
    try:
      sys_db.delete_data()
    except AttributeError:
      print("System Database doesn't have method 'delete_data'")

    db = Database("personal db", "admin", ["first name", "last name"])
    my_db = PersonalDatabaseDecorator(db)
    my_db.load_data([["Ivan", "Ivanov"], ["John", "Smith"], ["Kate", "Muller"]])
    my_db.create_backup("backup.txt")
    my_db.delete_data()