lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim", "Jim", "Jim"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()  #insert sth in the end of the list
friends.sort()  #sort in alphabetical order

print(friends.index("Jesus"))