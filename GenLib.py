'''
    This is the base class.
    Any client which is planning to utalize this library they would require to inherit the base class.
'''

class genlibMeta(type):

    def __new__(cls, name,bases,body):

        print(body)

        if "operate" not in body:
            raise NotImplementedError("mustOperate() method needs to be implemented.")

        return super().__new__(cls, name,bases,body)


class genlib(metaclass=genlibMeta):

    def operate(self):
        '''
            Operate method needs to be implemented by the client for different operation.
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


