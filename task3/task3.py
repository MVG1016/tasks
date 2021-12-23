# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json


def read_json(path):
    with open(path) as f:
        templates = json.load(f)
        #print(templates)
        return templates


def write_json(data, name):
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_values(dictionary):
    data = []
    for d in dictionary:
        t = type(dictionary[d])
        #print(d)
        #print(t)
        #print(dictionary[d])
        if t is list:
            for element in dictionary[d]:
                data += (get_values(element))
                #    print(get_values(element))
        else:
            data.append(dictionary[d])
            #print(dictionary[d])
            #print(data)
    #print(data)
    return data


def edit_data(dictionary, values):
    for d in dictionary:
        t = type(dictionary[d])
        if t is list:
            for element in dictionary[d]:
                edit_data(element, values)
        else:
            if d == "id":
                try:
                    dictionary["value"] = values[values.index(dictionary[d]) + 1]
                except ValueError:
                    pass


def main():
    if len(sys.argv) > 2:
        tests = read_json(sys.argv[1])
        values = read_json(sys.argv[2])
        values_list = get_values(values)
        edit_data(tests, values_list)
        write_json(tests, "report.json")
    else:
        print("Enter arguments")


if __name__ == "__main__":
    main()


# import sys
# import json
#
# dict = {}
#
# #Считываем входные файлы
#
# with open(sys.argv[1]) as read_file:
#     data_tests = json.load(read_file)
#     #print(data_tests)
# with open(sys.argv[2]) as read_file:
#     data_value = json.load(read_file)
#
# tests = (data_tests['tests'])
# #print(tests)
# values = (data_value['values'])
# #print(tests)
#
#
# for item in values:
#     dict[item['id']] = item['value']
#
# #print(dict)
#
# def fill_values(input_file):
#     for item in range(len(input_file)):
#
#         if input_file[item].get('value') is not None:
#             input_file[item]['value'] = dict[input_file[item]['id']]
#
#         if input_file[item].get('values') is not None:
#             fill_values(input_file[item]['values'])
#
#
# def main():
#     fill_values(tests)
#     with open("report.json", "w") as file:
#         json.dump(tests, file, ensure_ascii=False, indent=2)
#
# if __name__ == "__main__":
#     main()