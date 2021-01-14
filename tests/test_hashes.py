from democritus_hashes import (
    md5,
    sha1,
    sha256,
    sha512,
    ssdeep_compare,
    ssdeep,
)


def test_md5_1():
    assert md5('foobar') == '3858f62230ac3c915f300c664312c63f'


def test_sha1_1():
    assert sha1('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'


def test_sha256_1():
    assert sha256('foo') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'


def test_sha512_1():
    assert (
        sha512('foo')
        == 'f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'
    )


def test_ssdeep_compare_1():
    result = ssdeep_compare(ssdeep('foo'), ssdeep('fool'))
    assert result == 0

    result = ssdeep_compare(ssdeep('this is just a test'), ssdeep('this is just a jest'))
    assert result == 0
