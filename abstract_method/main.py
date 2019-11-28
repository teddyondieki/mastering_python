from .frog_world import FrogWorld
from .wizard_world import WizardWorld
from .game_environment import GameEnvironment


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you?')
        age = int(age)
    except ValueError as err:
        print(f'Age {age} is invalid, please try again...')
        return (False, age)
    return (True, age)


def main():
    name = input('Hello. What\'s your name?')
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()
