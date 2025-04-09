class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: 'ObjList') -> None:
        '''Добавление нового объекта obj класса ObjectList в конец списка'''
        if self.tail is None:
            self.tail = obj
            self.head = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        '''Удаление последнего объекта из связного списка'''
        if self.tail is None:
            return
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        '''Получение списка из строк локального свойства __data всех объектов связного списка'''
        list_data = []
        current_obj = self.head
        while current_obj:
            list_data.append(current_obj.get_data())
            current_obj = current_obj.get_next()
        return list_data


class ObjList:
    def __init__(self, data: str):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj: 'ObjList'):
        self.__next = obj

    def set_prev(self, obj: 'ObjList'):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data: str):
        if type(data) == str:
            self.__data = data
        else:
            raise TypeError("data должна быть строкой")

    def get_data(self):
        return self.__data


obj = ObjList("first data")
obj_2 = ObjList("second data")
lst = LinkedList()
lst.add_obj(obj)
lst.add_obj(obj_2)
lst.add_obj(ObjList("other data"))
result = lst.get_data()
print(result)
