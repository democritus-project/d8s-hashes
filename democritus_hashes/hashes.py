import hashlib
import os
import sys

import ppyssdeep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import decorators
from strings import string_encode_as_bytes


@decorators.map_first_arg
def ssdeep(input_string: str) -> str:
    """."""
    return ppyssdeep.ssdeep_hash(string_encode_as_bytes(input_string))


# TODO: I don't think this function is working properly
def ssdeep_compare(ssdeep_1: str, ssdeep_2: str) -> int:
    """."""
    return ppyssdeep.ssdeep_compare(ssdeep_1, ssdeep_2)


@decorators.map_first_arg
def md5(input_string: str) -> str:
    return _string_hash(input_string, 'md5')


@decorators.map_first_arg
def sha1(input_string: str) -> str:
    return _string_hash(input_string, 'sha1')


@decorators.map_first_arg
def sha256(input_string: str) -> str:
    return _string_hash(input_string, 'sha256')


@decorators.map_first_arg
def sha512(input_string: str) -> str:
    """Return the sha512 hash of the string."""
    return _string_hash(input_string, 'sha512')


@decorators.validate_arg_value(1, hashlib.algorithms_available)
def _string_hash(input_string: str, hash_type: str) -> str:
    input_string = string_encode_as_bytes(input_string)
    hash_ = eval('hashlib.{}(input_string).hexdigest()'.format(hash_type))
    return hash_
