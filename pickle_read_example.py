import pickle

f = open("temp1.pkl", "rb")

a = pickle.load(f)

print a

b = pickle.load(f)

print b

