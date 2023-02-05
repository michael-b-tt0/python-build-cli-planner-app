from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime
from src.reminder import PoliteReminder
import logging

logging.basicConfig(level=logging.DEBUG, format= "%(levelname)s %(message)s")


class DeadlinedMetaReminder(Iterable, metaclass= ABCMeta):


    @abstractmethod
    def is_due(self):
        raise NotImplementedError



class DeadlinedReminder(Iterable, ABC):

    
    @abstractmethod
    def is_due(self):
        raise NotImplementedError
    


    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date) -> None:
        self.text = text 
        self.date = parse(timestr = date, dayfirst=True)

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        formatted_date = self.date.isoformat()
        

        return iter([self.text, formatted_date])


DeadlinedReminder.register(PoliteReminder)



        


