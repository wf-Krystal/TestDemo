#!/usr/bin/python
# -*- coding: UTF-8 -*-

def bubble_sort(lists):
    len_list = len(lists)
    for i in range(len_list):
        for j in range(len_list-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
        print(lists)
    return lists


def insert_sort(lists):
    for i in range(len(lists)):
        position = i
        while position > 0:
            if lists[position] < lists[position-1]:
                lists[position], lists[position-1] = lists[position-1], lists[position]
            position -= 1
        print(lists)
    return lists

def insert_sort2(lists):
    for i in range(len(lists)):
        position = 0
        while position < len(lists)-1:
            if lists[position] > lists[position+1]:
                lists[position], lists[position+1] = lists[position+1], lists[position]
            position += 1
        print(lists)
    return lists



bubble_sort([1, 2, 4, 3, 2, 1, 0, 10, 5, 8, 9])
print('-----------------分隔线----------------------')
insert_sort([1, 2, 4, 3, 2, 1, 0, 10, 5, 8, 9])
print('-----------------分隔线----------------------')
insert_sort2([1, 2, 4, 3, 2, 1, 0, 10, 5, 8, 9])