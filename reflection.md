# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  'It seemed like a simple guessing game with numbers ranging from 1 to 100'
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  '1. The hints were inverted, 2, The new game button did not work as expected, it generated a new number but I am unable to play the guessing game. 3, Normal difficulty offers more attempts than the easy difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? : 'Claude Code'
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 'The AI was correct in generating the assertions I verified it by reading over it and determining if that was the output i excpected the app to return'
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
'I ran into a no module found error when running the tests and asked what the reason could be and the AI suggested a conftest.py file so pytest can correctly identify the root, that didnt work so I delve deeper into a conversation on multiple solutions/reasons and implemented the fix I ddetermined to be right which was to configure the test file in the testing extenstion on the sidebar I never used before'
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 'If it behaved how I expected it to after the reading and also how I would expect a guessing game to go'
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. 'I used pytest to run my generated tests and found all to pass, but I guess that inital success did discourage me from creating more test'
- Did AI help you design or understand any tests? How?
'It was supper helpful setting up the structure of the test file as well as assertions, although it messed up in picking the right type a function was supposed to output those were minor changes compared to creating a test file by hand'
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
