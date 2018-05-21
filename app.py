import pycountry
from flask import Flask, render_template
from pip._vendor import requests

app = Flask(__name__)


@app.route('/')
def channels():
    country_channes = {}
    channels = requests.get('http://playapi.mtgx.tv/v3/channels?limit=80')

    for channel in channels.json()['_embedded']['channels']:
        if channel['country'] == 'vs':
            channel['country'] = 'dk'

        print(pycountry.countries.get(alpha_2=channel['country'].upper()).name)
        if channel['country'] not in country_channes:
            country_channes[channel['country']] = []

        country_channes[channel['country']].append(channel)

    return render_template('channels.html', country_channes=country_channes, pycountry=pycountry)

@app.route('/formats/<int:channel_id>')
def formats(channel_id):
    pass

if __name__ == '__main__':
    app.run()
