from flask import Flask, request, render_template
import requests
import os

testing = False
if testing:
    route = 'http://127.0.0.1:5001/'
else:
    route = os.getenv('API_URL')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/npc', methods=['GET','POST'])
def create_npc():
    race = request.form.get('race')
    gender = request.form.get('gender')
    backstory = request.form.get('backstory')

    response = requests.get(route + f"/npc?race={race}&gender={gender}&backstory={backstory}")

    return render_template('npc_created.html', response=response.json())

@app.route('/item', methods=['GET','POST'])
def create_item():
    treasure_type = request.form.get('type')
    description_lod = request.form.get('lod')

    response = requests.get(route + f"/item?type={treasure_type}&lod={description_lod}")

    return render_template('item_created.html', response=response.json())

@app.route('/spells', methods=['GET','POST'])
def get_spells():
    spell = request.args.get('spell_name')
    level = request.form.get('spell_level')
    spell_class = request.form.get('spell_class')

    response = requests.get(route + f"/spells?spell_name={spell}&spell_level={level}&spell_classes={spell_class}")

    if spell:
        return render_template('spell.html', response=response.json())
    else:
        return render_template('spells.html', response=response.json())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
