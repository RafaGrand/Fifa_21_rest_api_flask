from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db_script import populate_database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:password@localhost/football_team'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    position = db.Column(db.String(2))
    nation = db.Column(db.String(50))
    club = db.Column(db.String(50))

    def __init__(self, name, position, nation, club):
        self.name = name
        self.position = position
        self.nation = nation
        self.club = club

#Creamos Tabla
db.create_all()

#Poblar database con resultados API Fifa 21  
populate_database()

class TeamSchema(ma.Schema):
    class Meta:
        fields = ('name', 'position', 'nation', 'club')

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

class PostSchema(ma.Schema):
    class Meta:
        fields = ('name','position','nation')
        model = Team

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

#Metodo POST
@app.route('/api/v1/team', endpoint="team", methods=['POST'])
def create_team():
    content = request.get_json()
    team = content["club"]
    all_tasks = Team.query.filter(Team.club.ilike('%'+team+'%'))

    result = posts_schema.dump(all_tasks)
    return jsonify(result)

#Metodo GET
@app.route('/api/v1/players', endpoint="search", methods=['GET'])
def list_players():
    content = request.get_json()
    name = content["name"]
    players = Team.query.filter(Team.name.ilike('%'+name+'%')).order_by(Team.name)

    result = teams_schema.dump(players)
    return jsonify(result)

#protegemos api con X-Content-Type-Options
@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


if __name__ == "__main__":
    app.run(debug=True)