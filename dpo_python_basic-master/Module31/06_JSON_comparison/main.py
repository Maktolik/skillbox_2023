import json

with open('json_new.json', 'r') as new_file, \
        open('json_old.json', 'r') as old_file:
    new_data = json.load(new_file)
    old_data = json.load(old_file)


def look_for_mathes(dict_1, dict_2, mathes):
    for key, val in dict_1.items():
        if isinstance(dict_1[key], dict):
            look_for_mathes(dict_1[key], dict_2[key], mathes)
        elif dict_1[key] != dict_2[key] and key in mathes:
            values[key] = dict_1[key]
    return values


values = {}
diff_lst = ["services", "staff", "datetime"]
res = look_for_mathes(new_data, old_data, diff_lst)
print(res)

with open('result.json', 'w') as final:
    json.dump(res, final, indent=4, ensure_ascii=False)