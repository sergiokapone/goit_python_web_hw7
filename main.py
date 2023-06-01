from  argparse import ArgumentParser

parser = ArgumentParser(description='Students DB')
parser.add_argument('--action', help='Commands: create, update, list, remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

argumens = parser.parse_args()

my_arg = vars(argumens)

action = my_arg.get('action')
title = my_arg.get('title')
_id = my_arg.get('id')
login = my_arg.get('login')

if __name__ == '__main__':
    print(action)
