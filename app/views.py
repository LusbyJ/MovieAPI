from app import app

from flask import request

from flask import render_template

import json, os


#defualt  
@app.route("/")
def home():  
    return render_template("home.html")

@app.route("/movies",methods=['GET','POST'])
def get_names():
    json_url = os.path.join("data","data.json")
    #Post new movie
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

# Get movie details from movie with specified title
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

# Get movies with durations less than specified query duration
#example - '/query?duration=120' will get movies less than 120 minutes long
@app.route("/query")
def query():
    args = request.args
    if "duration" in args:
        duration = args.get("duration")

    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))
    data = data_json["movies"]
    details = {}

    for x in data:
        runtime = x.get("runtime")

        if int(runtime) <= int(duration):
            details[x.get("title")] = x.get("runtime")
                   
    return {"Movies" : details}
    

   



