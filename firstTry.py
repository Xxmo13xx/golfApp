"""Calculator using docopt

Usage:
  firstTry.py <operation> <num1> <num2>
  firstTry.py (-h | --help)

Arguments
  num1 First Number
  num2 Second Number

Options:
  -h --help     Show this screen.
  -a

"""
from docopt import docopt

def add(num1, num2):
	print("Adding: " + str(num1) + " " + str(num2))
	return int(num1)+int(num2)
if __name__ == '__main__':
    args = docopt(__doc__, version='Calculator with docopt')
    print(args)
    functions = {
        'add': add(args['<num1>'],args['<num2>']),
        'subtract': lambda num1, num2: num1 - num2,
        'multiply': lambda num1, num2: num1 * num2,
        'divide': lambda num1, num2: num1 / num2
    }

    print functions[args['<operation>']]


