# -*- coding:utf-8 -*-
import os
import sys

def full2half(ustring):
    rstring = ''
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288: 
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring

def chnum_to_arabic(str):
    str = str.replace(u"零".encode("gb18030"), u"零零".encode("gb18030"))
    return arabic(str)

def arabic(str):

    a_table = [(u"十", 10), (u"百", 100), (u"千", 1000), (u"万", 10000), (u"零", 0), (u"佰", 100), (u"仟", 1000)] 
    b_table = [(u"零", 0), (u"一", 1), (u"二", 2), (u"三", 3), (u"四", 4), (u"五", 5), (u"六", 6),\
               (u"七", 7), (u"八", 8), (u"九", 9), (u"十", 10), (u"壹", 1), (u"貮", 2), (u"叁", 3),\
               (u"肆", 4), (u"伍", 5), (u"陆", 6), (u"柒", 7), (u"捌", 8), (u"玖", 9), (u"拾", 10)] 
    a_dict = {}
    b_dict = {}
    for a in a_table:
        a_dict[a[0].encode("gb18030")] = a[1]
    for b in b_table:
        b_dict[b[0].encode("gb18030")] = b[1]
    
    s = str[:4]
    if s.__len__() == 0:
        return 0
    elif s.__len__() == 2 and s in b_dict:
        return b_dict[s]
    elif s.__len__() >= 4 and s[2:] in a_dict and s[:2] in b_dict:
        return b_dict[s[:2]] * a_dict[s[2:]] + arabic(str[4:])
    else:
        return 0
if __name__ == "__main__":
    print chnum_to_arabic("十".decode("utf-8").encode("gb18030"))
