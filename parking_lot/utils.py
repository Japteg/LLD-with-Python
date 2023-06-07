
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


def parking_lot_exists(method):
    def wrapper(self, *args, **kw):
        if self.parking_lot is not None:
            return method(self, *args, **kw)
    return wrapper


class OutputPrinter:
    pass
