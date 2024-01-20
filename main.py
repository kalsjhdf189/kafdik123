#class Book:
#    def __init__(self, title, author, isbn):
#        self.__title = title #приватный
#        self.__author = author #приватный
#        self.__isbn = isbn #приватный
#
#    def get_title(self):
#        return self.__title
#    def set_title(self, title):
#        self.__title = title
#    def get_author(self):
#        return self.__author
#
#    def set_author(self, author):
#        self.__author = author
#    def get_isbn(self):
#        return self.__isbn
#    def set_isbn(self, isbn):
#        self.__isbn = isbn
#
#book1 = Book("Вино из одуванчиков", "Рей Бредбери", "11111111111111")
#print(book1.__title)

#Пример 2

#class Book:
#    def __init__(self, title, author, isbn):
#        self.__title = title #приватный
#        self.__author = author #приватный
#        self.__isbn = isbn #приватный
#
#    def get_title(self):
#        return self.__title
#    def set_title(self, title):
#        self._title = title
#
#    def get_author(self):
#        return self.__author
#    def set_author(self, author):
#        self.__author = author
#    def get_isbn(self):
#        return self.__isbn
#    def set_isbn(self, isbn):
#        self.__isbn = isbn
#
#book1 = Book("Вино из одуванчика", "Брэдбери", "111111111")
#print(book1.get_title())
#print(book1.get_author())
#print(book1.get_isbn())
#book1.set_title("Рэй Брэдбери")
#print(book1.get_title())

#Задание 1
class Student:
    def __init__(self, name, age, group, marks):
        self.__name = name
        self.__age = age
        self.__group = group
        self.__marks = marks

    def avarage (self):
        av = float()
        for mark in self.__marks:
            av += mark
        av = av / len(self.__marks)
        return av
class1 = Student("Миша", "18", "ПРС-14", [2,3,5,3,4,5,5,5,5,5])
print(class1.avarage())
