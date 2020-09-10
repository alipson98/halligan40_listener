import pyttsx3
import subprocess
import time
import re

GREEN = "\u001b[32m"
RM = "\u001b[0m"

engine = pyttsx3.init()
engine.setProperty('rate', 180)

# fill in with your login information before you run
user = ''

check_cmd = "ssh {}@homework.cs.tufts.edu \"halligan40 check_queue\"".format(user)

def get_end_of_queue():
    q = subprocess.check_output(check_cmd, shell=True).decode("utf-8").split('---')
    return q[-1]

def get_utln(line):
    utln = re.search(r'\((.*)\)', line)
    return utln.group(0) if utln else None

def alert(line):
    # add whatever alert prints or noises you would like
    print(GREEN+"New user in queue:"+RM)
    print(line)
    engine.say("new user in queue")
    engine.runAndWait()


if __name__ == "__main__":
    if (not user):
        print("Username is not specified. Edit this file with your EECS username\n")
        exit()
    
    init_end = get_end_of_queue()
    print(init_end)
    curr_utln = get_utln(init_end)

    while (True):
        time.sleep(15)
        test_end = get_end_of_queue()
        test_utln = get_utln(test_end)
        if (not test_utln): # queue empty
            curr_utln = None
            curr_end = None
            continue

        if (test_utln != curr_utln):
            curr_utln = test_utln
            curr_end = test_end
            alert(curr_end)
