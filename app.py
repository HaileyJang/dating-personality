from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Personality test questions
QUESTIONS = [
    {
        "id": 1,
        "text": "You regularly make new friends.",
        "category": "extraversion"
    },
    {
        "id": 2,
        "text": "You often get so lost in thoughts that you ignore or forget your surroundings.",
        "category": "intuition"
    },
    {
        "id": 3,
        "text": "You try to respond to your emails as soon as possible and cannot stand a messy inbox.",
        "category": "judging"
    },
    {
        "id": 4,
        "text": "You find it easy to introduce yourself to other people.",
        "category": "extraversion"
    },
    {
        "id": 5,
        "text": "You often feel overwhelmed by other people's problems.",
        "category": "feeling"
    },
    {
        "id": 6,
        "text": "You are usually highly motivated and energetic.",
        "category": "extraversion"
    },
    {
        "id": 7,
        "text": "Winning a debate matters less to you than making sure no one gets upset.",
        "category": "feeling"
    },
    {
        "id": 8,
        "text": "You often feel as if you have to justify yourself to other people.",
        "category": "turbulent"
    },
    {
        "id": 9,
        "text": "Your home and work environments are quite tidy.",
        "category": "judging"
    },
    {
        "id": 10,
        "text": "You do not usually initiate conversations.",
        "category": "introversion"
    },
    {
        "id": 11,
        "text": "You rarely do something just out of sheer curiosity.",
        "category": "sensing"
    },
    {
        "id": 12,
        "text": "You feel superior to other people.",
        "category": "thinking"
    },
    {
        "id": 13,
        "text": "Being organized is more important to you than being adaptable.",
        "category": "judging"
    },
    {
        "id": 14,
        "text": "You are usually the one who makes the first move in a relationship.",
        "category": "extraversion"
    },
    {
        "id": 15,
        "text": "Your mood can change very quickly.",
        "category": "turbulent"
    },
    {
        "id": 16,
        "text": "You enjoy participating in group activities.",
        "category": "extraversion"
    },
    {
        "id": 17,
        "text": "You like books and movies that make you come up with your own interpretation of the ending.",
        "category": "intuition"
    },
    {
        "id": 18,
        "text": "You think that everyone's views should be respected regardless of whether they are supported by facts or not.",
        "category": "feeling"
    },
    {
        "id": 19,
        "text": "You prefer to do your chores before allowing yourself to relax.",
        "category": "judging"
    },
    {
        "id": 20,
        "text": "You enjoy watching people argue.",
        "category": "thinking"
    }
]

# In-memory storage for test results
test_results = []

# Routes
@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Get all personality test questions"""
    return jsonify(QUESTIONS)

@app.route('/api/submit-test', methods=['POST'])
def submit_test():
    """Submit personality test answers and calculate results"""
    data = request.get_json()
    
    if not data or 'answers' not in data:
        return jsonify({"error": "Answers are required"}), 400
    
    answers = data['answers']
    
    # Calculate scores for each category
    scores = {
        'extraversion': 0,
        'introversion': 0,
        'intuition': 0,
        'sensing': 0,
        'thinking': 0,
        'feeling': 0,
        'judging': 0,
        'perceiving': 0,
        'assertive': 0,
        'turbulent': 0
    }
    
    # Process answers
    for answer in answers:
        question_id = answer['question_id']
        score = answer['score']  # -3 to 3
        
        # Find the question
        question = next((q for q in QUESTIONS if q['id'] == question_id), None)
        if not question:
            continue
        
        category = question['category']
        
        # Add score to appropriate category
        if category in scores:
            scores[category] += score
        
        # Handle reverse scoring for introversion
        if category == 'introversion':
            scores['introversion'] += score
        elif category == 'extraversion':
            scores['introversion'] -= score
        
        # Handle reverse scoring for sensing
        if category == 'sensing':
            scores['sensing'] += score
        elif category == 'intuition':
            scores['sensing'] -= score
        
        # Handle reverse scoring for perceiving
        if category == 'judging':
            scores['perceiving'] -= score
        
        # Handle assertive vs turbulent
        if category == 'turbulent':
            scores['turbulent'] += score
            scores['assertive'] -= score
    
    # Determine personality type
    personality = {
        'energy': 'Extraverted' if scores['extraversion'] > 0 else 'Introverted',
        'mind': 'Intuitive' if scores['intuition'] > scores['sensing'] else 'Observant',
        'nature': 'Thinking' if scores['thinking'] > scores['feeling'] else 'Feeling',
        'tactics': 'Judging' if scores['judging'] > 0 else 'Prospecting',
        'identity': 'Assertive' if scores['assertive'] > scores['turbulent'] else 'Turbulent',
        'scores': scores
    }
    
    # Store result
    result = {
        'id': len(test_results) + 1,
        'personality': personality,
        'timestamp': data.get('timestamp', '')
    }
    test_results.append(result)
    
    return jsonify(result), 201

@app.route('/api/results/<int:result_id>', methods=['GET'])
def get_result(result_id):
    """Get a specific test result"""
    result = next((r for r in test_results if r['id'] == result_id), None)
    if result:
        return jsonify(result)
    return jsonify({"error": "Result not found"}), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
