from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['GET'])
def scrape():
    website = request.args.get('website')
    if 'youtube.com' in website:
        data = scrape_youtube(website)
    elif 'amazon.com' in website:
        data = scrape_amazon(website)
    else:
        data = 'Unsupported website'

    return render_template('index.html', data=data)

def scrape_youtube(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.content, 'html.parser')
    

    video_title = soup.title.text

    return 'Video title: ' + video_title

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)