from FS.Binary import Binary


def test_binary():
    bn = Binary('binary', '9de3a64d8a4bb43877bc')
    bn_content = bn.read()
    assert bn_content == '9de3a64d8a4bb43877bc'

test_binary()