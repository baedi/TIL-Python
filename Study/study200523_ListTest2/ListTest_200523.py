#coding utf-8
import TestClass_List


### Variable
list_var = []


### Function
def ListvarState():
    print("List : " + str(list_var))
    print("Length : %d\n" % (len(list_var)))

### Start


ListvarState()

list_var.append(1)
list_var.append(5)
list_var.append(7)
ListvarState()
print("----------\n")

list_var.insert(0, TestClass_List.TestClass_List(10, 'Apple'))
print(list_var[0].GetName())
print(list_var[0].GetNumber())
ListvarState()
list_var.clear()
print("----------\n")

list_var.extend([10, 20, 30, 40, 50])
ListvarState()
print("----------\n")

list_var2 = list_var.copy()
ListvarState()
print(str(list_var2) + "\n")
print("----------\n")

list_var.remove(20)
list_var.remove(50)
ListvarState()
print("----------\n")

print(list_var.pop())
print(list_var.pop())
ListvarState()

