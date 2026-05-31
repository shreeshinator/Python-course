my_dictionary = { "a": 1, "b": 2, "c": 3 }

for item in my_dictionary.items(): #each item is a tuple of (key, value)
    print(f"Key: {item[0]}, Value: {item[1]}")# indexing the tuple to get key and value

for key, value in my_dictionary.items(): #each item is unpacked into key and value
    print(f"Key: {key}, Value: {value}")

