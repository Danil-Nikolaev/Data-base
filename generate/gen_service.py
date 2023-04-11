import json
title_list = open("title_service.txt", "r").readlines()
description_list = open("description.txt", "r").readlines()
dict_service = {}
for i in range(100):
    dict_service[title_list[i]] = description_list[i]

with open("service.json", "w") as write_file:
    json.dump(dict_service, write_file, ensure_ascii=False, indent=4)
