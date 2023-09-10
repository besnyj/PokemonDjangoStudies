from django.shortcuts import render
import requests as rq


def frontpage(request):
    return render(request, 'frontpage.html')


def pokemonSearch(request):
    pokemonNameOrId = request.POST.get("name").lower()

    pokemon = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonNameOrId}").json()

    pokemonName = pokemon["name"]
    pokemonId = pokemon["id"]
    pokemonHeight = pokemon["height"]
    pokemonWeight = pokemon["weight"]

    pokemonTypes = ""
    pokemonAbilities = ""

    for item in pokemon["types"]:
        pokemonTypes += f"{item['type']['name']}, "

    for item in pokemon["abilities"]:
        pokemonAbilities += f"{item['ability']['name']}, "

    pokemonDict = {
        "name": pokemonName,
        "id": pokemonId,
        "height": pokemonHeight,
        "weight": pokemonWeight,
        "types": pokemonTypes,
        "abilities": pokemonAbilities
    }

    return render(request, 'pokemonDisplay.html', pokemonDict)
