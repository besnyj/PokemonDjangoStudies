
import requests as rq




def pokemonSearch(request):
    pokemonNameOrId = request

    pokemon = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonNameOrId}").json()

    pokemonName = pokemon["name"]
    pokemonId = pokemon["id"]
    pokemonHeight = pokemon["height"]
    pokemonWeight = pokemon["weight"]

    pokemonTypes = ""
    pokemonAbilities = ""

    for item in pokemon["types"]:
        pokemonTypes += f"{item['type']['name']} "

    for item in pokemon["abilities"]:
        pokemonAbilities += f"{item['ability']['name']} "

    pokemonDict = {
        "name": pokemonName,
        "id": pokemonId,
        "height": pokemonHeight,
        "weight": pokemonWeight,
        "types": pokemonTypes,
        "abilities": pokemonAbilities
    }

    return pokemonDict

print(pokemonSearch("pikachu"))