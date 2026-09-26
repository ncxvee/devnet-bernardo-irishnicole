movies = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]

print (" --------------- ADD MOVIE --------------- ")
print ()

title = input ("Enter movie title: ")
director = input ("Enter director: ")
status = input ("Enter status: ")

movies.append(title)

print ()
print("Movie added successfully.")
print ()

for x in movies:
    print(x)
