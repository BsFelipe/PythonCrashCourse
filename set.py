# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("pan")
#utensils.remove("knife")
#utensils.clear()
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

#for x in dinner_table:
#    print(x)