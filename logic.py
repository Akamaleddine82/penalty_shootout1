import random
import csv
from datetime import datetime

class PenaltyShootoutGame:
    """Class handling the penalty shootout game logic."""

    def __init__(self) -> None:
        """Initialize the game state."""
        self.shots_taken = 0
        self.goals_scored = 0
        self.total_shots = 5

    def take_shot(self, direction: str) -> str:
        """
        Handle a penalty shot attempt.

        Args:
            direction (str): The direction the player chooses to shoot.

        Returns:
            str: Result of the shot and current score.
        """
        if self.shots_taken >= self.total_shots:
            return f"Game over! You scored {self.goals_scored}/{self.total_shots} goals."

        keeper_direction = random.choice(["left", "center", "right"])
        self.shots_taken += 1

        if direction != keeper_direction:
            self.goals_scored += 1
            result = f"GOAL! Keeper went {keeper_direction}."
        else:
            result = f"SAVED! Keeper went {keeper_direction}."

        if self.shots_taken == self.total_shots:
            result += f" Final score: {self.goals_scored}/{self.total_shots}."
            save_result(self.goals_scored, self.total_shots)

        return result

def save_result(goals: int, total: int) -> None:
    """
    Save the match result to a CSV file.

    Args:
        goals (int): Number of goals scored.
        total (int): Total number of shots.
    """
    try:
        with open('match_history.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), goals, total])
    except Exception as e:
        print(f"Error saving match result: {e}")

