from abc import ABC,abstractmethod

class AbstractGenLib(ABC):

    @abstractmethod
    def operate(self):
        '''
            This is the abstract method which would be implemented in the child class.
        :return:
        '''
        pass

    def convertToStr(self,value):

        '''
            Genertic convertion method to convert any value to type string.
        :param value:
        :return: str(value)
        '''

        if value:
            return str(value)
        else:
            raise ValueError("Passed value is None!")


