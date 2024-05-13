
# List
my_list = ["orange", "apple", "banana", "strawberry", "mango"]
print("List:", my_list)
print("First elem:", my_list[0])
print("Last elem:", my_list[-1])
print("Sublist:", my_list[2:4])
my_list[2] = "grapefruit"
print("Modified list:", my_list)

# Dictionary
my_dict = {"orange": "апельсин",
           "apple": "яблоко",
           "banana": "банан",
           "strawberry": "клубника",
           "mango": "манго"}
print("Dictionary: ", my_dict)
print("Translation: ", my_dict.get("apple"))
#при присвоении несуществующему ключу создается новая пара
my_dict["pineaapple"] = "ананас"
print("Modified dictionary: ", my_dict)
