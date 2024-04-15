# Four different ways to create the same dictionary holding names of MLB teams

# First: Use the dictionary literal
teams1 = {'Seattle': 'Mariners', 'Boston': 'Red Sox',
          'Minnesota': 'Twins', 'Milwaukee': 'Brewers'}
print("teams1: ")
print(teams1)
print()

# Second: Start with an empty dictionary, and then build it incrementally
teams2 = {}
teams2['Seattle'] = 'Mariners'
teams2['Boston'] = 'Red Sox'
teams2['Minnesota'] = 'Twins'
teams2['Milwaukee'] = 'Brewers'
print("teams2: ")
print(teams2)
print()

# Third: Use the dict constructor with keyword arguments
teams3 = dict(Boston='Red Sox', Minnesota='Twins', Milwaukee='Brewers',
              Seattle='Mariners')
print("teams3: ")
print(teams3)
print()

# Fourth: Use a list of lists or tuple of lists or tuple of tuples alongwith the dict constructor
teamsList = [['Seattle', 'Mariners'], ['Boston', 'Red Sox'],
             ['Minnesota', 'Twins'], ['Milwaukee', 'Brewers']]
teams4 = dict(teamsList)
print("teams4: ")
print(teams4)
print()


def displaySortedKeys(d):
    "Function to display elements of a dictionary in ascending order of keys"
    print("Displaying with ascending order of keys")
    # Get a list of key values by converting the keys() view object to a list
    keys = list(d.keys())

    # Sort the keys list
    keys.sort()

    # Use the sorted keys list to display elements of the dictionary in ascending key order
    for k in keys:
        print("{} : {}".format(k, d[k]))
    print()


def displaySortedKeys2(d):
    "Another function to display elements of a dictionary in ascending order of keys"
    print("Displaying with ascending order of keys 2")
    # Get a list of key values by converting the keys() view object to a list
    items = list(d.items())

    # Sort the items list - it will be based on the key values
    items.sort()

    # Use the sorted items list to display elements of the dictionary in ascending key order
    for k, v in items:
        print("{} : {}".format(k, v))
    print()


def displaySortedKeys3(d):
    "Yet another function to display elements of a dictionary in ascending order of keys"
    print("Displaying with ascending order of keys 3")
    for k in sorted(d):
        print(f"{k} : {d[k]}")
    print()


def displaySortedValues(d):
    "Function to display elements of a dictionary in ascending order of values"
    print("Displaying with ascending order of values")

    items = []

    for k, v in d.items():
        items.append((v, k))
    items.sort()
    for v, k in items:
        print("{} : {}".format(k, v))
    print()


def displaySortedValues2(d):
    "Another function to display elements of a dictionary in ascending order of values"
    print("Displaying with ascending order of values 2")
    for k in sorted(d, key=lambda x: d[x]):
        print("{} : {}".format(k, d[k]))
    print()


# displaySortedKeys(teams1)
displaySortedKeys3(teams3)
displaySortedKeys2(teams2)
# displaySortedValues(teams1)
displaySortedValues2(teams1)