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
    assert md5(['foo', 'bar']) == ['acbd18db4cc2f85cedef654fccc4a4d8', '37b51d194a7513e45b56f6524f2d51f2']


def test_sha1_1():
    assert sha1('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert sha1(['foo', 'bar']) == [
        '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33',
        '62cdb7020ff920e5aa642c3d4066950dd1f01f4d',
    ]


def test_sha256_1():
    assert sha256('foo') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'
    assert sha256(['foo', 'bar']) == [
        '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae',
        'fcde2b2edba56bf408601fb721fe9b5c338d10ee429ea04fae5511b68fbf8fb9',
    ]


def test_sha512_1():
    assert (
        sha512('foo')
        == 'f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'
    )
    assert sha512(['foo', 'bar']) == [
        'f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7',
        'd82c4eb5261cb9c8aa9855edd67d1bd10482f41529858d925094d173fa662aa91ff39bc5b188615273484021dfb16fd8284cf684ccf0fc795be3aa2fc1e6c181',
    ]


def test_ssdeep_compare_1():
    result = ssdeep_compare(ssdeep('foo'), ssdeep('fool'))
    assert result == 0

    result = ssdeep_compare(ssdeep('this is just a test'), ssdeep('this is just a jest'))
    assert result == 0
