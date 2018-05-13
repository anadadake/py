import re
if __name__ == '__main__':
    key = r"<html><body><h1>hello world<h1></body></html>"
    p1 = r"(?<=<h1>).+(?=<h1>)"
    pattern1 = re.compile(p1)
    matcher1 = re.search(pattern1, key)
    print(matcher1.group(0))

    # key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
    # p1 = r"chuxiuhong@hit\.edu\.cn"
    # pattern1 = re.compile(p1)
    # print(pattern1.findall(key))
    #
    # key = r"<h1>hello world<h1>"  # 源文本
    # p1 = r"<h1>.+<h1>"  # 我们写的正则表达式，下面会将为什么
    # pattern1 = re.compile(p1)
    # print(pattern1.findall(key))  # 发没发现，我怎么写成findall了？咋变了呢？
    #
    # key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"  # 胡编乱造的网址，别在意
    # p1 = r"https*://"  # 看那个星号！
    # pattern1 = re.compile(p1)
    # print(pattern1.findall(key))
