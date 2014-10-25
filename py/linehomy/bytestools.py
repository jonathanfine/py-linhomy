class MixIn:

    __str_format = "{0}({1})".format

    def __new__(cls, data_or_str):

        if isinstance(data_or_str, str):
            data = cls.data_from_str(data_or_str)
        else:
            data = data_or_str

        cls.check_data(data)
        return super().__new__(cls, data)


    def __str__(self):

        name = self.__class__.__name__
        arg = self.arg

        return self.__str_format(name, repr(arg))

    __repr__ = __str__


    def __eq__(self, other):

        if type(self) != type(other):
            raise TypeError

        return super().__eq__(self, other)
