# hn-sonar
Automatically be notified if someone replies to your comment on Hacker News. No email required. Wait! This one is different than the others (I know, that's what they all say.)

HN-Sonar can...

- be self-hosted so there are no privacy concerns with sharing your email address with another company/website. hn-sonar can still be centralized, and still does not need your email.

- is able to find the latest replies even if hn-sonar is not running all of the time. Use the `--continue` flag to search through all of the comments that were missed while hn-sonar was not running and check for replies. This allows you to batch replies into a single daily email by running hn-sonar daily. The continue option works even if the last comment that was seen was deleted, and it won't go into an infinite loop.

- be used to detect if the author edited their comment after submission, or deleted it*.


## Usage

Requires Python 3 and Beautiful Soup 4. If you have pip, you can install Beautiful Soup by running `pip install beautifulsoup4`. Run it as `while true; do python hn-sonar.py <your-hn-username> | mail; sleep 10; done;` to check every 10 seconds and recieve a mail message when someone responds to your comment. If you don't want to have hn-sonar running every 10 seconds (and there is a chance that hn-sonar will not be running all of the time) you can use the `--continue` flag which will check previous pages for comments. hn-sonar will use the last comment id to find where it left off from, so this flag cannot be used when you start hn-sonar for the first time. The continue option can be invoked with `python hn-sonar.py <your-hn-username> --continue`.

### Example email

Reply to comment: http://news.ycombinator.com/item?id=xyz

*Important:* ensure that the directory where hn-sonar is being run in is writable, as hn-sonar uses a database to know which replies have been emailed.
