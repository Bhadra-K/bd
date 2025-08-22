cart=[]
#add item
n = int(input("Number of items to add: "))
for i in range(n):
    item = input("Enter item to add: ")
    cart.append(item)
print("Cart:", cart)
#remove item
item=input("Enter item to remove : ")
cart.remove(item)
print("Cart:",cart)
#update item
old_item = input("Enter item to update: ")
new_item = input("Enter new item: ")
index=cart.index(old_item)
cart[index]=new_item
print(f"Updated cart:",cart)
#sort cart
cart.sort()
print(f"Sorted Array: ",cart)
#search item
searchitem=input("Enter the item to find: ")
if searchitem in cart:
    index=cart.index(searchitem)
    print(f"{searchitem} found at position {index}")
else :
    print(f"Item not found")
#slice cart
start=int(input("Enter start index:"))
stop=int(input("Enter stop index:"))
step=int(input("Enter step index:"))
slicedcart=cart[start:stop:step]
print(f"Sliced cart: ",slicedcart)