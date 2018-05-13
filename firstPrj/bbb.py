import os, glob, time
import humansize
import sys

if __name__ == '__main__':
    print(os.getcwd())
    print(glob.glob('*.py'))

    metadata = os.stat('aaa.py')
    print(time.localtime(metadata.st_mtime))

    for a in metadata:
        print(type(a))
        print(a)

    a_list = [1, 2, 3, 4, 5, 6]
    print([elem * 2 for elem in a_list])

    print([os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 100])

    print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')])
    print({os.stat(f).st_size: os.path.realpath(f) for f in glob.glob('*.py')})

    a_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    double_a_set = {x**2 for x in a_set}

    print(double_a_set)
    print("----------------")
    si_suffixes = humansize.SUFFIXES[1000]
    print(si_suffixes)

    print('1000{0[2]} = 1{0[3]}'.format(si_suffixes))
    print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))


    by = b'\x61'
    print(by)
    print(b'\xe6')
    print('a'.encode('utf-8'))

    a_string = '深入 Python'
    by = a_string.encode('utf-8')
    print(by)
    print(len(by))
    print(by.decode('utf-8'))