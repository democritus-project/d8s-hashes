import hashlib
from typing import Union

import ppdeep

from .hashes_temp_utils import validate_arg_value, string_encode_as_bytes


def ssdeep(input_string: Union[str, bytes]) -> str:
    """."""
    return ppdeep.hash(string_encode_as_bytes(input_string))


# TODO: I don't think this function is working properly
def ssdeep_compare(ssdeep_1: str, ssdeep_2: str) -> int:
    """."""
    return ppdeep.compare(ssdeep_1, ssdeep_2)


def md5(input_string: Union[str, bytes]) -> str:
    return _string_hash(input_string, 'md5')


def sha1(input_string: Union[str, bytes]) -> str:
    return _string_hash(input_string, 'sha1')


def sha256(input_string: Union[str, bytes]) -> str:
    return _string_hash(input_string, 'sha256')


def sha512(input_string: Union[str, bytes]) -> str:
    """Return the sha512 hash of the string."""
    return _string_hash(input_string, 'sha512')


@validate_arg_value(1, hashlib.algorithms_available)
def _string_hash(input_string: Union[str, bytes], hash_type: str) -> str:
    input_string = string_encode_as_bytes(input_string)
    hash_ = eval('hashlib.{}(input_string).hexdigest()'.format(hash_type))
    return hash_
