#slicing = in py is possible create a substring, slicing another string
# indexing[] or slice()
#[start:stop:step]


#name = 'Felipe Belo'

#firt_name = name[0:6]
#last_name = name[7:11]
#crazy_name = name[::2]#use the step to define the pass of slice
#reversed_name = name[::-1]

#print(firt_name)
#print(last_name)
#print(crazy_name)
#print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])