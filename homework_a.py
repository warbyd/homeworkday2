#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.insert(0, "Glasgow Queen St")

stops.append("Edinburgh Waverly")

stops.insert(4, "Polmont")

# index = stops.index("Linlithgow")
# print('The index of Linlithgow:', index)

stops.remove('Livingston')

stops.pop(2)

# index = stops.index("Cumbernauld")
# print('The index of Cumbernauld:', index)

# print(stops)

# print(len(stops))

stops.sort()
# print(stops)

stops.reverse()
# print(stops)

for x in stops:
    print(x)



