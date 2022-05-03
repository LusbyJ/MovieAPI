import json
from run import app # Flask instance of the API

def test_index_route():
    response = app.test_client().get('/movies')
    assert response.status_code == 200


    


  



    