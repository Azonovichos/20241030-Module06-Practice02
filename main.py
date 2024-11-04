# Module 6 Practice 2

class Vehicle:
    owner = True
    __model = True
    __engine_power = True
    __color = True
    __COLOR_VARIANTS = ['genuine green', 'brown', 'asphalt', 'bronze', 'aquamarine', 'black']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Vehicle Model: {self.__model}'

    def get_horsepower(self):
        return f'Vehicle Power: {self.__engine_power}'

    def get_color(self):
        return f'Vehicle Color: {self.__color}'

    def get_owner(self):
        return f'Vehicle owner: {self.owner}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(self.get_owner())

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
            print(f'Vehicle colored new color: {new_color}')
        else:
            print(f'Vehicle color can`t be change on: {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
print('\nИзначальные свойства')
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
print('\nМеняем свойства (в т.ч. вызывая методы)')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.set_color('Aquamarine')
vehicle1.set_color('genuine green')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print('\nПроверяем что поменялось')
vehicle1.print_info()

# Пробуем поменять модель ТС
print('\nПробуем поменять модель ТС')
print('У нас есть новенькая 21-я Волга Семёна Семёныча:')
vehicle2 = Sedan('Semyon Senyonych', 'GAZ 21 "Volga"', 'aquamarine', 80)
vehicle2.print_info()
print(f'\nМы загоняем {vehicle2.get_model()} в гараж, чтоб умельцы её переделали')
vehicle2.__model = 'Subaru Impreza WRX STI'
vehicle2.__engine_power = 265
vehicle2.set_color('Blue')
vehicle2.owner = 'Peter Forsberg'
print('И так, Peter Forsberg получает автомобиль, барабанная дробь:')
vehicle2.print_info()