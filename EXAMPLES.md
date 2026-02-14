# Question Examples

This document shows examples of how to create questions with the flexible scoring system.

## Basic Structure

```python
{
    "id": 1,                    # Unique question number
    "text": "Question text?",   # The question to ask
    "answers": [                # Array of possible answers
        {
            "id": "1a",         # Unique answer ID (question_id + letter)
            "text": "Answer text",
            "points": {         # Dictionary of trait: points
                "trait1": 2,
                "trait2": 1
            }
        }
    ]
}
```

## Example 1: Simple Binary Choice

```python
{
    "id": 1,
    "text": "Do you prefer staying in or going out?",
    "answers": [
        {
            "id": "1a",
            "text": "Staying in",
            "points": {
                "introvert": 3,
                "homebody": 2
            }
        },
        {
            "id": "1b",
            "text": "Going out",
            "points": {
                "extrovert": 3,
                "social": 2
            }
        }
    ]
}
```

## Example 2: Multiple Choices (3-4 options)

```python
{
    "id": 2,
    "text": "How do you handle stress?",
    "answers": [
        {
            "id": "2a",
            "text": "Talk to friends",
            "points": {
                "social": 3,
                "extrovert": 2,
                "emotional": 2
            }
        },
        {
            "id": "2b",
            "text": "Exercise or physical activity",
            "points": {
                "physical": 4,
                "active": 3,
                "healthy": 2
            }
        },
        {
            "id": "2c",
            "text": "Read or watch something",
            "points": {
                "introvert": 3,
                "calm": 2,
                "intellectual": 1
            }
        },
        {
            "id": "2d",
            "text": "Work through it logically",
            "points": {
                "analytical": 4,
                "logical": 3,
                "independent": 2
            }
        }
    ]
}
```

## Example 3: Many Options (5+ choices)

```python
{
    "id": 3,
    "text": "What's your ideal vacation?",
    "answers": [
        {
            "id": "3a",
            "text": "Beach resort with all amenities",
            "points": {
                "relaxed": 3,
                "luxury": 2,
                "traditional": 1
            }
        },
        {
            "id": "3b",
            "text": "Mountain hiking and camping",
            "points": {
                "adventurous": 4,
                "nature_lover": 3,
                "active": 3
            }
        },
        {
            "id": "3c",
            "text": "City tour with museums and culture",
            "points": {
                "intellectual": 3,
                "cultured": 3,
                "curious": 2
            }
        },
        {
            "id": "3d",
            "text": "Road trip with no fixed plans",
            "points": {
                "spontaneous": 4,
                "adventurous": 2,
                "flexible": 3
            }
        },
        {
            "id": "3e",
            "text": "Staycation at home",
            "points": {
                "introvert": 3,
                "homebody": 4,
                "practical": 2
            }
        },
        {
            "id": "3f",
            "text": "Volunteer trip or mission work",
            "points": {
                "altruistic": 4,
                "compassionate": 3,
                "purposeful": 3
            }
        }
    ]
}
```

## Example 4: Overlapping Traits

Notice how multiple answers can contribute to the same trait with different weights:

```python
{
    "id": 4,
    "text": "How do you make important decisions?",
    "answers": [
        {
            "id": "4a",
            "text": "Trust my gut feeling",
            "points": {
                "intuitive": 4,
                "emotional": 2,
                "spontaneous": 1
            }
        },
        {
            "id": "4b",
            "text": "Research thoroughly and analyze data",
            "points": {
                "analytical": 4,
                "logical": 3,
                "careful": 2
            }
        },
        {
            "id": "4c",
            "text": "Ask friends and family for advice",
            "points": {
                "social": 3,
                "collaborative": 3,
                "emotional": 2
            }
        },
        {
            "id": "4d",
            "text": "Consider pros and cons carefully",
            "points": {
                "logical": 3,
                "analytical": 2,
                "careful": 3
            }
        }
    ]
}
```

## Example 5: Career Assessment

```python
{
    "id": 5,
    "text": "What type of work environment do you prefer?",
    "answers": [
        {
            "id": "5a",
            "text": "Open office with team collaboration",
            "points": {
                "collaborative": 4,
                "social": 3,
                "team_player": 3
            }
        },
        {
            "id": "5b",
            "text": "Private office or remote work",
            "points": {
                "independent": 4,
                "focused": 3,
                "introvert": 2
            }
        },
        {
            "id": "5c",
            "text": "Mix of both depending on the task",
            "points": {
                "flexible": 3,
                "balanced": 3,
                "adaptable": 2
            }
        }
    ]
}
```

## Tips for Creating Good Questions

1. **Make answers mutually exclusive** - Users should clearly prefer one option
2. **Use 3-5 answers per question** - Not too few (limiting) or too many (overwhelming)
3. **Vary point values** - Use 1-4 points to show strength of association
4. **Create trait overlap** - Multiple questions should contribute to the same traits
5. **Balance your traits** - Make sure each trait appears in multiple questions
6. **Use clear language** - Avoid ambiguous or complex wording
7. **Test your questions** - Take the test yourself to ensure it makes sense

## Trait Naming Conventions

Use descriptive, lowercase trait names:
- ✅ `introvert`, `extrovert`, `analytical`, `creative`
- ✅ `team_player`, `nature_lover`, `risk_taker`
- ❌ `Introvert`, `EXTROVERT`, `analytical_person`

The frontend will automatically format them nicely (e.g., "team_player" → "Team Player")

## Calculating Results

The system automatically:
1. Sums all points for each trait
2. Identifies the top 5 traits
3. Calculates percentages for all traits
4. Displays results with visual bars and rankings

No additional configuration needed!
