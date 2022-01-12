from FS.Buffer import Buffer

buff = Buffer('buffer_1', [])

def test_push():
    element01 = '01'
    assert(buff.push(element01))

def test_size():
    elements_arr = []

    for i in range(buff.MAX_BUF_FILE_SIZE*2):
        elements_arr.append('rnd{i}')

    buff_1 =  Buffer('buffer_2', elements_arr)
    assert(buff_1.push('element01') == False)


def test_consume():
    element02 = '02'
    buff.push(element02)
    assert(len(buff.queue) == 2)
    assert(buff.consume())
    assert(buff.consume())
    assert(buff.consume() == False)
    

test_push()
test_size()
test_consume()