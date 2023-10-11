movies = {
    'Film1' : '11:00am',
    'Film2' : '12:00am',
    'Film3' : '1:00pm',
}

print("We are showing the following movie")



for key in movies:
    print(key)
    
movie = input("What movie would you like showtime for?\n")

showtime = movies.get(movie)

print(showtime)
    
    