# lists
my_list =[]
# this
values_to_add =[10,20,30,40]

for i in values_to_add:
    my_list.append(i)
print(my_list)
# or this

# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# my_list.append(40)

# inserting to the second value
my_list[1]=15
print(my_list)

# extending another list

another_list =[50, 60, 70]
# for i in another_list:
#     my_list.append(i)
#
my_list.extend(another_list)
print(my_list)

# remove the last element
my_list.pop() # pop removes last index by default



my_list.sort(reverse=False)
print(my_list)


