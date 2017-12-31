# Treehouse assignment
# a list to hold items
shopping_list=[]
print("Enter your items to enter")
print("Enter DEL to delete last entered item")
print("Enter DONE to stop adding items")
print("Enter SHOW to see current shopping list")

while True:
    new_item = input(">")
    if new_item.strip() == "DEL":
        if len(shopping_list)>0:
            del shopping_list[-1]
        else:
            print("No item to delete!")
    elif new_item.strip() == "DONE":
        break
    elif new_item.strip() == "SHOW":
        print("Shopping List till now :")
        count=1
        for i in shopping_list:
            print(str(count)+"."+shopping_list[count-1])
            count+=1
    else:
        shopping_list.append(new_item)


