class StorageFullException(Exception):

    def __init__(self, message='Storage full'):
        super().__init__(message)


class NotFoundException(Exception):

    def __init__(self, message='Key not found'):
        super().__init__(message)
