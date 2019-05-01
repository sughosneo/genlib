'''
    This is the sample client which uses genlib library to implement some specific functionality.
'''
from genlib import genlib

class client(genlib):

    def operate(self):

        print("This is the operation method contains actual implementation")

        return 5 + 10

    def doSpecificOperation(self):

        print("This method is responsible to do client specific operation")


if __name__ == '__main__':

    myClient = client()

    # Shows all the methods and attributes present in the library and client.
    help(myClient)

    # Calling implemented operation
    value = myClient.operate()

    # Converting any value to string
    strValue = myClient.convertToStr(value)

    print(type(strValue))
    print(strValue)



