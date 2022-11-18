import random

ADD_SUB = "+-"
MUL_DIV = "*/"
OPERATORS = "+-*/"
NUM_CAP = 10000
DECIMAL_POINTS = 4
OPERATOR_CAP = 3
DIFFICULTY_LEVELS = f"""
Difficulty levels:
    Level 1: integers
        integer [-{NUM_CAP}, {NUM_CAP}]
    Level 2: numbers
        number [-{NUM_CAP}, {NUM_CAP}] rounded to {DECIMAL_POINTS} decimal points.
    Level 3: addition and subtraction
        number followed by ((+ | -) number) repeated up to {OPERATOR_CAP} times.
    Level 4: multiplication and division
        number followed by ((* | /) number) repeated up to {OPERATOR_CAP} times.
    Level 5: full expressions
        number followed by ((+ | - | * | /) number) repeated up to {OPERATOR_CAP} times.
"""

class NumpadTrainer(object):
    """
    A training game for improving your numpad typing speed.
    """
    def __init__(self):
        """
        Creates a new NumpadTrainer object.
        Attributes:
            self.level (int [1,5])
        
        Methods:
            get_difficulty()
                returns level as int [1,5]
            get_expression()
                returns an expression of self.level difficulty
            input_matches()
                returns true if input matches
            play_round()
                returns true if answer correct
            play_game()
                returns score as Fraction
        """
        self.level = None
    
    def get_difficulty(self):
        input_message = "Please select a difficulty (1 to 5): "
        selected_level = input(DIFFICULTY_LEVELS + input_message)
        while not (selected_level.isdigit() and (1 <= int(selected_level) <= 5)):
            selected_level = input("Invalid number! " + input_message)
        return int(selected_level)

    def get_integer(self):
        return str(random.randint(-NUM_CAP, NUM_CAP))

    def get_number(self):
        num_dp = random.randint(1, DECIMAL_POINTS)
        remainder = random.randint(1, 10**num_dp - 1) / 10**num_dp
        return self.get_integer() + str(remainder)
    
    def get_operator(self, operators):
        return random.choice(list(operators))

    def get_operator_expression(self, operators):
        num_operators = random.randint(1, OPERATOR_CAP)
        expression = self.get_number()
        for _ in range(num_operators):
            expression += self.get_operator(operators)
            expression += self.get_number()
        return expression

    def get_expression(self):
        match self.level:
            case 1:
                expression = self.get_integer()
            case 2:
                expression = self.get_number()
            case 3:
                expression = self.get_operator_expression(ADD_SUB)
            case 4:
                expression = self.get_operator_expression(MUL_DIV)
            case 5:
                expression = self.get_operator_expression(OPERATORS)
            case _:
                return "ERROR: Difficulty level not set!"
        return expression

    def input_matches(self, answer, expected):
        return answer.strip() == expected

    def play_round(self):
        expected = self.get_expression()
        answer = input("\nExpression:  " + expected + "\nYour answer: ")
        if answer == "stop":
            return answer
        else:
            return self.input_matches(answer, expected)

    def play_game(self):
        self.level = self.get_difficulty()
        score_list = []
        while True:
            value = self.play_round()
            if value == "stop":
                break
            else:
                score_list.append(value)
        correct = sum(score_list)
        total = len(score_list)
        percent = round((correct/total) * 100, 2)
        print(f"You got {correct} out of {total} correct. ({percent}%)")
        return correct, total
    
if __name__ == "__main__":
    trainer = NumpadTrainer()
    # trainer.level = trainer.get_difficulty()
    # print(trainer.play_round())
    trainer.play_game()