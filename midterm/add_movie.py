movies = ["Movie 01", "Movie 02", "Movie 03"]

title = input ("Enter movie title: ")
director = input ("Enter director: ")
status = input ("Enter status: ")

movies.append(title)

print ()
print("Movie added successfully.")
print ()

for x in movies:
    print(x)