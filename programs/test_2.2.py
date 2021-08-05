
# 2. Объявите класс Point с конструктором, который бы позволял создавать экземпляр на основе другого, уже существующего.
# Если аргументы в конструктор не передаются, то создается объект с локальными атрибутами по умолчанию.
# т.е. в конструктор может быть передан экземпляр класса Point и по его данным нужно создать новый экземпляр класса Point
# p1 = Point(1,2) и, затем сделать так: p2 = Point(p1)



class Point1:
    '''класс Point1 с конструктором, который бы позволял создавать экземпляр
     на основе другого, уже существующего. Если аргументы в конструктор не передаются, то
     создается объект с локальными атрибутами по умолчанию.
        '''
    def __init__(self, x, y = None):
        if y is None:
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y

    # Этот метод возвращает строковое представление объекта.
    # Этот метод вызывается, когда для объекта вызывается функция print () или str () - __str__.
    def __str__(self):
        return str(self.x) + " " + str(self.y)

# т.е. в конструктор может быть передан экземпляр класса Point
# и по его данным нужно создать новый экземпляр класса Point
pt_Point1 = Point1(5, 10)                   # в конструктор Point1 передадим экземпляр класса pt_Point1
print(pt_Point1)
# p1 = Point(1,2) и, затем сделать так: p2 = Point(p1)
pt22 = Point1(pt_Point1)                    # создан новый экземпляр класса pt22, на основе уже существующего pt_Point1
print(pt22)

pt22 = Point1(6, 11)                        # создадим в экземпляре класса pt22  новые два параметра
print(pt22)
print(pt_Point1.__dict__, pt22.__dict__)

print(type(pt_Point1), type(pt22))
