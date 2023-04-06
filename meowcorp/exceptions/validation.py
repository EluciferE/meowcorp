class MissingArguments(Exception):
    """
    If worker takes more args than he got
    """
    pass


class ExtraArguments(Exception):
    """
    If worker takes less args than he got
    """
    pass


class NotFound(Exception):
    """
    instance was not found in database by primary key
    """
    pass


class ConvertException(Exception):
    """
    can't convert data to type
    """
    pass
