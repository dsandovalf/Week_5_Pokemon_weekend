from flask import render_template, request
import requests
from .forms import SearchForm
from flask_login import login_required
from .import bp as main

@main.route('/')
def index():
    return render_template('index.html.j2')



@main.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    form = SearchForm()
    if request.method == 'POST':
        pokemon = request.form.get('search')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        print(url)
        if response.ok:
            data = response.json()
            all_pokemon=[]
            pokemon_dict={
                "name":data["forms"][0]["name"],
                "ability": data["abilities"][0]["ability"]["name"],
                "base_experience":data["base_experience"],
                "base_hp":data["stats"][0]["base_stat"],
                "base_defense":data["stats"][2]["base_stat"],
                "base_attack":data["stats"][1]["base_stat"],
                "front_shiny":data["sprites"]["front_shiny"],
            }
            all_pokemon.append(pokemon_dict)
            print(all_pokemon)
            return render_template('pokemon.html.j2', pokemons=all_pokemon, form=form)
        else:
            error_string = "The pokemon you entered is not in the Pokedex."
            return render_template('pokemon.html.j2', error = error_string, form=form)
    return render_template('pokemon.html.j2', form=form)