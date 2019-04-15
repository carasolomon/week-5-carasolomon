# Tacara Solomon - Week 5 Assignment: Design Patterns

# Factory Pattern
from abc import ABCMeta, abstractclassmethod

class Rooms(metaclass=ABCMeta):
    def __init__(self, name, bedrooms, price):
        self.name = name
        self.bedrooms = bedrooms
        self.price = price

    @classmethod
    def getPrice(self):
        pass

    def __str__(self):
       return '{} dollars per night'.format(self.price)    

    
class PenthouseRoom(Rooms):
    def getPrice(self):
        return 398

class SingleBedRoom(Rooms): 
    def getPrice(self):
        return 189

class DoubleBedRoom(Rooms):
    def getPrice(self):
        return 205

class RoomFactory(object):
    @classmethod
    def create(cls, room, *args):
        room = room.lower().strip()

        if room == 'penthouseroom':
            return PenthouseRoom(*args)
        elif room == 'singlebedroom':
            return SingleBedRoom(*args)
        elif room == 'doublebedroom':
            return DoubleBedRoom(*args)     

# Facade Pattern
class GetUserAccount:
    def __init__(self):
        self._account = Account()
        self._payment = Payment()

    def getInfo(self):
        self._account.getAccountNumber()

    

class Account:
    def __init__(self, _name, _address, _accountNumber, _paymentInfo):
        self._name = _name
        self._address = _address
        self._accountNumber = _accountNumber
        self._paymentInfo = _paymentInfo

    def getAccountNumber(self):
        return self._accountNumber


class Payment:
    def __init__(self, _accountNumber, _creditCardNumber, _billingAddress):
        self._accountNumber = _accountNumber
        self._creditCardNumber = _creditCardNumber
        self._billingAddress = _billingAddress

    def getCardNumber(self): 
        return self._creditCardNumber 

def main():
    getInfo = GetUserAccount()
    getInfo.getInfo()


# Singleton Pattern - One account instance open at a time
class Account2:
    __instance = None

    def __new__(cls):
      if cls.__instance == None:
        cls.__instance = "Open Account"
      return cls.__instance