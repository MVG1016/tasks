#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def read_file(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            for i in line.strip().split():
                data.append(int(i))
    return data


def main():
    if len(sys.argv) > 1:
        digits = {}
        nums = read_file(sys.argv[1])
        #print(nums)
        for i in nums:
            if i in digits:
                digits[i] += 1
            else:
                digits[i] = 1
        nums.sort()
        average_sum = sum(nums) // len(nums)
        middle = nums[len(nums) // 2]
        #count_sum = 0
        count_middle = 0
        #print(nums)
        #Будем приводить к среднему элементу массива
        for n in nums:
            #count_sum += abs(n - average_sum)
            count_middle += abs(n - middle)
        #print(count_sum, count_middle)
        print(count_middle)
    else:
        print("Enter arguments")


if __name__ == "__main__":
    main()