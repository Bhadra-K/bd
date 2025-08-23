list=['apple','mango','lemon','berry','kiwi']
# print(list)    #whole list
# print(list[0])   #1st item
# print(list[1:3])   #slice
# list.append('orange')    #add item
# print(list)
# if "lemon" in list:      #search
#     print("lemon found")
# else:
#     print("Item not found")
# list.remove("mango")
# print(list)
# # or print(list.remove("mango"),list)
# #loops
# while True:
#     print("\nMENU","\n1.Add","\n2.View","\n3.Exit")
#     choice=input("Enter choice:")
#     if choice=='1':
#        item=input("enter item:")
#        list.append(item)
#        print("Item added")
#     elif choice=='2':
#         print(list)
#     else:
#         print("exited!!")
#         break
# for i in list:
#     print(i)

# for i,j in enumerate(list,start=1):   #by default start=0
#     print(i,j)                        #prints value with index

# item=input("Enter any item from list to unlock discount:")
# if item=='apple':
#     price=50
#     sale=40
#     discount=price - sale
#     np=(discount/price)*100
#     print("You unlocked 50% discount lucky pal :)")
#     print("New price=",np,"Hurray!!!") 
# elif item=='mango':
#     price=60
#     sale=30
#     discount=price - sale
#     np=(discount/price)*100
#     print("You unlocked 50% discount lucky pal :)")
#     print("New price=",np,"Hurray!!!") 

fruits=[]
while True:
    print("\nMENU","\n1.Add","\n2.View","\n3.Update","\nExit")
    choice=input("Enter choice:")
    if choice=='1':
       name=input("enter name of fruit:")
       price=float(input("enter price of fruit:"))
       fruits.append({"name":name,"price":price})
       print(f"Added: {name} with price {price}")
    elif choice=='2':
       print(fruits)
    elif choice == '3':
         old = input("Enter old fruit name: ")
         new = input("Enter new fruit name: ")
         found = False
         for fruit in fruits:
             if fruit["name"] == old:
                  fruit["name"] = new
                  found = True
                  print("Updated fruits!")
                  break
         if not found:
            print("Fruit not found in the list.")
    else:
       break
    
   
   