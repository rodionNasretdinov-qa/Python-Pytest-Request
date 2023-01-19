import requests
import json

token = 'c30bc35eae61d215c43837aaaeb56ede'

respornse = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "name": "Roaring Moon",
    "photo": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/1005.png"
})

print(respornse.text)

pokemon_id = respornse.json()['id']


respornse_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Ревущая Луна",
    "photo": ""
})

print(respornse_change.text)


pokemon_id = respornse.json()['id']

respornse = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers= {'Content-Type' : 'application/json', 'trainer_token': token},
json= {
    "pokemon_id": pokemon_id,
    "name": "Ревущая Луна",
    "photo": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/1005.png"
})

print(respornse.text)