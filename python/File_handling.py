f = open("cities.txt","r") 
print(f.read()) 
f.close()

#Sort cities
f = open("cities.txt","r") 
k = f.readlines() 
k.sort()
f.close()

#Move the sorting in the different file
f = open("sorted_cities.txt","a") 
f.writelines(k)
f.close()

#Open that file
f = open("sorted_cities.txt","r") print(f.read())

#Reverse Sorting
f = open("cities.txt","r") 
k = f.readlines() 
k.sort(reverse = "true") 
f.close()

f = open("desc_cities.txt","a") 
f.writelines(k)
f.close()
f = open("desc_cities.txt","r") 
print(f.read())
