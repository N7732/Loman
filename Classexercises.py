# from abc import ABC, abstractmethod
# class Nation(ABC):
#     def people(self):
#         pass
# class tanzania(Nation):
#     def people(self):
#         print("Kiswahiri")
# class Rwanda(Nation):
#     def people(self):
#         print("Kinyarwanda")
# class France(Nation):
#     def people(self):
#         print("France")

# from typing import List
# p:list[str]=[]
# def get_string() -> list[str]:
#     return p
# while True:
#     n=str(input("Enter string : "))
#     if n.lower() == 'yes':
#         if len(p) >= 2:
#             break
#         else:
#             print("Please enter at least two strings before finishing.")
#     else:
#         p.append(n)
# print("All strings entered:", get_string())
# class student():
#     def __init__(self,name,regNumber,ssn):
#         self.name= name
#         self.regNumber=regNumber
#         self._ssn=ssn
#     @property
#     def ssn(self):
#         return "**********" + self._ssn[-3:]
# shaw= student("OLIVIER",224008132,"+250791756343")
# print(shaw.ssn)
# class study():
#     def __init__(self,name,respons):
#         self.name=name
#         self.respons=respons
#     def __setattr__(self,name,value):
#         if isinstance(value,str):
#             print(f"setting {name}={value}")
#             self.__dict__[name]=value
#         else:
#             raise Exception("Unexpected datatype")
# s = study("Alice", "Research")
# class boys:
#     def __init__(self):
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count<=10:
#             resul=self.count
#             self.count +=2
#             return resul
#         else:
#             raise StopIteration
# celia=boys()
# for n in celia:
#     print(n)
from abc import ABC,abstractmethod
class people(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def colour(self):
        pass
class rwanda(people):
    def speak(self):
        print("Kinyarwanda")
    def colour(self):
        print("Black")
class france(people):
    def speak(self):
        print("France")
    def colour(self):
        print("white")
a=rwanda()
b=france()
print(f"Rwandan say :{a.speak()} and is :{a.colour()}")
print(f"France say :{b.speak()} ans is {b.colour()}")
        
        