fruits = {"cherry","orange","grapes","pomegranate"}
#fruits.pop()
#fruits.clear()
print(len(fruits))
fruits.add("apple")
print(len(fruits))
print(fruits)

fruits = {"cherry","orange","grapes","pomegranate"}
print("pineapple" in fruits)
#print(fruits.index("grapes"))
#print(fruits.count("cherry"))

#dictionary
capitals = {"USA": "Washington DC",
            "INDIA": "New Delhi",
            "CHINA": "Beijing",
            "Russia": "San Francisco",}
capitals.update({"GERMANY": "Berlin"})
print(capitals)
capitals.pop("Russia")
print(capitals)
print(capitals.get("INDIA"))
print(capitals.get("JAPAN"))

keys = capitals.keys()
print(keys)

for i in keys:
    print(i)

values = capitals.values()
print(values)

for j in capitals.values():
    print(j)

items = capitals.items()
print(items)

for key, value in items:
    print(key, value)
    #print(f"{key}:, {value}")


