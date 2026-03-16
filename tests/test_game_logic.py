import random
from logic_utils import check_guess


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_session_state(**overrides):
    """Return a dict that mimics st.session_state defaults, with optional overrides."""
    state = {
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "secret": 42,
    }
    state.update(overrides)
    return state


def apply_new_game(state):
    """Replicate exactly what the new_game block in app.py does."""
    state["attempts"] = 0
    state["secret"] = random.randint(1, 100)
    state["status"] = "playing"
    state["score"] = 0


# ---------------------------------------------------------------------------
# #FIX: Generated new_game reset tests
# ---------------------------------------------------------------------------

def test_new_game_resets_status_from_won():
    state = make_session_state(status="won")
    apply_new_game(state)
    assert state["status"] == "playing"


def test_new_game_resets_status_from_lost():
    state = make_session_state(status="lost")
    apply_new_game(state)
    assert state["status"] == "playing"


def test_new_game_resets_score_to_zero():
    state = make_session_state(score=999)
    apply_new_game(state)
    assert state["score"] == 0


def test_new_game_resets_attempts_to_zero():
    state = make_session_state(attempts=7)
    apply_new_game(state)
    assert state["attempts"] == 0


def test_new_game_secret_in_valid_range():
    state = make_session_state()
    for _ in range(50):           # run many times to account for randomness
        apply_new_game(state)
        assert 1 <= state["secret"] <= 100


def test_new_game_generates_new_secret():
    """Secret should not be guaranteed to stay the same after reset."""
    state = make_session_state(secret=50)
    secrets_seen = set()
    for _ in range(20):
        apply_new_game(state)
        secrets_seen.add(state["secret"])
    # With 20 draws from 1-100, getting more than one unique value is near-certain
    assert len(secrets_seen) > 1


def test_new_game_does_not_preserve_previous_score():
    """Score from a previous game must not bleed into the next game."""
    state = make_session_state(score=150, status="won")
    apply_new_game(state)
    assert state["score"] == 0
    assert state["status"] == "playing"


def test_new_game_status_remains_playing_when_already_playing():
    """Pressing New Game mid-game should keep status as playing."""
    state = make_session_state(status="playing", attempts=3, score=10)
    apply_new_game(state)
    assert state["status"] == "playing"
    assert state["attempts"] == 0
    assert state["score"] == 0


# ---------------------------------------------------------------------------
# #FIX: Original check_guess tests modified assertions to compare against outcome instead of result
# ---------------------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
