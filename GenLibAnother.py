from AbstractGenLib import *

class GenLibAnother(AbstractGenLib):

    def operate(self):
        print("This is operation method !")

        return 5 + 10

    def convert(self,value):

        return self.convertToStr(value)

if __name__ == '__main__':

    client = GenLibAnother()
    value = client.operate()

    print(type(client.convert(value)))
    print(client.convert(value))