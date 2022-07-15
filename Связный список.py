class ListObject:
    
    def __init__(self, data):
        self.data = data
        self.next_obj = None
        
    def link(self, obj):
        tail = ListObject(obj)
        head = self
        while head.next_obj:
            head = head.next_obj
        head.next_obj = tail
        
# считывание списка из входного потока (эту строку не менять)
lst_in = ['1. Первые шаги в ООП',
            '1.1 Как правильно проходить этот курс',
            '1.2 Концепция ООП простыми словами',
            '1.3 Классы и объекты. Атрибуты классов и объектов',
            '1.4 Методы классов. Параметр self',
            '1.5 Инициализатор init и финализатор del',
            '1.6 Магический метод new. Пример паттерна Singleton',
            '1.7 Методы класса (classmethod) и статические методы (staticmethod)',]

iter_data = iter(lst_in) 
    

head_obj = ListObject(next(iter_data))
for s in range(1, len(lst_in)):
    head_obj.link(next(iter_data))


def p(a):
    if a.next_obj is None:
        print(a.data)
        return 
    else:
        print(a.data)
        p(a.next_obj)
p(head_obj)
