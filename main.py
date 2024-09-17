class House:

    def __init__(self, name, limit_floor):
        self.name = name
        self.limit_floor = limit_floor

    def __del__(self):
        print(f'{self.name} is exit')

    def __len__(self):
        return self.limit_floor

    def __str__(self):
        return f'name is: {self.name}, number of foolrs: {self.limit_floor}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1) # при появлении метода __str__ в консоль выводятся все параметры атрибута. без метода __str__ в консоль выводится ссылка на выделенное место в памяти устройства ????

print(h1.__len__()) # вызываем метод len атрибута h1 класса home
print(h2.__len__())
print()

print(h1.__str__()) # вызываем метод str
print(h2.__str__())
print()
