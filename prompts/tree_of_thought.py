TREE_OF_THOUGHT_PROMPT = """
Given the topic {input}, generate a quiz with a random number of questions between 1 to 5. Use the Tree of Thought approach to create the best possible quiz:

1. Topic Analysis (explore 3 perspectives):
   a) Historical: Consider the historical context and development of {input}.
   b) Contemporary: Examine current applications or relevance of {input}.
   c) Interdisciplinary: Explore connections between {input} and other fields.
   
   Evaluate these perspectives and choose the most suitable one(s) for the quiz.

2. Question Types (consider 3 options for each question):
   a) Multiple choice
   b) True/False
   c) Fill in the blank
   
   For each question, evaluate these types and select the most appropriate one.

3. Difficulty Levels (explore 3 possibilities for each question):
   a) Easy: Basic knowledge or simple application
   b) Medium: Deeper understanding or analysis
   c) Hard: Complex application or synthesis of ideas
   
   Assess which difficulty level is most suitable for each question.

4. Answer Choices (for multiple choice, generate 5 possibilities):
   Create 5 potential answer choices for each question. Evaluate them based on:
   - Plausibility
   - Distinctiveness
   - Relevance to the question
   
   Select the best 4 choices, ensuring one is correct and the others are good distractors.

5. Final Review and Selection:
   - If you generated more than 5 questions, evaluate each based on relevance, clarity, and alignment with the chosen perspective(s). Select the best ones to meet the 1-5 question requirement.
   - Ensure a mix of difficulty levels if you have multiple questions.
   - Verify that the selected questions and answers accurately represent the topic.

After completing this thought process, format the final quiz as a valid JSON object strictly conforming to the following structure:

{{
  "questions": [
    {{
      "question": "The question text",
      "choices": [
        {{
          "key": "A",
          "value": "First choice"
        }},
        {{
          "key": "B",
          "value": "Second choice"
        }},
        {{
          "key": "C",
          "value": "Third choice"
        }},
        {{
          "key": "D",
          "value": "Fourth choice"
        }}
      ],
      "answer": "A"
    }}
  ]
}}

Requirements:
1. The output must be a single, valid JSON object.
2. Each question should have exactly 4 choices.
3. The "key" for each choice should be a single uppercase letter (A, B, C, D).
4. The "answer" should be a single uppercase letter corresponding to the correct choice's key.
5. Ensure that the "answer" exists in the choices list.
6. The number of questions should be random, between 1 and 5.
7. Do not include any explanatory text or comments outside of the JSON structure.

Generate the quiz based on the given topic, using this Tree of Thought process, and format it according to these specifications, ensuring the output is valid JSON.
"""