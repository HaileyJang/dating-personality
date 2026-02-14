// API Base URL
const API_URL = '/api';

// State
let questions = [];
let currentQuestionIndex = 0;
let answers = [];
let isSubmitting = false;

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
    
    // Display answer options
    const answersContainer = document.getElementById('answersContainer');
    answersContainer.innerHTML = question.answers.map(answer => `
        <button class="answer-btn" data-answer-id="${answer.id}" onclick="selectAnswer('${answer.id}')">
            ${escapeHtml(answer.text)}
        </button>
    `).join('');
}

// Handle answer selection
function selectAnswer(answerId) {
    // Prevent double-clicks on the same question
    if (isSubmitting) return;
    
    const question = questions[currentQuestionIndex];
    
    // Disable all buttons to prevent double-click
    const buttons = document.querySelectorAll('.answer-btn');
    buttons.forEach(btn => btn.disabled = true);
    
    // Store answer
    answers.push({
        question_id: question.id,
        answer_id: answerId
    });
    
    // Visual feedback - find the clicked button by answer id
    buttons.forEach(btn => {
        if (btn.dataset.answerId === answerId) {
            btn.classList.add('selected');
        }
    });
    
    // Move to next question after a short delay
    setTimeout(() => {
        currentQuestionIndex++;
        displayQuestion();
    }, 400);
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Submit test and get results
async function submitTest() {
    // Prevent multiple submissions
    if (isSubmitting) return;
    isSubmitting = true;
    
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
        isSubmitting = false;
        alert('Error submitting test. Please try again.');
    }
}

// Display results
function displayResults(result) {
    // Hide test screen, show results screen
    document.getElementById('testScreen').classList.remove('active');
    document.getElementById('resultsScreen').classList.add('active');
    
    // Get scales for easier reference
    const scales = result.scales;
    const archetypes = result.archetypes;
    const labels = result.labels;
    
    // Populate the scale overview card (left)
    const scaleOverview = document.getElementById('scaleOverview');
    scaleOverview.innerHTML = `
        <div class="scale-overview-item">
            <div class="scale-overview-header">
                <span class="scale-overview-label">Attachment</span>
                <span class="scale-overview-value">${scales.attachment.toFixed(2)}</span>
            </div>
            <div class="mini-scale-labels">
                <span>X</span>
                <span>S</span>
                <span>V</span>
            </div>
            <div class="mini-scale-bar">
                <div class="mini-scale-marker" style="left: ${((scales.attachment + 5) / 10) * 100}%"></div>
            </div>
            <div class="scale-overview-result">${labels.attachment}</div>
        </div>
        <div class="scale-overview-item">
            <div class="scale-overview-header">
                <span class="scale-overview-label">Conflict</span>
                <span class="scale-overview-value">${scales.conflict.toFixed(2)}</span>
            </div>
            <div class="mini-scale-labels">
                <span>D</span>
                <span>H</span>
                <span>W</span>
            </div>
            <div class="mini-scale-bar">
                <div class="mini-scale-marker" style="left: ${((scales.conflict + 5) / 10) * 100}%"></div>
            </div>
            <div class="scale-overview-result">${labels.conflict}</div>
        </div>
        <div class="scale-overview-item">
            <div class="scale-overview-header">
                <span class="scale-overview-label">Connection</span>
                <span class="scale-overview-value">${scales.connection.toFixed(2)}</span>
            </div>
            <div class="mini-scale-labels">
                <span>T</span>
                <span>B</span>
                <span>E</span>
            </div>
            <div class="mini-scale-bar">
                <div class="mini-scale-marker" style="left: ${((scales.connection + 5) / 10) * 100}%"></div>
            </div>
            <div class="scale-overview-result">${labels.connection}</div>
        </div>
    `;
    
    // Populate the personality type card (right)
    const personalityType = document.getElementById('personalityType');
    personalityType.innerHTML = `
        <h2>Your Relationship Type</h2>
        <div class="personality-code">${result.personality_code}</div>
        <p class="personality-subtitle">
            ${archetypes.attachment.name} • 
            ${archetypes.conflict.name} • 
            ${archetypes.connection.name}
        </p>
    `;
    
    // Display the three detailed scales with archetypes
    const traitsList = document.getElementById('traitsList');
    
    traitsList.innerHTML = `
        <div class="scale-card">
            <div class="scale-card-left">
                <h3>Attachment Style</h3>
                <div class="scale-label-row">
                    <span class="scale-end">Anxious</span>
                    <span class="scale-end">Secure</span>
                    <span class="scale-end">Avoidant</span>
                </div>
                <div class="scale-bar-container">
                    <div class="scale-bar">
                        <div class="scale-marker" style="left: ${((scales.attachment + 5) / 10) * 100}%"></div>
                    </div>
                </div>
                <div class="scale-result-label">${labels.attachment}</div>
                <p class="scale-description">${getAttachmentDescription(scales.attachment)}</p>
            </div>
            <div class="scale-card-right">
                <div class="archetype-badge">
                    <div class="archetype-code">${archetypes.attachment.code}</div>
                    <div class="archetype-name">${archetypes.attachment.name}</div>
                </div>
            </div>
        </div>
        
        <div class="scale-card">
            <div class="scale-card-left">
                <h3>Conflict Style</h3>
                <div class="scale-label-row">
                    <span class="scale-end">Defensive</span>
                    <span class="scale-end">Healthy</span>
                    <span class="scale-end">Withdrawing</span>
                </div>
                <div class="scale-bar-container">
                    <div class="scale-bar">
                        <div class="scale-marker" style="left: ${((scales.conflict + 5) / 10) * 100}%"></div>
                    </div>
                </div>
                <div class="scale-result-label">${labels.conflict}</div>
                <p class="scale-description">${getConflictDescription(scales.conflict)}</p>
            </div>
            <div class="scale-card-right">
                <div class="archetype-badge">
                    <div class="archetype-code">${archetypes.conflict.code}</div>
                    <div class="archetype-name">${archetypes.conflict.name}</div>
                </div>
            </div>
        </div>
        
        <div class="scale-card">
            <div class="scale-card-left">
                <h3>Connection Style</h3>
                <div class="scale-label-row">
                    <span class="scale-end">Turn Away</span>
                    <span class="scale-end">Balanced</span>
                    <span class="scale-end">High Engagement</span>
                </div>
                <div class="scale-bar-container">
                    <div class="scale-bar">
                        <div class="scale-marker" style="left: ${((scales.connection + 5) / 10) * 100}%"></div>
                    </div>
                </div>
                <div class="scale-result-label">${labels.connection}</div>
                <p class="scale-description">${getConnectionDescription(scales.connection)}</p>
            </div>
            <div class="scale-card-right">
                <div class="archetype-badge">
                    <div class="archetype-code">${archetypes.connection.code}</div>
                    <div class="archetype-name">${archetypes.connection.name}</div>
                </div>
            </div>
        </div>
    `;
}

// Get attachment style description
function getAttachmentDescription(score) {
    if (score < -2) {
        return "You tend to seek reassurance and closeness, sometimes worrying about your partner's availability. You may fear abandonment and need frequent validation.";
    } else if (score > 2) {
        return "You value independence and may feel uncomfortable with too much closeness. You prefer emotional distance and self-reliance in relationships.";
    } else {
        return "You're comfortable with intimacy and independence. You can be close without losing yourself and trust your partner's commitment.";
    }
}

// Get conflict style description
function getConflictDescription(score) {
    if (score < -2) {
        return "During conflicts, you may become defensive, critical, or show contempt. You tend to counter-attack or focus on your partner's flaws.";
    } else if (score > 2) {
        return "You tend to withdraw or stonewall during conflicts. You may shut down, need space, or avoid emotional confrontation.";
    } else {
        return "You handle conflicts constructively. You take responsibility, show empathy, and work toward resolution without attacking or withdrawing.";
    }
}

// Get connection style description
function getConnectionDescription(score) {
    if (score < -2) {
        return "You may miss or reject your partner's bids for connection. You might be dismissive of their attempts to engage or share moments.";
    } else if (score > 2) {
        return "You're highly responsive to your partner's bids for connection. You seek deep emotional intimacy and want to know everything about them.";
    } else {
        return "You have a balanced approach to connection. You respond to bids for attention while maintaining healthy boundaries.";
    }
}

// Restart test
function restartTest() {
    document.getElementById('resultsScreen').classList.remove('active');
    document.getElementById('welcomeScreen').classList.add('active');
    
    currentQuestionIndex = 0;
    answers = [];
    isSubmitting = false;
}
