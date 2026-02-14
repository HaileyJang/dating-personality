# Quick Start Guide

## Installation & Setup

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Open in Browser

Navigate to `http://localhost:5000` and take the test!

## How the Scoring System Works

### Question Format

Each question in `app.py` follows this structure:

```python
{
    "id": 1,
    "text": "What's your ideal first date?",
    "answers": [
        {
            "id": "1a",
            "text": "Coffee shop conversation",
            "points": {
                "introvert": 2,      # +2 points to introvert
                "intellectual": 1,   # +1 point to intellectual
                "traditional": 1     # +1 point to traditional
            }
        },
        {
            "id": "1b",
            "text": "Adventure activity",
            "points": {
                "extrovert": 2,
                "adventurous": 3,
                "physical": 2
            }
        }
    ]
}
```

### When User Selects an Answer

If the user selects "Coffee shop conversation":
- `introvert` gets +2 points
- `intellectual` gets +1 point
- `traditional` gets +1 point

### Final Results

After all questions are answered:
1. System totals points for each trait
2. Ranks traits by score (highest first)
3. Shows top 5 traits with visual bars
4. Displays all traits with percentages

## Customizing Questions

### Add a New Question

Open `app.py` and add to the `QUESTIONS` list:

```python
QUESTIONS = [
    # ... existing questions ...
    {
        "id": 9,  # Next available ID
        "text": "Your new question here?",
        "answers": [
            {
                "id": "9a",
                "text": "First option",
                "points": {
                    "trait_name": 3,
                    "another_trait": 1
                }
            },
            {
                "id": "9b",
                "text": "Second option",
                "points": {
                    "different_trait": 2
                }
            }
        ]
    }
]
```

### Modify Existing Questions

Simply edit the question text, answer text, or point allocations in the `QUESTIONS` array.

### Remove Questions

Delete the question object from the `QUESTIONS` array.

## Understanding Results

### Top Traits Section
- Shows the 5 highest-scoring traits
- Displays rank (#1, #2, etc.)
- Shows point total and percentage
- Visual bar shows relative strength

### All Traits Grid
- Shows every trait that received points
- Sorted by score (highest to lowest)
- Displays points and percentage for each

## Tips for Creating Questions

1. **Use 3-5 answer options** per question
2. **Make answers distinct** - avoid overlapping choices
3. **Vary point values** (1-4 points) based on strength
4. **Create trait consistency** - multiple questions should contribute to the same traits
5. **Use descriptive trait names** like `adventurous`, `analytical`, `team_player`

## Example Scenarios

### Scenario 1: User is Very Consistent

If a user consistently chooses adventurous options:
- `adventurous` trait accumulates many points
- Result: Clear #1 trait with high percentage

### Scenario 2: User is Balanced

If a user's choices are varied:
- Points spread across many traits
- Result: Multiple traits with similar scores

### Scenario 3: User Has Conflicting Traits

The system handles this naturally:
- Both `introvert` and `extrovert` can score points
- Results show which tendency is stronger

## Troubleshooting

### Port Already in Use

If port 5000 is taken, modify `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change port
```

### Questions Not Loading

Check browser console (F12) for errors. Ensure:
- Flask server is running
- No syntax errors in `app.py`
- CORS is enabled (already configured)

### Results Look Wrong

Verify:
- Each answer has valid point allocations
- Point values are positive numbers
- Trait names are spelled consistently

## Next Steps

1. **Customize questions** - Edit `QUESTIONS` in `app.py`
2. **Add more questions** - Follow the format in `EXAMPLES.md`
3. **Style the UI** - Modify `static/css/style.css`
4. **Add database** - Store results persistently (see README.md)
5. **Deploy** - Use Gunicorn + Nginx for production

## Need Help?

- See `EXAMPLES.md` for detailed question examples
- See `README.md` for full documentation
- Check `app.py` for the complete question format
