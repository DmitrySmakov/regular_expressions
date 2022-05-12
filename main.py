import re
import csv


def join_(x, y):
    if x == y:
        return x
    else:
        return x+y


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list1 = []
for lst in contacts_list:
    fio = f'{lst[0]} {lst[1]} {lst[2]}'  # print(fio)     # print(fio.split())
    tmp = fio.split()
    if len(tmp) == 2:
        tmp.append('')
    tmp.extend([lst[3], lst[4], lst[5], lst[6]])
    contacts_list1.append(tmp)

contacts_list2 = []
for x in contacts_list1:
    for y in contacts_list1:
        if x != y and x[0] == y[0] and x[1] == y[1] and (x[2] == y[2] or not x[2] or not y[2]):
            tmp = [x[0], x[1], join_(x[2], y[2]), join_(x[3], y[3]), join_(x[4], y[4]), join_(x[5], y[5]),
                   join_(x[6], y[6])]
            break
        else:
            tmp = x
    if tmp not in contacts_list2:
        contacts_list2.append(tmp)
pattern1 = r"(\+7|8)?\s*?\(?(\d+)\)?(\s?|-)(\d{3})(-?|\s?)(\d{2})(-?|\s?)(\d{2})"
sub1 = "+7(\2)\4-\6\8"
pattern2 = r"\s*?\(?(доб\.\s*?(\d+))\)?"
sub2 = " доб.\2"
for i in contacts_list2:
    result = re.sub(pattern1, sub1, i[5])
    result = re.sub(pattern2, sub2, result)
    i[5] = result

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list2)
