# hn-sonar
Automatically be notified if someone replies to your comment on Hacker News. No email required. Wait! This one is different than the others (I know, that's what they all say.)

[![Updates](https://pyup.io/repos/github/Decagon/hn-sonar/shield.svg)](https://pyup.io/repos/github/Decagon/hn-sonar/) [![Python 3](https://pyup.io/repos/github/Decagon/hn-sonar/python-3-shield.svg)](https://pyup.io/repos/github/Decagon/hn-sonar/)


hn-sonar is a decentralized and self-hosted app which lets you know if someone responds to your HN comment or post. Notifications can be batched in any interval you desire, simply by running hn-sonar whenever you would like to check for new comments. It keeps track of which comments it has already seen, and will catch up by checking older comments to see if those have received new replies, so that you don't miss anything. 

HN-Sonar can...

- be self-hosted so there are no privacy concerns with sharing your email address with another company/website. hn-sonar can still be centralized, and still does not need your email.

- is able to find the latest replies even if hn-sonar is not running all of the time. Use the `--continue` flag to search through all of the comments that were missed while hn-sonar was not running and check for replies. This allows you to batch replies into a single daily email by running hn-sonar daily. The continue option works even if the last comment that was seen was deleted, and it won't go into an infinite loop.

- be used to detect if the author edited their comment after submission, or deleted it*.


## Usage

Requires Python 3 and Beautiful Soup 4.

If you have pip, you can install Beautiful Soup by running `pip install beautifulsoup4`.

Grab hn-sonar.py: `wget https://raw.githubusercontent.com/Decagon/hn-sonar/master/hn-sonar.py`

Run it as `while true; do python hn-sonar.py <your-hn-username> --continue | mail; sleep 1m; done;` to check every minute and recieve an email when someone responds to your comment. Don't worry--the `--continue` flag will keep track of which comments it hasn't seen yet, so feel free to stop or start hn-sonar however often you please.

### Example email

Reply to comment: http://news.ycombinator.com/item?id=xyz

*Important:* ensure that the directory where hn-sonar is being run in is writable, as hn-sonar uses a database to know which replies have been emailed.
