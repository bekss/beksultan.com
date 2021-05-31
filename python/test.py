import random
new_list = [9, 10, 8, 8, 8, 1, 7, 5, 10, 12, 8, 4, 3, 13]
first = []
second = []
end_list= []


fr_lst = new_list[:len(new_list)//2]                #Получаем правую часть спика 7 чисел
sec_lst = new_list[len(new_list)//2:]               #Получаем левую часть спика 7 чисел


for a in range(0, len(fr_lst)):                     #Сортировка левой части
    st = min(val for val in fr_lst if val > 0)      #Берем минимальное число из list
    if st not in first:
        first.append(st)
        fr_lst.remove(st)

for a in range(0, len(sec_lst)):                    #Сортировка правой части
    st = min(val for val in sec_lst if val > 0)
    if st not in second:
        second.append(st)
        sec_lst.remove(st)


new_list.clear()
new_list.extend(first)                              #Соединяем оба части в один
new_list.extend(second)
first.clear()
second.clear()

for a in range(0, len(new_list)):                   #Сортировка правой части
    st = min(val for val in new_list if val > 0)
    if st not in first:
        first.append(st)
        new_list.remove(st)

print(first)                                        #Последний итог list


