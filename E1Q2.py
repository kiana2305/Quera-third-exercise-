class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def change_age(self, new_age):
        self.age = new_age

# ورودی ها
input_data = input().strip().split()
name = input_data[0]
age = int(input_data[1])

# ایجاد شیء از کلاس Person
person = Person(name, age)

# ورودی جدید برای سن
new_age = int(input().strip())

# تغییر سن
person.change_age(new_age)

# خروجی
print(f'name: {person.name}, age: {person.age}')