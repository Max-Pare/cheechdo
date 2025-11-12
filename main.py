import random, sys, re, shlex, subprocess, string, hashlib
from defs import *
from time import sleep

responses_negative = ['definitely not (right now|now|today|this week)', 'LATER!', 'later...', "can't do that right now", 'maybe (tomorrow|next week|next year|next month|later)']
responses_positive = ['ok kang']
timeframes = ['week', 'month', 'year']

CHEECH_INTOXICATION_LEVEL = 75 # [0 - 100]
CHEECH_INTOXICATION_SCALED = CHEECH_INTOXICATION_LEVEL * 0.01
CHEECH_DELAY = .9

def cheech_think(ok: bool = False) -> str:
    global CHEECH_DELAY
    sleep(CHEECH_DELAY)
    def try_collapse(_response: str): # quantum collapse or whatever it's called
        # if a wildcard is not found just return the response brah
        if (res := re.search(r'\((.*)\)', _response)) is None: return _response 
        # pick the first capture group which is the wildcard with the parentheses removed
        found = res.group(1).split('|') 
        return _response.replace(res.group(), random.choice(found))
    response = random.choice(responses_negative)
    response = try_collapse(response)
    # n (n / 100) chance to add BRAH to the end of the string, unless there is a non-letter character (to avoid shit like LATER! brah)
    if random.random() < .2 and response[-1].lower() in string.ascii_lowercase: response += ' brah'
    return response

def ask_cheech(_command: list):
    global CHEECH_DELAY
    cheech_ok = True
    if random.random() <= CHEECH_INTOXICATION_SCALED:
        cheech_ok = False
    if cheech_ok:
        sleep(CHEECH_DELAY * .5)
        print('ok kang')
        sleep(1)
        subprocess.run(_command, check=True)
        exit(0)
    print(cheech_think())

def main():
    global CHEECH_DELAY
    CHEECH_DELAY = CHEECH_DELAY * (random.random() + .5)
    command = sys.argv[1:]
    ask_cheech(command)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        raise STOOOP('No chance')

