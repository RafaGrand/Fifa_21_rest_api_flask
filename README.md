# Fifa_21_rest_api_flask
A simple Rest API

Just export the .sql to your local machine and replace your SQL password in the DB connection

Could initialize the venv with the dependencies or install packages with requirements.txt 

This microservice read data from Fifa 21 API and store it in MySQL db.

The service expose a rest api with custom endpoints and HTML methods.

#Examples:

#POST api/v1/team
Request example:

{
"club" : "real madrid",
"page" : 1
}

Response:

{name: "Marcelo", "position": "LB", "nation" : "Brazil"},
...

#GET api/v1/players

Request example:
{
"name" : "crist",
"page" : 1
}

Response:
{"name": "Cristiano Ronaldo", "position": "ST", "nation": "Portugal", "team" : "Juventus"},
...

#Run:
python /src/app.py
