#!/usr/bin/env python
import json
from flask import Flask, jsonify, request
import os

#create instance of Flask app
app = Flask(__name__)

#defualt  
@app.route('/')
def hello():
    text = "Hello World!"  
    return text

@app.route("/recipes",methods=['GET','POST'])
def get_names():
    json_url = os.path.join("data","data.json")
    #Post new recipe
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        new_recipe = {  "name":name,
                        "ingredients":ingredients,
                        "instructions":instructions
                        }
        with open(json_url, "r+") as file:
            data_json = json.load(file)
            data_json["recipes"].append(new_recipe)
            file.seek(0)
            json.dump(data_json, file)
        return "Successfully added a recipe"
        
    #Get data if not Posting
    data_json = json.load(open(json_url))
    data = data_json["recipes"]
    recipe_names = [x['name'] for x in data]
    return jsonify(recipe_names)

#Get recipe ingredients and number of steps
@app.route("/recipes/details/<name>",methods=['GET'])
def get_ingredients(name):
    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))
    data = data_json["recipes"]
    details = [(x['ingredients'], len(x['instructions'])) for x in data if x['name']==name]
    return jsonify(details)

if __name__ == "__main__":
    app.run(debug=True)
