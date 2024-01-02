import os
import sys
from pprint import pprint

# sys.path.append(os.path.realpath('.'))
import inquirer

questions = [
    inquirer.List('cost',
                      message='Which column do you want for cost?',
                      choices=['column_1', 'column_2', 'column_3'],
                      ),
]

answers = inquirer.prompt(questions)

pprint(answers)