import functools
from typing import List, Union


def validate_arg_value(arg_index: Union[str, int, float], valid_values: List[str]):
    """Validate that the value of the argument at the given arg_index is in the list of valid_values."""

    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            arg_index_int = int(arg_index)
            arg_value = args[arg_index_int]

            if arg_value not in valid_values:
                message = f'The value of the argument at index {arg_index} (whose value is "{arg_value}") is not valid (valid values are: {valid_values}).'
                raise RuntimeError(message)

            return func(*args, **kwargs)

        return wrapper

    return actual_decorator


def string_encode_as_bytes(input_string: Union[str, bytes], encoding: str = 'utf-8', **kwargs):
    if isinstance(input_string, str):
        return input_string.encode(encoding, **kwargs)
    else:
        return input_string
