import re



# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# function 1: isValidRomanNumber  -->done
# function 2: change Roman NUmber to decimal number
# function 3: change decimal number to Roman NUmber


def isValidRomanNumber(inputRomanNumberStr):
    # pattern = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$')
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$'
    matchObj = re.match(pattern, inputRomanNumberStr.upper())
    if matchObj:
        print("match for " + inputRomanNumberStr)
        #TODO
        sum = 0
        temp = 0

        # str = re.split('\d',)




    else:
        print("#### not match for " + inputRomanNumberStr)

def changeRoman2Dec(inputRomanNumberStr):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$'
    matchObj = re.match(pattern, inputRomanNumberStr)
    if matchObj:
        print("match for " + inputRomanNumberStr)
        lstOfChar = []
        upper = inputRomanNumberStr.upper()
        for i in range(0, len(upper)):
            lstOfChar.append(upper[i:i + 1])
        print(lstOfChar)
        #TODO
        # start
        sum = 0
        a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        left_char = ''

        for i in range(0,len(lstOfChar)):
            current_char=lstOfChar.pop()
            if i == 0:
                sum = sum + a_dict[current_char]
                left_char = current_char
            else:
                if current_char == 'I':
                    if left_char == 'I':
                        sum = sum + a_dict[current_char]
                    else:
                        sum = sum - a_dict[current_char]
                elif current_char == 'V':
                    sum = sum + a_dict[current_char]
                elif current_char == 'X':
                    #
                    if left_char == 'C' or left_char == 'L':
                        sum = sum - a_dict[current_char]
                    else:
                        sum = sum + a_dict[current_char]
                    # print()
                elif current_char == 'L':
                    sum = sum + a_dict[current_char]
                elif current_char == 'C':
                    if left_char == 'M' or left_char == 'D':
                        sum = sum - a_dict[current_char]
                    else:
                        sum = sum + a_dict[current_char]
                elif current_char == 'D':
                    sum = sum + a_dict[current_char]
                elif current_char == 'M':
                    sum = sum + a_dict[current_char]
                left_char = current_char
        print(sum)
        return sum

        #end

    else:
        raise ValueError('Not valid Roman Number! ')


if __name__ == '__main__':

    # a = 'MCMXL'.upper()
    # lstOfChar =[]
    #
    # for i in range(0,len(a)):
    #     print(i)
    #     lstOfChar.append(a[i:i+1])

    # print(lstOfChar)


    lst = ['XIX', 'MCM', 'MMMM', 'MCMXL']
    for i in lst:
        isValidRomanNumber(i)

    # 19
    changeRoman2Dec('XIX')
    #1900
    changeRoman2Dec('MCM')

    #1449
    changeRoman2Dec('MCDXLIX')
    # 1949
    changeRoman2Dec('MCMXLIX')

    #3000
    changeRoman2Dec('MMM')
    #1940
    changeRoman2Dec('MCMXL')
    #2666
    changeRoman2Dec('MMDCLXVI')
    #3888
    changeRoman2Dec('MMMDCCCLXXXVIII')
