class MixIn:


    def __new__(cls, data_or_str):

        if isinstance(data_or_str, str):
            data = cls.data_from_str(data_or_str)
        else:
            data = data_or_str

        cls.check_data(data)
        return super().__new__(cls, data)
