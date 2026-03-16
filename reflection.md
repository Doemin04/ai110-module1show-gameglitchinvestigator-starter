# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- On first run the UI looked functional but behaved oddly: hints often told me to do the opposite of what I should, the New Game button didn't reliably let me play again, and attempts/counts were inconsistent.
- Concrete bugs I observed: 
1) The hint messages were reversed — when a guess was too high the UI said "Go HIGHER!" and vice versa. 
2) The New Game button did not fully reset the game state (it reset the secret and attempts but did not reset `status`/`score`/`history`), so after winning or losing you could still be blocked from playing. 
3) Attempts display and control are inconsistent (attempts are initialized to 1, New Game sets attempts to 0, and the UI can show one attempt left while the game is unplayable). 
4) The secret is sometimes coerced to a string on alternating attempts which creates mixed-type comparisons and unpredictable behavior.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

* **Correct AI Suggestion:** I used Copilot Agent with the @workspace tag to fix the `new_game` button. The AI correctly suggested adding `st.session_state.status = "playing"` to the block. I verified this by running the app and successfully starting a new game after losing.
* **Incorrect/Misleading AI Suggestion:** AI that wrote unnecessary string comparison. I verified this was wrong by looking at the check_guess func and told it to fix it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

## 3. Debugging and testing your fixes

* I decided a bug was genuinely fixed when I could play the game in the browser without encountering the previous errors (like the backwards hints or the broken restart button) and when all of my automated unit tests passed successfully in the terminal.
* I ran `pytest tests/test_game_logic.py` which executed four tests, including the new `test_parse_guess_invalid_input` test. This test verified that passing a non-numeric string like "hello" to `parse_guess` correctly returns `False`, `None`, and an error message.
* Yes, Copilot Agent helped me design the test for invalid inputs. I asked it to generate a test specifically targeting the `parse_guess` function, and it successfully wrote the assertions and imported the required module on its own.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
