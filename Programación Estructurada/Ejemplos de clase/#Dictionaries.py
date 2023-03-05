#Dictionaries
dict_colors={"red":"rojo", "blue":"azul", "yellow":"amarillo"}
print(dict_colors)

print(dict_colors["red"])

value = dict_colors["yellow"]
print(value)

dict_colors["black"]="negro"
print(dict_colors)

del(dict_colors["black"])
print(dict_colors)

dict_colors.pop("yellow")

print(dict_colors)

for color in dict_colors:
    print(color)

for key, value in dict_colors.items():
    print(key, value)
