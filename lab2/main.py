from FS.Log import Log
from FS.Binary import Binary
from FS.Directory import Directory
from FS.Buffer import Buffer
import random
import string


def print_filesystem(fs):
    fs.list_subdirectories()
    print('\n-----------------------------------\n')


def random_string(k=18):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def generate_array(num, type):
    arr = []
    if type == 'bin':
        for i in range(num):
            arr.append(Binary('Bin_{}'.format(
                random_string(3)), random_string(10)))
    if type == 'log':
        for i in range(num):
            arr.append(
                Log('Log_{}'.format(random_string(3)), '[0{}.11.2021]: {}'.format(i, random_string(10))))
    if type == 'buf':
        for i in range(num):
            arr.append(Buffer('Buf_{}'.format(random_string(3)), []))
    return arr


fs = Directory('Directory', [])

bins = generate_array(5, 'bin')
logs = generate_array(5, 'log')
bufs = generate_array(3, 'buf')

logs_1 = generate_array(1, 'log')[0]
logs_2 = generate_array(3, 'log')
bins_1 = generate_array(1, 'bin')[0]
bins_2 = generate_array(1, 'bin')[0]

dir_4_3 = Directory('dir_3', logs_2)
dir_4_2 = Directory('dir_2', [dir_4_3, logs_1])
dir_4_1 = Directory('dir_1', [dir_4_2, bins_1])

dir1 = Directory('bins', bins)
dir2 = Directory('logs', logs)
dir3 = Directory('bufs', bufs)
dir4 = Directory('dirs', [dir_4_1])

fs.append(dir1)
fs.append(dir2)
fs.append(dir3)
fs.append(dir4)

print_filesystem(fs)

print('Files {}, {} and {} are to be deleated.'.format(
    bins[0].name, logs[3].name, bufs[2].name))
dir1.delete(bins[0])
dir2.delete(logs[3])
dir3.delete(bufs[2])

print('File {} is moved to {} directory.'.format(logs[4].name, dir_4_1.name))
dir2.move(logs[4], dir_4_1)

print('Folder {} is removed.'.format(dir1.name))
fs.delete(dir1)

print('Folder {} is moved to {}.'.format(dir_4_2.name, dir2.name))
dir_4_1.move(dir_4_2, dir2)
print_filesystem(fs)

# bufs[0].push(random_string(3))
# bufs[0].push(random_string(3))
# bufs[0].push(random_string(3))
# bufs[0].push(random_string(3))
# print(bufs[0].queue)
# bufs[0].consume()
# print(bufs[0].queue)
