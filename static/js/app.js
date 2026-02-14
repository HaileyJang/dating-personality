// API Base URL
const API_URL = '/api';

// State
let questions = [];
let currentQuestionIndex = 0;
let answers = [];

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadQuestions();
});

// Load questions from API
async function loadQuestions() {
    try {
        const response = await fetch(`${API_URL}/questions`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch questions');
        }
        
        questions = await response.json();
        document.getElementById('totalQuestions').textContent = questions.length;
    } catch (error) {
        console.error('Error loading questions:', error);
        alert('Error loading questions. Please refresh the page.');
    }
}

// Start the test
function startTest() {
    document.getElementById('welcomeScreen').classList.remove('active');
    document.getElementById('testScreen').classList.add('active');
    
    currentQuestionIndex = 0;
    answers = [];
    
    displayQuestion();
}

// Display current question
function displayQuestion() {
    if (currentQuestionIndex >= questions.length) {
        submitTest();
        return;
    }
    
    const question = questions[currentQuestionIndex];
    
    // Update question text
    document.getElementById('questionText').textContent = question.text;
    
    // Update progress
    document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progressFill').style.width = `${progress}%`;
    
    // Clear previous selection
    document.querySelectorAll('.scale-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
}

// Handle answer selection
function selectAnswer(value) {
    const question = questions[currentQuestionIndex];
    
    // Store answer
    answers.push({
        question_id: question.id,
        score: value
    });
    
    // Visual feedback
    document.querySelectorAll('.scale-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    event.target.closest('.scale-btn').classList.add('selected');
    
    // Move to next question after a short delay
    setTimeout(() => {
        currentQuestionIndex++;
        displayQuestion();
    }, 300);
}

// Submit test and get results
async function submitTest() {
    try {
        const response = await fetch(`${API_URL}/submit-test`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                answers: answers,
                timestamp: new Date().toISOString()
            }),
        });
        
        if (!response.ok) {
            throw new Error('Failed to submit test');
        }
        
        const result = await response.json();
        displayResults(result);
    } catch (error) {
        console.error('Error submitting test:', error);
        alert('Error submitting test. Please try again.');
    }
}

// Display results
function displayResults(result) {
    const personality = result.personality;
    
    // Hide test screen, show results screen
    document.getElementById('testScreen').classList.remove('active');
    document.getElementById('resultsScreen').classList.add('active');
    
    // Update personality badges
    document.getElementById('energyBadge').textContent = personality.energy;
    document.getElementById('mindBadge').textContent = personality.mind;
    document.getElementById('natureBadge').textContent = personality.nature;
    document.getElementById('tacticsBadge').textContent = personality.tactics;
    document.getElementById('identityBadge').textContent = personality.identity;
    
    // Generate description
    const description = generateDescription(personality);
    document.getElementById('personalityDescription').innerHTML = description;
}

// Generate personality description
function generateDescription(personality) {
    let html = '<h3>Your Dating Personality</h3>';
    
    // Energy
    if (personality.energy === 'Extraverted') {
        html += '<p><strong>Extraverted:</strong> You gain energy from social interactions and enjoy meeting new people. In dating, you likely prefer active dates and social settings.</p>';
    } else {
        html += '<p><strong>Introverted:</strong> You recharge through alone time and prefer deeper one-on-one connections. You likely enjoy intimate, meaningful dates.</p>';
    }
    
    // Mind
    if (personality.mind === 'Intuitive') {
        html += '<p><strong>Intuitive:</strong> You focus on possibilities and the big picture. You appreciate deep conversations and intellectual connection in relationships.</p>';
    } else {
        html += '<p><strong>Observant:</strong> You focus on concrete facts and present realities. You value practical demonstrations of affection and reliability.</p>';
    }
    
    // Nature
    if (personality.nature === 'Thinking') {
        html += '<p><strong>Thinking:</strong> You make decisions based on logic and objective analysis. You value honesty and direct communication in relationships.</p>';
    } else {
        html += '<p><strong>Feeling:</strong> You make decisions based on emotions and values. You prioritize harmony and emotional connection in relationships.</p>';
    }
    
    // Tactics
    if (personality.tactics === 'Judging') {
        html += '<p><strong>Judging:</strong> You prefer structure and planning. You likely enjoy planning dates in advance and appreciate predictability in relationships.</p>';
    } else {
        html += '<p><strong>Prospecting:</strong> You prefer flexibility and spontaneity. You enjoy spontaneous adventures and keeping things fresh in relationships.</p>';
    }
    
    // Identity
    if (personality.identity === 'Assertive') {
        html += '<p><strong>Assertive:</strong> You are self-assured and resistant to stress. You approach dating with confidence and don\'t dwell on setbacks.</p>';
    } else {
        html += '<p><strong>Turbulent:</strong> You are self-conscious and sensitive to stress. You are driven to improve and deeply care about your partner\'s feelings.</p>';
    }
    
    return html;
}

// Restart test
function restartTest() {
    document.getElementById('resultsScreen').classList.remove('active');
    document.getElementById('welcomeScreen').classList.add('active');
    
    currentQuestionIndex = 0;
    answers = [];
}
