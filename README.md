# Dating Personality Test

A modern personality test application inspired by [16personalities.com](https://www.16personalities.com/free-personality-test), built with Python Flask backend and vanilla JavaScript frontend. Discover your unique dating personality type through an interactive questionnaire.

## Features

- 💝 20-question personality assessment
- 📊 Scale-based answers (Strongly Disagree to Strongly Agree)
- 🎨 Beautiful, modern UI with smooth animations
- 📱 Fully responsive mobile design
- ⚡ Real-time progress tracking
- 🎯 Detailed personality results based on 5 dimensions
- 🔒 RESTful API with CORS support

## How It Works

The test evaluates your personality across 5 dimensions:

1. **Energy** - Extraverted vs. Introverted
2. **Mind** - Intuitive vs. Observant
3. **Nature** - Thinking vs. Feeling
4. **Tactics** - Judging vs. Prospecting
5. **Identity** - Assertive vs. Turbulent

Each question is answered on a 7-point scale from "Strongly Disagree" to "Strongly Agree", similar to the 16personalities.com format.

## Project Structure

```
.
├── app.py                 # Flask backend with API endpoints
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Single-page application template
├── static/
│   ├── css/
│   │   └── style.css     # Modern, responsive styles
│   └── js/
│       └── app.js        # Frontend logic and API calls
└── README.md
```

## Installation

1. **Clone the repository** (or use this template):
   ```bash
   git clone <your-repo-url>
   cd dating-personality
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

The application will be running on port 5000 by default.

## API Endpoints

### Get all questions
```http
GET /api/questions
```

Returns an array of 20 personality test questions.

### Submit test answers
```http
POST /api/submit-test
Content-Type: application/json

{
  "answers": [
    {
      "question_id": 1,
      "score": 2
    },
    ...
  ],
  "timestamp": "2026-02-13T12:00:00Z"
}
```

Returns personality analysis with scores across all 5 dimensions.

### Get test result
```http
GET /api/results/{id}
```

Retrieves a previously submitted test result.

## Customization

### Adding More Questions

Edit the `QUESTIONS` array in `app.py` to add or modify questions:

```python
QUESTIONS = [
    {
        "id": 1,
        "text": "Your question text here",
        "category": "extraversion"  # or other category
    },
    ...
]
```

### Customizing the Scoring Algorithm

The scoring logic is in the `submit_test()` function in `app.py`. Modify this to change how personality types are calculated.

### Adding a Database

The current implementation uses in-memory storage. To persist results:

1. Install Flask-SQLAlchemy:
   ```bash
   pip install flask-sqlalchemy
   ```

2. Update `app.py` to include database models for storing test results.

### Styling

- Modify `static/css/style.css` to customize colors, fonts, and layout
- The design uses CSS custom properties (variables) for easy theming
- Current theme uses a pink/purple gradient inspired by dating apps

## Production Deployment

For production deployment, consider:

1. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Add a database** (PostgreSQL, MySQL, etc.)

3. **Set up environment variables** for configuration

4. **Use a reverse proxy** (Nginx, Apache)

5. **Enable HTTPS** with SSL certificates

6. **Set `debug=False`** in production

## Technologies Used

- **Backend**: Python 3, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Design**: Custom CSS with gradients, animations, and responsive layout
- **API**: RESTful architecture
- **Inspiration**: [16personalities.com](https://www.16personalities.com/free-personality-test)

## Screenshots

The application features:
- A welcoming landing page with test information
- Interactive question cards with 7-point scale buttons
- Real-time progress tracking
- Detailed results page with personality badges and descriptions

## Future Enhancements

- [ ] Add more questions for deeper analysis
- [ ] Implement user accounts to save results
- [ ] Add social sharing features
- [ ] Create detailed personality type pages
- [ ] Add compatibility matching between personality types
- [ ] Export results as PDF
- [ ] Multi-language support

## License

MIT License - feel free to use this for your projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.