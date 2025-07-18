from flask import Flask, render_template, request, jsonify
from src.search_engine import SearchEngine
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
search_engine = SearchEngine()

# Index sample documents
documents = {
    0: '''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background''',
    1: '''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia''',
    2: '''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain''',
    3: '''Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a presentation about Security presented by Rocky Heckman read his blog its quite good In it he was talking about security algorithms The part that really stuck with me went like this''',
    4: '''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering''',
    5: '''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it''',
    6: '''Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly this sort of question pops up a lot in my referring search term stats Why CAPTCHAs never use the numbers 0 1 5 7 Its a relativity simple question with a reasonably simple answer Its because each of the above numbers are easy to confuse with a letter See the below''',
}
for doc_id, doc in documents.items():
    search_engine.add_document(doc_id, doc)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    results = search_engine.search(query)
    return jsonify({'results': [(r[0], r[1]) for r in results], 'query': query})

@app.route('/voice-search', methods=['POST'])
def voice_search():
    from speech_recognition import Recognizer, AudioFile
    import base64
    recognizer = Recognizer()
    audio_data = request.json.get('audio')
    if audio_data:
        audio_data = base64.b64decode(audio_data.split(',')[1])
        with open('temp.wav', 'wb') as f:
            f.write(audio_data)
        with AudioFile('temp.wav') as source:
            audio = recognizer.record(source)
            query = recognizer.recognize_google(audio)
            results = search_engine.search(query)
            return jsonify({'results': [(r[0], r[1]) for r in results], 'query': query})
    return jsonify({'error': 'No audio data'})

if __name__ == '__main__':
    app.run(debug=True)