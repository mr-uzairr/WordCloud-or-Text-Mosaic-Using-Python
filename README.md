# WordCloud or Text Mosaic Using Python

This Python project generates a word cloud from Wikipedia content based on user input. The word cloud is shaped using a background image and removes common words for better visualization.

## Features
- Fetches text from Wikipedia.
- Generates a word cloud using a custom background image.
- Saves the generated word cloud as an image (`sample.png`).
- Removes common words using `STOPWORDS`.

## Installation
### Prerequisites
Ensure you have Python installed along with the required libraries.

### Setup
1. Clone this repository:

   git clone https://github.com/yourusername/WordCloud-or-Text-Mosaic-Using-Python.git

2. Navigate to the project folder:

   cd WordCloud-or-Text-Mosaic-Using-Python

3. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux

   .venv\Scripts\activate      # On Windows

4. Install dependencies:
   pip install -r requirements.txt


## Usage
1. Run the script:
   python word.py

2. Enter a search term for Wikipedia content.
3. The script fetches the content and generates a word cloud.
4. The output image `sample.png` is saved in the project directory.

## Requirements
Install required libraries:
pip install numpy pillow wikipedia-api wordcloud


## Example
- Input: `Python (programming language)`
- Output: Word cloud shaped by `Image.jpeg`, saved as `sample.png`.

## Troubleshooting
- Ensure `Image.jpeg` exists in the project directory.
- If Wikipedia content retrieval fails, try another search term.
- If `ImportError` occurs, ensure all dependencies are installed.
