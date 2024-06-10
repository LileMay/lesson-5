immutable_var = (1, 2, "name", 2.2, True)
print(immutable_var)
#immutable_var[3] = 10  кортеж не поддерживает обращение по элементам.
#print(immutable_var)
mutable_list = [1, 2, "name", 2.2, True]
print(mutable_list)
mutable_list[1] = "last"
print(mutable_list)