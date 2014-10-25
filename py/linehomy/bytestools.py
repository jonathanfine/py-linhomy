class MixIn:


    def __new__(cls, bytes_or_str):

        if isinstance(bytes_or_str, str):

            data = cls.bytes_from_str(bytes_or_str)
            return super().__new__(cls, data)
