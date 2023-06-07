class InvalidApiException(Exception):

    def __init__(self, api_name='', message='Invalid API'):
        message = 'Error: ' + message
        if len(api_name):
            message += ' - ' + api_name
        super().__init__(message)


class InvalidTicketException(Exception):

    def __init__(self, ticket_id='', message='Invalid Ticket'):
        message = 'Error: ' + message
        if len(ticket_id):
            message += ' - ' + ticket_id
        super().__init__(message)


class ParkingLotFullException(Exception):

    def __init__(self, vehicle_type='', message='Parking lot is full'):
        if len(vehicle_type):
            message += ' - ' + vehicle_type
        super().__init__(message)
