#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
#from decimal import Decimal


def read_file(path):
    file_to_list = []
    with open(path, "r") as file:      #Открываем файл для чтения
        for line in file:
            line_to_list = []
            for i in line.split():    #Переводим каждую строку файла в список
                #print(line.split())
                line_to_list.append(float(i))    #Переводим текстовые записи в числа
            file_to_list.append(line_to_list)    #Каждый файл - это главный список, каждая строка - подсписок
    #print(file_to_list)
    return file_to_list


def distance(circle_coord, dot_coord):
    dist = math.sqrt((dot_coord[0] - circle_coord[0]) ** 2 + (dot_coord[1] - circle_coord[1]) ** 2)
    return dist


def main():
    if len(sys.argv) > 2:
        coordinates_of_circle = read_file(sys.argv[1])
        points = read_file(sys.argv[2])
        for point in points:
            dist = distance(coordinates_of_circle[0], point)
            if coordinates_of_circle[1][0] == dist:
                print(0)
            elif coordinates_of_circle[1][0] > dist:
                print(1)
            else:
                print(2)
    else:
        print("Enter arguments")


if __name__ == "__main__":
    main()
