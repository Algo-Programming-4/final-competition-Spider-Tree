from typing import Tuple, List

Position = Tuple[int, int]

class Player:
    """
    Handles position and movement; student must implement olisort.
    """
    def __init__(self, start_pos: Position, rows: int, cols: int):
        self.pos = start_pos
        self.rows = rows
        self.cols = cols

    def get_position(self) -> Position:
        return self.pos

    def move(self, direction: str) -> None:
        r, c = self.pos
        if direction == 'up' and r > 0:
            r -= 1
        elif direction == 'down' and r < self.rows - 1:
            r += 1
        elif direction == 'left' and c > 0:
            c -= 1
        elif direction == 'right' and c < self.cols - 1:
            c += 1
        self.pos = (r, c)

    def olisort(self, data: List[int]) -> List[int]:
        """
        Student stub: sort data and return new list.
        """
        pass
    def joliQueue_challenge(tasks):
        pass
    # Most people know farmer Joliphant is horrible at time managment.
# To help dear old Joliphant and his wife you will have to manage farmer Joliphant's schedule for a week.
# Each day you will receive a tuple containing 5 tasks.
# Each task will have an energy property that is required to perform the task. Your energy limit is 100 per day.
# Each task will have a success property. YOUR 401K will be in shambles if you do not meet the success quota of 1000 at the end of the week.
# Task is a class with methods .getEnergy() and .getSuccess().
# You will return a priorety queue with a method .dequeue() which pops the most valuble task and returns that task.
# Good luck! It's real tricky to determine a good balance between energy and success. "Just like my kids." -- Gandhi
