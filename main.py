    # 1
class Number:
    def __init__(self, x=0):
        self.x = x
    def __str__(self):
        return f'({self.x})'
    def __add__(self, other):
        x = self.x + other.x
        return x
    def __sub__(self, other):
        x = self.x - other.x
        return x
    def __mul__(self, other):
        x = self.x * other.x
        return x
    def __truediv__(self, other):
        x = self.x / other.x
        return x
x1 = Number(1)
x2 = Number(2)
print(f'x1 = {x1}')
print(f'x2 = {x2}')

print(f'x1 + x2 = {x1 + x2}')
print(f'x1 - x2 = {x1 - x2}')
print(f'x1 * x2 = {x1 * x2}')
print(f'x1 / x2 = {x1 / x2}')

    # 2
class Drob:
    def __init__(self, ch, z):
        self.ch = ch
        self.z = z
    def __str__(self):
        return f'{self.ch}/{self.z}'
    def __add__(self, other):
        x = self.ch * other.z + self.z * other.ch
        y  = self.z * other.z
        return f'{x} / {y}'
    def __sub__(self, other):
        x = self.ch * other.z - self.z * other.ch
        y = self.z * other.z
        return f'{x} / {y}'
    def __mul__(self, other):
        x = self.ch * other.ch
        y = self.z * other.z
        return f'{x} / {y}'
    def __truediv__(self, other):
        x = self.ch * other.z
        y = self.z * other.ch
        return f'{x} / {y}'

drob1 = Drob(2, 3)
drob2 = Drob(5, 10)
print(f'drob1 = {drob1}')
print(f'drob2 = {drob2}')

print(f'{drob1} + {drob2} = {drob1+drob2}')
print(f'{drob1} - {drob2} = {drob1-drob2}')
print(f'{drob1} * {drob2} = {drob1*drob2}')
print(f'{drob1} / {drob2} = {drob1/drob2}')

    # 3
class Biblioteka:
    def __init__(self, name, adrs, summ):
        self.name = name
        self.adrs = adrs
        self.summ = summ
    def __str__(self):
        return f'Имя библиотеки: {self.name} \nАдрес библиотеки: {self.adrs} \nКол-во книг в библиотеке: {self.summ}'
    def __add__(self, other):
        x = self.summ + other.summ
        return x
    def __sub__(self, other):
        x = self.summ - other.summ
        return x
    def __iadd__(self, other):
        self.summ += other.summ
        return self.summ
    def __isub__(self, other):
        self.summ -= other.summ
        return self.summ
    def __lt__(self, other):
        s = self.summ
        o = other.summ
        return s < o
    def __gt__(self, other):
        s = self.summ
        o = other.summ
        return s > o
    def __eq__(self, other):
        s = self.summ
        o = other.summ
        return s == o
    def __ne__(self, other):
        s = self.summ
        o = other.summ
        return s != o
    def __le__(self, other):
        s = self.summ
        o = other.summ
        return s <= o
    def __ge__(self, other):
        s = self.summ
        o = other.summ
        return s >= o

bibl = Biblioteka("Им. Ломоносова", "ул. Швецова. д.39", 10)
print(bibl)
bibl2 = Biblioteka("Им. Ломоносова", "ул. Швецова. д.39", int(input('Укажите кол-во книг: ')))
print(f'{bibl + bibl2} книг при добавлении указанного кол-ва')
print(f'{bibl - bibl2} книг при вычетании указанного кол-ва')
print(f'+=: \n{bibl2}')
print(f'-=: \n{bibl2}')


print(f'bibl < bibl2 {bibl < bibl2}')
print(f'bibl > bibl2 {bibl > bibl2}')
print(f'bibl == bibl2 {bibl == bibl2}')
print(f'bibl != bibl2 {bibl != bibl2}')
print(f'bibl <= bibl2 {bibl <= bibl2}')
print(f'bibl >= bibl2 {bibl >= bibl2}')

    # 4
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __sub__(self, other):
        days_self = self.day + 30 * self.month + 365 * self.year
        days_other = other.day + 30 * other.month + 365 * other.year
        return days_self - days_other

    def __add__(self, days):
        days_self = self.day + 30 * self.month + 365 * self.year + days
        year = days_self // 365
        days_self -= year * 365
        month = days_self // 30
        days = days_self - month * 30
        return Date(days, month, year)

dateToday = Date(3, 4, 2023)
dateNew = Date(20, 5, 2025)
print(dateNew - dateToday)
print(dateNew + dateToday)