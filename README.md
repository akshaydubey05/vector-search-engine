
# Vector Space Search Engine

## Overview

The Vector Space Search Engine is a modular and intelligent search engine built in Python that supports advanced relevance scoring, query refinement, and voice-activated search. It combines vector space models, natural language processing, and web technologies to provide an efficient and interactive text search experience.

## Features

- **Vector Space Model**: Implements cosine similarity to rank documents based on query relevance.
- **Machine Learning Scoring**: Uses a linear regression model to refine the ranking of search results.
- **AI Query Refinement**: Enhances search accuracy using a distilled BERT model to expand or correct user queries.
- **Voice Search**: Enables hands-free search through voice input using the Web Speech API and Python's SpeechRecognition.
- **Flask Web Interface**: Interactive browser-based interface for entering or speaking search queries.
- **Command-Line Interface (CLI)**: Lightweight terminal-based version of the engine for quick testing.
- **Unit Testing**: Ensures reliability through Python’s built-in unittest framework.
- **Modular Design**: Clean separation of concerns through well-structured modules.

## Technologies Used

- **Python 3.8+**
- **Flask** – Web server and routing
- **scikit-learn** – Machine learning model for relevance
- **transformers (Hugging Face)** – NLP model for query refinement
- **SpeechRecognition** – Capturing and converting voice to text
- **PyAudio** – Microphone access and audio input
- **HTML/CSS/JavaScript** – Frontend for Flask app

## Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Chrome browser (for voice support)
- Microphone access
- Internet connection

### Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/vector-search-engine.git
cd vector-search-engine

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

**Note (Windows):** If PyAudio fails to install, use a prebuilt `.whl` from:  
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  
Then run:
```bash
pip install PyAudio‑0.2.14‑cp312‑cp312‑win_amd64.whl
```

## Usage

### CLI Interface

```bash
# Activate the environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run the CLI app
python main.py
```

### Web Interface

```bash
# Activate environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run the web app
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

To use voice search, click "Start Voice Search", allow microphone permission, and speak your query.

## Testing

```bash
python -m unittest discover tests
```

You should see all tests pass indicating system reliability.

## Deployment

To deploy the application on Heroku:

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create vector-search-engine

# Create a Procfile with:
# web: python app.py

# Push to Heroku
git push heroku main

# Open in browser
heroku open
```

## Troubleshooting

- **TemplateNotFound**: Ensure `index.html` is in the `/templates` folder.
- **Port Issues**: Free port 5000 using `netstat` and `taskkill` on Windows.
- **PyAudio install errors**: Use wheel files if installing fails with pip.

## Project Structure

```
vector-search-engine/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── src/
│   ├── __init__.py
│   ├── indexer.py
│   ├── search_engine.py
│   └── vector_compare.py
├── tests/
│   ├── __init__.py
│   └── test_vector_compare.py
```

## Author

**Akshay Kumar Dubey**  
GitHub: [https://github.com/akshaydubey05](https://github.com/akshaydubey05)

## License

This project is licensed under the MIT License.
