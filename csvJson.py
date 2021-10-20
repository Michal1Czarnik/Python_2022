#!/usr/bin/python3

import json

print('Plik JSON zawierajacy recenzje o filmach')

f = open('data.json')
movies = json.load(f)
print("Obecna zawartosc: ")
for i in movies.items(): 
    print(i)

print('\nChcesz dodac nowa recenzje, czy usunac istniejaca? (dodac/usunac)')
decision = input()
if(decision == 'dodac'):
    print('\nPodaj nazwe rekordu jaki chcesz dodac')
    nick = input()
    print('Podaj tytul filmu')
    title = input()
    print('Podaj date premiery')
    premiere = input()
    print('Podaj opinie')
    opinion = input()
    movies[str(nick)] = {'title': str(title), 'premiere': str(premiere), 'opinion': str(opinion)}
elif(decision == 'usunac'):
    print('Podaj nazwe rekordu jaki chcesz usunac')
    nick = input()
    movies.pop(str(nick))
else:
    print("Nieznana komenda")

print("\nZawartosc po modyfikacjach: ")
for i in movies.items(): 
    print(i)
with open('data.json', 'w') as f:
    json.dump(movies, f)