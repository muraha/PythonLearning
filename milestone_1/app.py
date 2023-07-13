# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def find_movie(movie1=''):
    res = list(filter(
        lambda m: (movie1.lower() in m['title'].lower()),
        movies
    ))
    # is_in = [movie for movie in movies if movie1.lower() in movie['title'].lower()]
    print(res)

def list_movies():
    res = [movie['title'] for movie in movies]
    print(res)


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie()
    elif selection == "l":
        list_movies()
    elif selection == "f":
        prompt = input('What name are we looking for?: ')
        find_movie(prompt)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!a
