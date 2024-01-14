from enum import Enum



class BaseType(Enum):
        def __new__(cls, *args, **kwargs):
            obj = object.__new__(cls)
            if isinstance(args[0], BaseType):
                obj._value_ = args[0].code
            else:
                obj._value_ = args[0]
            return obj


