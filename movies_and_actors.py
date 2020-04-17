import codecs

movie_1 = ''
movie_2 = ''
actor_1 = ''
actor_2 = ''
action_movies = ''
action_actors = ''
movie_or_actor = input('What do you choose? \n1) Movies \n2) Actors\n')
print()
if movie_or_actor == '1' or movie_or_actor == 'Movies':
    print('Enter 2 movies:')
    movie_1 = input()
    movie_2 = input()
    print()
    action_movies = input('Choose an action: \n1) Determine the total cast of the actors who '
          'starred in at least one of these two films. \n'
          '2) Identify the actors who starred in both the first and second films.\n'
          '3) Identify actors involved in shooting the first film but not in shooting the second.\n')

elif movie_or_actor == '2' or movie_or_actor == 'Actors':
    print('Enter 2 actors:')
    actor_1 = input()
    actor_2 = input()
    print()
    action_actors = input('Choose an action: \n1) Determine the titles of films in '
                   'which at least one of the actors was acting. \n'
                   '2) Determine the titles of films in which both actors were filmed.\n'
                   '3) Identify the names of films in which the first actor was shot, '
                   'but did not participate in the shooting of the second.\n')


list_of_lines = []
with codecs.open('films.txt', 'r', encoding='utf-8') as films:
    for string in films.readlines():
        list_of_lines.append(string.strip())

dict_of_movies = {}
for i in list_of_lines:
    film = i[:i.find(':')]
    actors = i[i.find(':') + 1:]
    actors = actors.split(',')
    actors = set(actors)
    dict_of_movies[film] = actors


list_of_actors = []
set_of_movies = set()
for key, value in dict_of_movies.items():
    for v in value:
        dict_actors = {}
        set_of_movies.add(key)
        dict_actors[v] = set_of_movies
        list_of_actors.append(dict_actors)

dict_of_actors = {}
for dict in list_of_actors:
    for key, val in dict.items():
        for i in val:
            if key in dict_of_movies[i]:
                set_movies = set()
                set_movies.add(i)
                dict_of_actors[key] = set_movies


first_actors_set = ''
second_actors_set = ''
for key in dict_of_movies.keys():
    if movie_1 in dict_of_movies and movie_2 in dict_of_movies:
        first_actors_set = dict_of_movies[movie_1]
        second_actors_set = dict_of_movies[movie_2]

first_movie_set = ''
second_movie_set = ''
for key in dict_of_actors.keys():
    if actor_1 in dict_of_actors and actor_2 in dict_of_actors:
        first_movie_set = dict_of_actors[actor_1]
        second_movie_set = dict_of_actors[actor_2]

if action_movies == '1':
    print(first_actors_set | second_actors_set)
elif action_movies == '2':
    print(first_actors_set & second_actors_set)
elif action_movies == '3':
    print(first_actors_set - second_actors_set)

if action_actors == '1':
    print(first_movie_set | second_movie_set)
elif action_actors == '2':
    print(first_movie_set & second_movie_set)
elif action_actors == '3':
    print(first_movie_set - second_movie_set)