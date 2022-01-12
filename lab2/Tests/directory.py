from FS.Buffer import Buffer
from FS.Directory import Directory


def test_create():
    dir = Directory('dir')

    for i in range(dir.DIR_MAX_ELEMS*2):
        buff = Buffer(f'buff{i}', ['random string'])
        dir.append(buff)

    assert len(dir.files) == dir.DIR_MAX_ELEMS


def test_move():
    dir1 = Directory('dir1')
    dir2 = Directory('dir2')
    assert len(dir1.files) == 0
    assert len(dir2.files) == 0

    buff = Buffer('buff', ['random string'])

    dir1.append(buff)
    assert len(dir1.files) == 1

    dir1.move(buff, dir2)
    assert len(dir1.files) == 0
    assert len(dir2.files) == 1

test_create()
test_move()