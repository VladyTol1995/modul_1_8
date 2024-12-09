my_dict = {"July":1997, "Vlad":1995, "Brony":2023}
print(my_dict)
print(my_dict.get("Vlad"))
print(my_dict.get("John"))
my_dict.update({"Sofi":2012, "Sam":1967})
print(my_dict)
del my_dict ["July"]
print(my_dict)
my_set = {25, "Apple", False, 766, 25, False, "Orange"}
print(my_set)
my_set.update({"Game Over", 1995})
print(my_set)
my_set.discard(False)
print(my_set)