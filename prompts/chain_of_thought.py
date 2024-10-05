CHAIN_OF_THOUGHT_PROMPT = """

Given the following topic {input}, generate a quiz with a random number of questions between 1 to 5. Follow these steps to create the quiz:

Step 1: Analyze the topic
- Consider the main concepts and key points related to {input}.
- Think about what aspects of this topic would be important to test in a quiz.

Step 2: Determine the number of questions
- Randomly choose a number between 1 and 5 for the quiz length.
- Write down your chosen number: [NUMBER OF QUESTIONS]

Step 3: Generate questions
For each question (repeat this step [NUMBER OF QUESTIONS] times):
- Formulate a clear, concise question about an important aspect of {input}.
- Create four distinct answer choices, ensuring one is correct and the others are plausible but incorrect.
- Assign letters A, B, C, D to the choices.
- Identify the correct answer's letter.
- Write down the question, choices, and correct answer.

Step 4: Format the output
- Structure the quiz data as a JSON object according to the specified format.
- Ensure all requirements are met:
  1. The output is a single, valid JSON object.
  2. Each question has exactly 4 choices.
  3. The "key" for each choice is a single uppercase letter (A, B, C, D).
  4. The "answer" is a single uppercase letter corresponding to the correct choice's key.
  5. The "answer" exists in the choices list.
  6. The number of questions is between 1 and 5.
  7. No explanatory text or comments outside the JSON structure.

Step 5: Review and validate
- Double-check that the JSON structure is correct and all requirements are met.
- Ensure the quiz content is relevant to the given topic {input}.

Now, please generate the quiz based on the topic {input}, following these steps and formatting it according to the specifications. The output should be valid JSON in the following structure:

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


"""