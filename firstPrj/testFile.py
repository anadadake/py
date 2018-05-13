if __name__ == '__main__':
    # a_file = open('C:/Users/anada/Desktop/linux.txt',mode='r',encoding='gb2312')
    # a_string = a_file.read()
    #
    # print(a_string)
    # print(a_file.name)
    # print(a_file.encoding)
    # print(a_file.read())
    # a_file.seek(3)
    # print(a_file.read(2))
    # print(a_file.tell())
    with open('C:/Users/anada/Desktop/linux.txt',mode='r',encoding='gb2312') as a_file:
        a_file.seek(17)
        a_character = a_file.read(1)
        print(a_character)
