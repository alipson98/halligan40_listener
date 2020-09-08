# halligan40_listener

Super simple script to poll the `halligan40` queue and alert when someone new joins

## To run:
Make sure all of the necessary packages are installed by running `pip install -r requirements.txt` or install each package seperately if that doesn't work.

This program uses pyttsx for text to speech. If it gives you problems, see the documentation at https://pyttsx.readthedocs.io/en/latest/install.html

Edit listener.py and add your EECS username (utln)
Run listener.py with python3

### SSH setup
This program must run locally for text to speech to work, so it needs to ssh into the Halligan server to run `halligan40`. This script assumes that you already have an ssh key set up locally and have added the public key to the Halligan server. See https://www.ssh.com/ssh/keygen/ for more on ssh keys. If your setup is correct, you will be able to run `ssh [username]@homework.cs.tufts.edu "halligan40 check_queue"` and see the current queue.

Alternatively, if you don't want to add an ssh key, you could edit the script to expect and enter your password.
