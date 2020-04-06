import argparse
import platform
import os

parser = argparse.ArgumentParser(description='Argument Parser Tutorial')
parser.add_argument('--name', type=str,  help='Show the text')
parser.add_argument('--transportation','-t', choices=['Car', 'Bicycle'], help='Crop the image?')

if __name__ == '__main__':
    args = parser.parse_args()
    name = args.name
    trans = args.transportation

    print('{} always take {} to the scool'.format(name, trans) )
    if vars(args).get('transportation') == None and vars(args).get('name') == None :
        raise Exception('GG')
    print(vars(args))
    