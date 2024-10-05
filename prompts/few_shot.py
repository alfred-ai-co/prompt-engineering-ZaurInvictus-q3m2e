FEW_SHOT_PROMPT = """

Given the following topic {input}, generate a quiz with a random number of questions between 1 to 5.

Please format the output as a valid JSON object that strictly conforms to the following structure:

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

Please generate the quiz based on the given topic and format it according to these specifications, ensuring the output is valid JSON.

"""