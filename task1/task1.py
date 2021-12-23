#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from itertools import cycle


def circular_array(n, m):
    in_arr = []    #input array numbers
    for i in range(n):
        in_arr.append(i+1)
    #print(in_arr)
    cycled_in_arr = cycle(in_arr)    #cycled input array numbers

    count_m = 0
    for i in cycled_in_arr:
        count_m += 1
        if count_m == 1:              #В начале всегда должен быть 1
            print(i, end='')
        if count_m == m and i != 1:
            count_m = 1               #Нужно обнулиить счетчик чтобы новый цикл начинался с конца предыдущего
            print(i, end='')
        elif count_m == m and i == 1:  #Если вернулись в начало, то ничего не пишем и завершаем цикл
            print("")
            break


def main():
    if len(sys.argv) > 2:     #Должно быть 3 аргумета
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        circular_array(n, m)
    else:
        print("Enter arguments")


if __name__ == "__main__":
    main()
