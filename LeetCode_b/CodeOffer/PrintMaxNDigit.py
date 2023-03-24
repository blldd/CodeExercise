# -*- coding:UTF-8 -*-

def Print1(n):
    if n <= 0:
        return
    list_num = ["0"] * n
    while Increament(list_num) is False:  # 判断时候已经去到最大值了，是的话停止
        PrintNumber(list_num)


def PrintNumber(number):
    isBegin = False
    for i in range(len(number)):
        if number[i] != "0" and isBegin is False:
            isBegin = True
        if isBegin:
            tmp = ("".join(number[i:]))
            print(tmp)
            break


def Increament(number):
    isOverFlow = False
    isIncre = 0  # 是够归零进一
    len_num = len(number)
    n = len_num - 1  # 因为从最后一位开始而不是0位
    while n >= 0:
        nsum = int(number[n]) + isIncre
        if n == len_num - 1:
            nsum += 1  # 就是最后一位加一
        if nsum == 10:
            if n == 0:
                isOverFlow = True  # 如果是最后的一个9999加一 那说明已经移除  例如 2位 的是 99 再加一就是溢出了
            else:
                isIncre = 1  # 如果不是那么就前面一位加一,自己变为0
                number[n] = "0"
        else:
            number[n] = str(nsum)
        n -= 1
    return isOverFlow


if __name__ == '__main__':
    Print1(3)
