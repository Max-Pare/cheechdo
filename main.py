import random
import sys
import re

responses_generic = ['Definitely not (right now|now|today|this week)', 'LATER!', 'Later...', "Can't do that right now", 'Maybe later', 'Maybe (tomorrow|next week|next year|next month|later)']
timeframes = ['week', 'month', 'year']

def ask_cheech():
    def try_collapse(_response: str):
        if (res := re.search('\((.*)\)', _response)) is None: return _response
        found = res.group(1).split('|')
        return _response.replace(res.group(), random.choice(found))
    response = try_collapse(random.choice(responses_generic))
    if random.random() < .2: response += ' brah'
    return response

def main():
    for _ in range (32):
        print(ask_cheech())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        raise Exception("STOOOP!!!")