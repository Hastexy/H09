class NameLengthException(Exception):
    pass

# class AlreadyRegisteredExeption(Exception)
#     pass

def validate_name(name):
    if len(name) >= 50:
        raise NameLengthException()
    
# def validate_results(score):
#     if score in results:
#         raise AlreadyRegisteredExeption()