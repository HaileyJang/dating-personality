# Relationship Manual Test

A relationship assessment tool built with Python Flask that measures three key dimensions: **Attachment Style**, **Conflict Style**, and **Connection Style**. Based on research from attachment theory and the Gottman Method.

> 📖 **Discover Your Relationship Manual**: Understand how you bond, fight, and connect in relationships through 8 research-based questions.

---

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [The Three Scales](#the-three-scales)
- [How It Works](#how-it-works)
- [API Endpoints](#api-endpoints)
- [Customization](#customization)
- [Technologies](#technologies)

---

## Features

- 💝 **Three Research-Based Scales**: Attachment, Conflict, Connection
- 📊 **Visual Scale Results**: See where you fall on each dimension
- 🎯 **8 Scenario-Based Questions**: Real relationship situations
- 🎨 **Beautiful, Modern UI**: Gradient scales with animated markers
- 📱 **Fully Responsive**: Works perfectly on mobile devices
- ⚡ **Instant Results**: Immediate feedback with detailed descriptions
- 🔒 **RESTful API**: Easy to integrate and extend

## The Three Scales & Archetypes

### 1. Attachment Style (Anxious ← Secure → Avoidant)

Measures your bonding patterns in relationships:

- **X - The Pursuer** (Anxious, score < -2): Seeks reassurance, fears abandonment, needs validation
- **S - The Anchor** (Secure, score -2 to 2): Comfortable with intimacy and independence
- **V - The Distancer** (Avoidant, score > 2): Values independence, uncomfortable with closeness

### 2. Conflict Style (Defensive ← Healthy → Withdrawing)

Identifies your "Four Horsemen" patterns (Gottman Method):

- **D - The Defender** (Defensive/Critical, score < -2): Counter-attacks, criticism, contempt
- **H - The Harmonizer** (Healthy, score -2 to 2): Takes responsibility, shows empathy, constructive
- **W - The Withdrawer** (Stonewalling, score > 2): Withdraws, shuts down, needs space

### 3. Connection Style (Turn Away ← Balanced → High Engagement)

Measures how you respond to "bids" for connection:

- **T - The Turned Away** (Turn Away/Against, score < -2): Dismissive, rejects bids for attention
- **B - The Balancer** (Balanced, score -2 to 2): Responsive with healthy boundaries
- **E - The Engager** (High Engagement, score > 2): Seeks deep intimacy, highly responsive

## Your Relationship Type Code

Like MBTI, you get a **3-letter code** representing your relationship style:

**Examples:**
- **SHB** - Secure Anchor + Healthy Harmonizer + Balanced = Ideal relationship style
- **XDT** - Anxious Pursuer + Defensive + Turned Away = High conflict potential
- **VWB** - Avoidant Distancer + Withdrawer + Balanced = Emotionally distant but fair

Your code appears at the top of your results, making it easy to share and discuss your relationship manual.

## How It Works

### Scale-Based Scoring

Each answer moves you along one of the three scales:

```python
{
    "text": "Your partner hasn't replied in 4 hours...",
    "answers": [
        {
            "text": "Panic. I check my phone repeatedly.",
            "scales": {
                "attachment": -3  # Moves toward Anxious
            }
        },
        {
            "text": "Indifference. I'll do my own thing.",
            "scales": {
                "attachment": 3  # Moves toward Avoidant
            }
        },
        {
            "text": "Secure. I assume they're busy.",
            "scales": {
                "attachment": 0  # Stays at Secure
            }
        }
    ]
}
```

After all questions, your average position on each scale determines your relationship manual.

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

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open browser to http://localhost:5000
```

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Installation and basic usage
- **[EXAMPLES.md](EXAMPLES.md)** - Detailed question examples and patterns
- **[SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md)** - Architecture and technical details

## API Endpoints

### Get all questions
```http
GET /api/questions
```

Returns 8 questions across 3 sections (attachment, conflict, connection).

**Response:**
```json
[
  {
    "id": 1,
    "section": "attachment",
    "text": "The 'Silence' Trigger: You text your partner...",
    "answers": [
      {
        "id": "1a",
        "text": "Panic. I check my phone repeatedly...",
        "scales": {
          "attachment": -3
        }
      },
      {
        "id": "1b",
        "text": "Indifference. I assume they're busy...",
        "scales": {
          "attachment": 3
        }
      }
    ]
  }
]
```

### Submit test answers
```http
POST /api/submit-test
Content-Type: application/json

{
  "answers": [
    {
      "question_id": 1,
      "answer_id": "1a"
    },
    {
      "question_id": 2,
      "answer_id": "2b"
    }
  ],
  "timestamp": "2026-02-13T12:00:00Z"
}
```

**Response:**
```json
{
  "id": 1,
  "scales": {
    "attachment": -1.67,
    "conflict": 1.33,
    "connection": 0.5
  },
  "labels": {
    "attachment": "Secure Attachment",
    "conflict": "Healthy Conflict Resolution",
    "connection": "Balanced Connection"
  },
  "raw_totals": {
    "attachment": -5,
    "conflict": 4,
    "connection": 1
  }
}
```

### Get test result
```http
GET /api/results/{id}
```

Retrieves a previously submitted test result.

## Customization

### Adding More Questions

Edit the `QUESTIONS` array in `app.py`. Each question follows this structure:

```python
{
    "id": 1,
    "section": "attachment",  # or "conflict" or "connection"
    "text": "Your scenario question here",
    "answers": [
        {
            "id": "1a",
            "text": "Answer option text",
            "scales": {
                "attachment": -3  # -5 to +5 scale
            }
        },
        {
            "id": "1b",
            "text": "Another answer option",
            "scales": {
                "attachment": 3  # Opposite end of scale
            }
        }
    ]
}
```

### Scale Value Guidelines

**Attachment Scale:**
- `-5 to -3`: Strong anxious attachment
- `-2 to -1`: Mild anxious lean
- `0`: Secure attachment
- `1 to 2`: Mild avoidant lean
- `3 to 5`: Strong avoidant attachment

**Conflict Scale:**
- `-5 to -3`: Strong defensive/critical/contempt
- `-2 to -1`: Mild defensiveness
- `0`: Healthy conflict resolution
- `1 to 2`: Mild withdrawal
- `3 to 5`: Strong stonewalling

**Connection Scale:**
- `-5 to -3`: Turn away/against bids
- `-2 to -1`: Mild disengagement
- `0`: Balanced responsiveness
- `1 to 2`: Moderately engaged
- `3 to 5`: Highly engaged/seeking deep intimacy

### Adapting for Other Assessments

This scale-based system works for any assessment with dimensional outcomes:

**Political Compass:**
```python
"scales": {
    "economic": -3,  # Left vs Right
    "social": 2      # Authoritarian vs Libertarian
}
```

**Learning Styles:**
```python
"scales": {
    "abstract_concrete": -2,  # Abstract vs Concrete
    "active_reflective": 3    # Active vs Reflective
}
```

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

## Key Features of the Scoring System

### ✅ Flexible Question Format
- Each question can have **2-10+ answer options**
- No fixed format or scale required

### ✅ Multi-Trait Scoring
- Each answer contributes points to **multiple traits**
- Example: "Coffee shop date" → +2 introvert, +1 intellectual, +1 traditional

### ✅ Dynamic Criteria
- **No predefined traits** - use any trait names you want
- System automatically tracks and calculates all traits

### ✅ Comprehensive Results
- Shows **top 5 traits** with rankings
- Displays **all traits** with scores and percentages
- Visual bars show relative strength

## Use Cases

This flexible system works for any type of assessment:

- 🎭 **Personality Tests** - Dating style, Myers-Briggs, Big Five
- 💼 **Career Assessments** - Job fit, leadership style, work preferences
- 📚 **Learning Styles** - Visual, auditory, kinesthetic preferences
- 🍕 **Preference Surveys** - Food, travel, lifestyle choices
- 🎮 **Character Quizzes** - "Which character are you?" style quizzes

## Future Enhancements

- [ ] User accounts to save results
- [ ] Database integration for persistence
- [ ] Social sharing features
- [ ] Detailed trait descriptions and insights
- [ ] Compatibility matching between users
- [ ] Export results as PDF
- [ ] Multi-language support
- [ ] Admin panel to manage questions

## License

MIT License - feel free to use this for your projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Questions?

- Check [EXAMPLES.md](EXAMPLES.md) for question patterns
- See [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md) for technical details
- Review the code in `app.py` for implementation details