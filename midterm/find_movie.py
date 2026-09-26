movies = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]

print (" ------------ FIND MOVIE ------------ ")
print ()

find = input ("Enter movie title: ")

print ()

if find in movies:
  print("Movie found!")

else:
  print("Movie not found!")
  
print ()