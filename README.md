
# Formi Chatbot Demo

This project is a Flask-based chatbot backend with a frontend interface.

## Project Structure

```
/frontend       # Contains the frontend files including index.html, CSS, JS, etc.
/api            # Flask API blueprints for state machine, knowledge base, and post call logs
app.py          # Main Flask application entry point
prompts/        # Folder containing prompt templates for the chatbot
```

## Setup & Run

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. Clone the repo
   ```bash
   git clone <your-repo-url>
   cd formi-chatbot
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app
   ```bash
   python app.py
   ```

4. Open your browser at
   ```
   http://localhost:5000
   ```

## Notes

- The frontend files are served from the `frontend` folder.
- The Flask app exposes APIs for chatbot conversation flow under `/api/*`.
- Prompts are stored as templates in the `prompts` folder and loaded dynamically.
- Customize or add prompt templates as needed for your conversational design.

## Troubleshooting

- If the frontend does not load, make sure `index.html` is located inside the `frontend` folder.
- Check that all required Python packages are installed.
- Verify API routes are correctly registered in `app.py`.

## Contact

For any questions or help, contact [Your Name] at [your-email@example.com].
