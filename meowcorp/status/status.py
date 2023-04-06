from settings.settings import SEPARATOR
from meowcorp.exceptions.status import SimilarStatuses


class auto:
    pass


class STATUS:
    def __init__(self, raw: str):
        self.raw = raw

    def __call__(self, *args, **kwargs) -> str:
        value = self.raw

        args = list(args) + list(kwargs.values())

        args = list(map(lambda arg: str(int(arg)) if isinstance(arg, bool) else str(arg), args))

        return SEPARATOR.join([value] + args)

    def match(self, user=None, call=None) -> bool:
        if user is not None:
            return user.status.split(SEPARATOR)[0] == self.raw

        if call is not None:
            return call.data.split(SEPARATOR)[0] == self.raw

        return Fasle

    def get_status(self) -> str:
        return self.raw

    def __str__(self) -> str:
        return f"<Status raw={self.raw}>"


class StatusEnum(type):

    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)

        statuses = [name for name, func in attrs.items() if isinstance(func, auto) or func == auto]
        updated = []

        for status in statuses:
            if status.upper() in updated:
                raise SimilarStatuses(f"Got similar statuses: {status}")

            status_class = STATUS(raw=status.upper())
            setattr(cls, status, status_class)

            updated.append(status.upper())
