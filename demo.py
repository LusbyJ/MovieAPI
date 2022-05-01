#!/usr/bin/env python
import json
from flask import Flask, jsonify, request
import os

#create instance of Flask app
app = Flask(__name__)

#defualt  
@app.route('/')
def hello():
    text = "This is a movie api!"  
    return text

@app.route("/movies",methods=['GET','POST'])
def get_names():
    json_url = os.path.join("data","data.json")
    #Post new recipe
    if request.method == 'POST':
        title = request.form['title']
        cast = request.form['cast']
        tags = request.form['tags']
        runtime = request.form['runtime']
        format = request.form['format']
        new_movie = {  "title":title,
                        "cast":cast,
                        "tags":tags,
                        "runtime":runtime,
                        "fornat":format
                        }
        with open(json_url, "r+") as file:
            data_json = json.load(file)
            data_json["recipes"].append(new_movie)
            file.seek(0)
            json.dump(data_json, file)
        return "Successfully added a new movie"
        
    #Get data if not Posting
    data_json = json.load(open(json_url))
    data = data_json["movies"]
    movie_names = [x['title'] for x in data]
    return {"Movies" : movie_names}

#Get movie details from movie with specified title
@app.route("/movies/details/<title>",methods=['GET'])
def get_movies(title):
    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))
    data = data_json["movies"]
    for x in data:
        if x['title'] == title: 
            details = {
                "cast": x.get("cast"),
                "tags": x.get("tags"),
                "runtime" : x.get("runtime"),
                "format" : x.get("format")
            }
    return {"Details" : details}

if __name__ == "__main__":
    app.run(debug=True)
