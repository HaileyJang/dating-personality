from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Relationship Manual Test Questions
# Three scales: Attachment (-5 to +5), Conflict (-5 to +5), Connection (-5 to +5)
# Negative values = Anxious/Defensive/Turn Away
# Positive values = Avoidant/Stonewalling/Turn Towards  
# Zero = Secure/Healthy/Balanced

QUESTIONS = [
    # ===== PART 1: ATTACHMENT RADAR (Bonding Style) =====
    {
        "id": 1,
        "section": "attachment",
        "text": "The 'Silence' Trigger: You text your partner good morning. It is now 2:00 PM, and you see they've been active on Instagram but haven't replied to you. What is your immediate internal reaction?",
        "answers": [
            {
                "id": "1a",
                "text": "Panic. I check my phone repeatedly and wonder if I did something wrong.",
                "scales": {
                    "attachment": -3  # Anxious
                }
            },
            {
                "id": "1b",
                "text": "Indifference/Annoyance. I assume they are busy. If they don't reply, I'll just do my own thing.",
                "scales": {
                    "attachment": 3  # Avoidant
                }
            },
            {
                "id": "1c",
                "text": "Secure. I assume they got distracted. I'll send a funny meme later or just wait.",
                "scales": {
                    "attachment": 0  # Secure
                }
            },
            {
                "id": "1d",
                "text": "Anger. I feel disrespected and prepare to confront them.",
                "scales": {
                    "attachment": -4  # Disorganized/Anxious
                }
            }
        ]
    },
    {
        "id": 2,
        "section": "attachment",
        "text": "The 'Closeness' Trigger: You've spent three nights in a row with a new partner. They ask to see you again tonight. How do you feel?",
        "answers": [
            {
                "id": "2a",
                "text": "Excited. I love the momentum and want to be around them as much as possible.",
                "scales": {
                    "attachment": -2  # Anxious/Secure lean
                }
            },
            {
                "id": "2b",
                "text": "Suffocated. I need a night off to recharge and feel like myself again.",
                "scales": {
                    "attachment": 4  # Avoidant
                }
            },
            {
                "id": "2c",
                "text": "Comfortable. I'm happy to see them, but also fine saying 'not tonight' if I'm tired.",
                "scales": {
                    "attachment": 0  # Secure
                }
            }
        ]
    },
    {
        "id": 3,
        "section": "attachment",
        "text": "The Vulnerability Test: Something embarrassing or painful happened to you at work. Do you tell your partner?",
        "answers": [
            {
                "id": "3a",
                "text": "Immediately. I need their validation to feel better.",
                "scales": {
                    "attachment": -3  # Anxious
                }
            },
            {
                "id": "3b",
                "text": "Maybe later. I process it alone first, then share the 'edited' version.",
                "scales": {
                    "attachment": 3  # Avoidant
                }
            },
            {
                "id": "3c",
                "text": "Yes. I share it because I trust them to support me, but I don't need them to fix it.",
                "scales": {
                    "attachment": 0  # Secure
                }
            }
        ]
    },
    
    # ===== PART 2: GOTTMAN "HORSEMEN" SCAN (Conflict Style) =====
    {
        "id": 4,
        "section": "conflict",
        "text": "The 'Complaint' Scenario: Your partner says: 'You never do the dishes. You're so messy.' What is your instinctual comeback?",
        "answers": [
            {
                "id": "4a",
                "text": "I cooked dinner! You're the one who leaves socks everywhere.",
                "scales": {
                    "conflict": -2  # Defensiveness
                }
            },
            {
                "id": "4b",
                "text": "You're right, I've been slacking. I'll do them now.",
                "scales": {
                    "conflict": 0  # Healthy - Taking Responsibility
                }
            },
            {
                "id": "4c",
                "text": "I'm 'messy'? You're acting like a nag.",
                "scales": {
                    "conflict": -4  # Criticism/Contempt
                }
            },
            {
                "id": "4d",
                "text": "I say nothing, turn away, and look at my phone.",
                "scales": {
                    "conflict": 3  # Stonewalling
                }
            }
        ]
    },
    {
        "id": 5,
        "section": "conflict",
        "text": "The 'Eye Roll' Check (Contempt): During a disagreement, your partner starts crying or gets emotional. What is your thought?",
        "answers": [
            {
                "id": "5a",
                "text": "Oh great, here come the waterworks. Grow up.",
                "scales": {
                    "conflict": -5  # Contempt
                }
            },
            {
                "id": "5b",
                "text": "I hate seeing them upset. I want to fix it.",
                "scales": {
                    "conflict": 0  # Empathy
                }
            },
            {
                "id": "5c",
                "text": "I feel overwhelmed. I don't know what to do.",
                "scales": {
                    "conflict": 2  # Flooding
                }
            }
        ]
    },
    {
        "id": 6,
        "section": "conflict",
        "text": "The 'Cool Down' Needs: The fight is heating up and you are yelling. What do you need to stop?",
        "answers": [
            {
                "id": "6a",
                "text": "Reassurance. I need them to hug me or tell me we're okay, or I can't calm down.",
                "scales": {
                    "conflict": -3  # Anxious Repair
                }
            },
            {
                "id": "6b",
                "text": "Space. I need to leave the room for 20 minutes. If they follow me, I will explode.",
                "scales": {
                    "conflict": 4  # Stonewalling/Avoidant
                }
            },
            {
                "id": "6c",
                "text": "Logic. I need us to stop using emotion and stick to the facts.",
                "scales": {
                    "conflict": 1  # Intellectualizing
                }
            }
        ]
    },
    
    # ===== PART 3: DAILY "BIDS" (Connection Style) =====
    {
        "id": 7,
        "section": "connection",
        "text": "The 'Look at This' Test: Your partner interrupts your reading/work to show you a cute dog video.",
        "answers": [
            {
                "id": "7a",
                "text": "Turn Towards. I put my book down, watch it, and laugh with them.",
                "scales": {
                    "connection": 3  # Turn Towards
                }
            },
            {
                "id": "7b",
                "text": "Turn Away. I grunt or barely look up.",
                "scales": {
                    "connection": -2  # Turn Away
                }
            },
            {
                "id": "7c",
                "text": "Turn Against. I say, 'Can't you see I'm busy?'",
                "scales": {
                    "connection": -4  # Turn Against
                }
            }
        ]
    },
    {
        "id": 8,
        "section": "connection",
        "text": "The 'Love Map' Depth: How much do you want to know about your partner's inner world (childhood, fears, dreams)?",
        "answers": [
            {
                "id": "8a",
                "text": "Everything. I want to merge our minds.",
                "scales": {
                    "connection": 4  # High Intimacy
                }
            },
            {
                "id": "8b",
                "text": "The Basics. I care, but I don't need to psychoanalyze them constantly.",
                "scales": {
                    "connection": 0  # Moderate Intimacy
                }
            },
            {
                "id": "8c",
                "text": "Action-Oriented. I prefer doing activities together rather than deep emotional talks.",
                "scales": {
                    "connection": -3  # Low Intimacy/Activity-Based
                }
            }
        ]
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
    
    # Initialize the three scales
    scales = {
        'attachment': 0,
        'conflict': 0,
        'connection': 0
    }
    
    # Count answers per section for averaging
    section_counts = {
        'attachment': 0,
        'conflict': 0,
        'connection': 0
    }
    
    # Process each answer
    for answer in answers:
        question_id = answer['question_id']
        answer_id = answer['answer_id']
        
        # Find the question
        question = next((q for q in QUESTIONS if q['id'] == question_id), None)
        if not question:
            continue
        
        # Find the selected answer within the question
        selected_answer = next((a for a in question['answers'] if a['id'] == answer_id), None)
        if not selected_answer:
            continue
        
        # Add scale values from this answer
        section = question.get('section', 'attachment')
        for scale_name, value in selected_answer['scales'].items():
            scales[scale_name] += value
            section_counts[section] += 1
    
    # Calculate averages for each scale
    averaged_scales = {}
    for scale_name, total in scales.items():
        count = section_counts.get(scale_name, 1)
        averaged_scales[scale_name] = round(total / count if count > 0 else 0, 2)
    
    # Determine labels and archetypes for each scale
    def get_attachment_info(score):
        if score < -2:
            return {
                "label": "Anxious Attachment",
                "archetype": "X",
                "archetype_name": "The Pursuer"
            }
        elif score > 2:
            return {
                "label": "Avoidant Attachment",
                "archetype": "V",
                "archetype_name": "The Distancer"
            }
        else:
            return {
                "label": "Secure Attachment",
                "archetype": "S",
                "archetype_name": "The Anchor"
            }
    
    def get_conflict_info(score):
        if score < -2:
            return {
                "label": "Defensive/Critical",
                "archetype": "D",
                "archetype_name": "The Defender"
            }
        elif score > 2:
            return {
                "label": "Stonewalling/Withdrawing",
                "archetype": "W",
                "archetype_name": "The Withdrawer"
            }
        else:
            return {
                "label": "Healthy Conflict Resolution",
                "archetype": "H",
                "archetype_name": "The Harmonizer"
            }
    
    def get_connection_info(score):
        if score < -2:
            return {
                "label": "Turn Away/Against",
                "archetype": "T",
                "archetype_name": "The Turned Away"
            }
        elif score > 2:
            return {
                "label": "High Engagement",
                "archetype": "E",
                "archetype_name": "The Engager"
            }
        else:
            return {
                "label": "Balanced Connection",
                "archetype": "B",
                "archetype_name": "The Balancer"
            }
    
    # Get info for each scale
    attachment_info = get_attachment_info(averaged_scales['attachment'])
    conflict_info = get_conflict_info(averaged_scales['conflict'])
    connection_info = get_connection_info(averaged_scales['connection'])
    
    # Create result object
    result = {
        'id': len(test_results) + 1,
        'scales': averaged_scales,
        'labels': {
            'attachment': attachment_info['label'],
            'conflict': conflict_info['label'],
            'connection': connection_info['label']
        },
        'archetypes': {
            'attachment': {
                'code': attachment_info['archetype'],
                'name': attachment_info['archetype_name']
            },
            'conflict': {
                'code': conflict_info['archetype'],
                'name': conflict_info['archetype_name']
            },
            'connection': {
                'code': connection_info['archetype'],
                'name': connection_info['archetype_name']
            }
        },
        'personality_code': f"{attachment_info['archetype']}{conflict_info['archetype']}{connection_info['archetype']}",
        'raw_totals': scales,
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
