class Dog:
  def __init__(self, name, breed, age, color):
    self.name = name
    self.breed = breed
    self.age = age
    self.color = color


  def get_name(self):
    return self.name


  def get_breed(self):
    return self.breed


  def get_age(self):
    return self.age


  def get_color(self):
    return self.color


  def message(self):
    return (f"Hi my name is {self.get_name()}.\n"
            f"My breed, age and color are {self.get_breed()}, {self.get_age()}, {self.get_color()}")


tuffy = Dog("Tuffy", "Papillon", 5, "white")
max = Dog("Max", "Great Dane", 7, "black")


print(tuffy.message())
print(max.message())