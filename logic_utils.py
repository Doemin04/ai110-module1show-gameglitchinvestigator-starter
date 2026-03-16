def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    # normalize whitespace
    raw = raw.strip()

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # allow floats like "3.0"
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Return a single outcome string: "Win", "Too High", or "Too Low".
    # Prefer numeric comparison when possible.
    try:
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win"
        if g > s:
            return "Too High"
        return "Too Low"
    except Exception:
        # Fall back to string comparison / numeric float attempt
        g_str = str(guess)
        s_str = str(secret)
        if g_str == s_str:
            return "Win"
        try:
            if float(g_str) > float(s_str):
                return "Too High"
            return "Too Low"
        except Exception:
            # Last resort: lexicographic
            if g_str > s_str:
                return "Too High"
            return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
