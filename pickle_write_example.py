import pickle

#take data structures, serialize into byte streams, save then in a file, and retrieve later

#create the pickle file for writing
f = open("temp1.pkl", "wb")
# create a list for example
a = range(10)
# add something to the list

a.append('This is Radio Clash')

# insert in pickle file
pickle.dump(a, f)

#create another list. a splice of the original in this case

b = a[5:]

#write to file again
pickle.dump(b, f)

# close the file
f.close()

