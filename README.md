# Word Finder

## Overview
This is a Python program that allows users to search for five-letter words based on specific conditions, such as required letters, excluded letters, specific starting/ending letters, and letters at specific positions.

## Features
- Filter words that must contain specific letters.
- Exclude words containing certain letters.
- Find words that start or end with a particular letter.
- Search for words with specific letters at exact positions.
- Interactive search interface for user input.

## Requirements
This project requires the following Python packages:

```
nltk==3.9.1
pandas==2.2.3
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/word-finder.git
   cd word-finder
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Download NLTK word corpus:
   ```python
   import nltk
   nltk.download('words')
   ```

## Usage
Run the script to start an interactive search session:
```sh
python main.py
```
Follow the on-screen prompts to search for words based on your criteria.

## Example Search
- Find words that must contain "A" and "S", must not contain "R" and "T", and start with "P":
  ```
  Enter letters that must be contained (comma-separated, e.g., 'S,A'): A,S
  Enter letters that must not be contained (comma-separated, e.g., 'R,T'): R,T
  Enter the prefix that the words must start with (leave blank if none): P
  Enter the suffix that the words must end with (leave blank if none):
  ```

## Contributing
If you’d like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

