
Vector Space Search Engine
==========================

A state-of-the-art search engine implemented in Python, leveraging a vector space model enhanced with machine learning for relevance scoring, voice-activated search, and AI-powered query refinement.

Features
--------
- Vector space model with cosine similarity
- AI-powered query refinement using BERT
- Relevance scoring using Linear Regression
- Voice-activated search using Web Speech API + SpeechRecognition
- Flask-based web interface
- Unit-tested modules
- Modular and scalable

Project Structure
-----------------
vector-search-engine/
├── app.py                  # Flask app
├── main.py                 # CLI interface
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── templates/
│   └── index.html          # Web UI template
├── src/
│   ├── __init__.py
│   ├── indexer.py
│   ├── search_engine.py
│   └── vector_compare.py
├── tests/
│   ├── __init__.py
│   └── test_vector_compare.py

Installation Steps
------------------
1. Clone the repository:
   git clone https://github.com/yourusername/vector-search-engine.git
   cd vector-search-engine

2. Create and activate virtual environment:
   python -m venv venv

   - On Windows:
     venv\Scripts\activate

   - On macOS/Linux:
     source venv/bin/activate

3. Upgrade pip:
   pip install --upgrade pip

4. Install dependencies:
   pip install -r requirements.txt

5. Install PyAudio manually if needed (Windows only):
   pip install PyAudio‑0.2.14‑cp312‑cp312‑win_amd64.whl

Usage - CLI
-----------
Activate the virtual environment and run:
   python main.py

Example:
   Enter Search Term: captcha

Usage - Web
-----------
Activate the environment and run:
   python app.py

Open in browser:
   http://127.0.0.1:5000

To use voice search, click the “Start Voice Search” button and allow microphone access.

Testing
-------
Run unit tests:
   python -m unittest discover tests

Troubleshooting
---------------
- TemplateNotFound: Ensure index.html is in templates/
- PyAudio error: Use .whl for Windows
- Voice not working: Check browser mic permissions
- Port 5000 busy: Use netstat/taskkill to free port

Deployment
----------
To deploy on Heroku:
   heroku login
   heroku create vector-search-engine
   Add a Procfile: web: python app.py
   git push heroku main
   heroku open

Author
------
Akshay Kumar Dubey
GitHub: https://github.com/yourusername
