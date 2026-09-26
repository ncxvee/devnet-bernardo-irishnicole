movies = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]

print (" --------------- REMOVE MOVIE --------------- ")
print ()

remove = input ("Remove Movie Title: ")

movies.remove(remove)

print ()
print("Movie removed successfully.")
print ()

for x in movies:
    print(x)