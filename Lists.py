#list = used to store multiple values in a single variable

food = ["pizza","hamburger","hotdog", "lasagna","rice and beans"]

food[2] = "sushi"

#food.append("chicken") #insert item in the list
#food.remove(food[0]) #remove item
#food.pop() #remove the last item
#food.insert(0,"cake") #intert intem
#food.sort() #sort list in alphabetic order
#food.clear() #clear the list

for i in food:
    print(i)


#2d List = list of lists

drinks = ["beer","soda","wine"]
dinner = ["hamburger","pizza","lasagna"]
dessert = ["pudding","cake"]

food = [drinks,dinner,dessert]

#food = [["beer","soda","wine"],["hamburger","pizza","lasagna"]]

print(food)