import random

responses_generic = ['Definitely not now', 'Definitely not today' , ' LATER! ', ' Later brah... ', " Can't do that right now brah ", ' Maybe later...', 'Maybe next __TIMEFRAME__']
timeframes = ['week', 'month', 'year']

def ask_cheech():
    response = random.choice(responses_generic)
    if '__TIMEFRAME__' in response:
        return response.replace('__TIMEFRAME__', random.choice(timeframes))
    return response

def main():
    for _ in range (10):
        print(ask_cheech())

if __name__ == '__main__':
    main()