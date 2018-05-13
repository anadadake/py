
from humansize import approximate_size
import os
import glob

if __name__ == '__main__':
    sizeOf1000 = approximate_size(49595949393,False)
    sizeOf1024 = approximate_size(49595949393)
    print(sizeOf1000)
    print(sizeOf1024)
    x=1
    print(x+1)
    print(True)
    print(False)
    print(type(1))
    print(isinstance(1,int))
    print(isinstance(1.0,float))
    print(isinstance(float(1),float))

    a_list = ['a', 'b', 'c']
    a_list.extend(['d','e','f'])
    print(a_list)
    a_list.append(['g', 'h', 'i'])
    print(a_list)
    print(len(a_list))
    print('a' in a_list)
    print('----')
    # print(a_list.count('b'))
    # print(a_list.index('x'))
    print(a_list[1])
    print(a_list)
    del a_list[1:2]
    print(a_list)
    print(a_list.pop(0))
    print(a_list)
    print(a_list.pop())
    print(a_list)
    print('Tuple---------------------------------')
    a_tuple=("a", "b", "mpilgrim", "z", "example")
    print(a_tuple)
    b_list = list(a_tuple)
    print(b_list)
    v = ('a', 2, True)
    (x, y, z) = v
    print(x)
    print(y)
    print(z)
    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    print(SUNDAY)

    a_list = ['a', 'b', 'mpilgrim', True, False, 42]
    a_set= set(a_list)
    print(a_set)
    a_set = {}
    if a_set:
        print(111)
    else:
        print(222)
    print(type(a_set))
    # a_set.pop()

    a_set = {2, 4, 5, 9}
    b_set = {1, 2, 3, 5}
    print(a_set.union(b_set))
    print(a_set.intersection(b_set))
    print(a_set.difference(b_set))
    print(a_set.symmetric_difference(b_set))

    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
    print(a_dict)
    a_dict['user']= 'kevin'
    print(a_dict)
    print(a_dict['user'])

    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
    print(SUFFIXES)
    print(len(SUFFIXES))
    print(len(SUFFIXES[1000]))
    print(SUFFIXES[1000])
    print("---------------------------------")
    print(os.getcwd())
    # print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))
    pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
    (dirname,filename) = os.path.split(pathname)
    print(dirname)
    print(filename)

    print(glob.glob('/*.*'))