import ast

#read the contents from the txt file.
f = open("10.txt", 'r')
dictionaries = f.read()
f.close()

#split the contents of the txt file by line
dictionaries = dictionaries.split("\n")

#we're going to need this, so we can find the max depth
max_depth = -1

#for every line that we find
for dictionary in dictionaries:
    #we try to convert it to a dictionary
    try:
        dictionary = ast.literal_eval(dictionary)

        #and then we find its depth
        depth = 0
        for item in dictionary.values():
            if type(item) == list or type(item) == dict:
                depth += 1
        
        #and lastly we apply simple find-max algorithm, to find the max depth
        if depth > max_depth:
            max_depth = depth
    except Exception as e:
        print("Found an invalid dictionary. Error:", e)

print("The dictionary with the biggest depth, has a depth size of:", max_depth)