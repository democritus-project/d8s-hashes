from d8s_hashes import (
    md5,
    sha1,
    sha256,
    sha512,
    ssdeep_compare,
    ssdeep,
)


def test_md5_1():
    assert md5('foobar') == '3858f62230ac3c915f300c664312c63f'
    assert md5(b'foobar') == '3858f62230ac3c915f300c664312c63f'


def test_sha1_1():
    assert sha1('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'


def test_sha256_1():
    assert sha256('foo') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'


def test_sha512_1():
    assert (
        sha512('foo')
        == 'f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'
    )


def test_ssdeep_1():
    result = ssdeep('foo')
    assert result == '3:Nn:N'

    result = ssdeep('this is just a test')
    assert result == '3:YKPQCEPRn:YUg'


def test_ssdeep_compare_1():
    # compare the same string
    result = ssdeep_compare(
        ssdeep('when in the course of human events it becomes necessary'),
        ssdeep('when in the course of human events it becomes necessary'),
    )
    assert result == 100

    # compare slightly different strings
    result = ssdeep_compare(
        ssdeep('when in the course of human events it becomes unnecessary'),
        ssdeep('when in the course of human events it becomes necessary'),
    )
    assert result == 14

    # if values are very short, differences will not be detected
    result = ssdeep_compare(ssdeep('foo'), ssdeep('fool'))
    assert result == 0
