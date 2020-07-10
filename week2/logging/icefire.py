import logging
import requests
import argparse
import pprint

BOOK = "https://www.anapioficeandfire.com/api/books"
CHARACTER = "https://www.anapioficeandfire.com/api/characters"
HOUSES = "https://www.anapioficeandfire.com/api/houses"

def main():

    # if you use logging, always describe your logging.basicConfig @ the start
    # default logging level is 'warning', which would skip less severe warnings
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    
    try:
        # this write
        # INFO: 12/12/2019 11:55:02 AM Program started
        logging.info('Scripting started')
    
        # make a call to the API
        if args.bookno:
            icefire = requests.get(BOOK + "/" + args.bookno)
        elif args.characterno:
            icefire = requests.get(CHARACTER + "/" + args.characterno)
        elif args.houseno:
            icefire = requests.get(HOUSES + "/" + args.houseno)

        # force a ZeroDivisionError
        # 10 / 0
        IF_data = icefire.json()
        # pretty print the json response
        # pprint.pprint(icefire.json())
        print(f"name: {IF_data['name']}\nplayed by: {IF_data['playedBy']}")
        
        # write response code to log
        logging.info("API Response Code - " + str(icefire))
        
    # if a program errors, write that error to a log file
    except Exception as err:
        logging.critical(err)
                        
    finally:
        # INFO: 12/12/2019 11:55:02 AM Program ended
        logging.info("Program ended")
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (integer) to look up.')
    parser.add_argument('--characterno', help='Enter the character number (integer) to look up.')
    parser.add_argument('--houseno', help='Enter the house number (integer) to look up.')
    args = parser.parse_args()
    main()
