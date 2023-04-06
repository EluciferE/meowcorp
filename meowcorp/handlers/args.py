import inspect
from models.models import Base
from settings.settings import SEPARATOR
from meowcorp.exceptions.validation import *


class ArgsValidation:

    def __init__(self):
        self.possible_classes = []
        self._init_classes()

    def _init_classes(self):
        possible_models = __import__('models.models', fromlist=('*',))
        self.possible_classes = []

        for class_object in dir(possible_models):
            attr = getattr(possible_models, class_object)
            if not inspect.isclass(attr):
                continue

            if not issubclass(attr, Base):
                continue

            if attr == Base:
                continue

            self.possible_classes.append(attr)

    def prepare_args(self, class_object, db, user=None, call=None):
        if user is not None:
            args = user.status.split(SEPARATOR)[1:]
        elif call is not None:
            args = call.data.split(SEPARATOR)[1:]
        else:
            return []

        func_args_dict = inspect.getfullargspec(class_object.work)

        func_args = func_args_dict.args[1:]
        defaults = func_args_dict.defaults if func_args_dict.defaults is not None else tuple()

        if len(func_args) > len(args) + len(defaults):
            missing_args = func_args[len(args):]
            if defaults:
                missing_args = func_args[len(args): -len(defaults)]

            missing_args = list(map(lambda x: f"'{x}'", missing_args))

            raise MissingArguments(f'{class_object.__class__.__name__}->work()'
                                   f' missing {len(missing_args)} required args: {", ".join(missing_args)}')

        if len(func_args) < len(args):
            raise ExtraArguments(f'{class_object.__class__.__name__}->work()'
                                 f'takes {len(func_args)} args but {len(args)} was given')

        annotations = func_args_dict.annotations

        for index, arg_name in enumerate(func_args[:len(args)]):
            if arg_name not in annotations:
                continue

            arg_type = annotations[arg_name]

            if arg_type in self.possible_classes:
                instance = db.query(arg_type).get(args[index])
                if instance is None:
                    raise NotFound(f"Instance {arg_type.__name__}"
                                   f" was not found by 'pk = {args[index]}'")

                args[index] = instance
                continue

            if arg_type == int:
                if args[index].isnumeric():
                    args[index] = int(args[index])
                    continue

                raise ConvertException(f"Could not convert {args[index]} to int")

            if arg_type == float:
                if args[index].count('.') <= 1 and \
                        args[index].replace('.', '').isnumeric():
                    args[index] = float(args[index])
                    continue
                raise ConvertException(f"Could not convert {args[index]} to float")

            if arg_type == bool:
                if args[index].isnumeric():
                    args[index] = bool(int(args[index]))
                else:
                    args[index] = bool(args[index])

        return args


args_validation = ArgsValidation()
