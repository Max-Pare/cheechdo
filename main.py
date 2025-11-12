import random, sys, re, shlex, subprocess, string
from defs import *

responses_generic = ['Definitely not (right now|now|today|this week)', 'LATER!', 'Later...', "Can't do that right now", 'Maybe later', 'Maybe (tomorrow|next week|next year|next month|later)']
timeframes = ['week', 'month', 'year']


def ask_cheech():
    def try_collapse(_response: str): # quantum collapse or whatever it's called
        # if a wildcard is not found just return the response brah
        if (res := re.search('\((.*)\)', _response)) is None: return _response 
        # pick the first capture group which is the wildcard with the parentheses removed
        found = res.group(1).split('|') 
        return _response.replace(res.group(), random.choice(found))
    response = random.choice(responses_generic)
    response = try_collapse(response)
    # n (n / 100) chance to add BRAH to the end of the string, unless there is a non-letter character (to avoid shit like LATER! brah)
    if random.random() < .2 and response[-1].lower() in string.ascii_lowercase: response += ' brah'
    return response

def main():
    for _ in range (32):
        print(ask_cheech())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        raise STOOOP('No chance')

