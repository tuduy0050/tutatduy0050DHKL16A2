# Tìm kiếm thú trong vườn thú
List_of_animals = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animals:",List_of_animals)
print("Number of animals:",len(List_of_animals))
animals = input("I Want To Find: ")
find = animals in List_of_animals
if find == True:
    print("Thers is",animals,"in list of animals")
else:
    print("Thers is",animals,"is not in list of animals")
