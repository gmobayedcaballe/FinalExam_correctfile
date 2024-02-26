# Empty list
k = []
# We can append stuff into the list
k.append("3")
k.append("4")

print(k) # k changes

# String
a = "dog eats meat"
a.replace("dog", "cat")
print(a) # a remains unchanged
b = a.replace("dog","cat")
print(b) # if we want the edited content of a we must save it into another object