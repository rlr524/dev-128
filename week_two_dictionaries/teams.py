teams = {
    "Seattle": "Mariners",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers"
}
print(teams)

teams_two = {
    "Seattle": "Mariners",
    "Boston": "Red Sox"
}

teams_two["San Diego"] = "Padres"
print(teams_two)


teams_three = [["Los Angeles", "Dodgers"], ["Houston", "Astros"], ["New York", "Mets"]]
teams_three_new = dict(teams_three)
print(teams_three_new)


teams_four = dict(SF="Giants", NYA="Yankees")
print(teams_four)

def add(numb_one: int, numb_two: int):
    return numb_one + numb_two


result = add(23.5, 21)
print(result)
