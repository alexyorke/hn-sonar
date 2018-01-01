# hn-sonar
Automatically be notified if someone replies to your comment on Hacker News. No email required. Wait! This one is different than the others (I know, that's what they all say.)

[![Updates](https://pyup.io/repos/github/Decagon/hn-sonar/shield.svg)](https://pyup.io/repos/github/Decagon/hn-sonar/) [![Python 3](https://pyup.io/repos/github/Decagon/hn-sonar/python-3-shield.svg)](https://pyup.io/repos/github/Decagon/hn-sonar/)

```
usage: hn-sonar.py [-h] -u [U] [--nocomments] [--nostory]
                   [--tmpfile [TMPFILE]]

optional arguments:
  -h, --help           show this help message and exit
  -u [U]               your Hacker News username
  --nocomments         don't notify when you recieve a reply to your comment
  --nostory            don't notify when you recieve a reply to your story
  --tmpfile [TMPFILE]  the visited comment ids database file path
  ```
 
`hn-sonar` is a decentralized and self-hosted app which lets you know if someone responds to your HN comment or post. Notifications can be batched in any interval you desire, simply by running `hn-sonar` whenever you would like to check for new comments. It keeps track of which comments it has already seen, and will catch up by checking older comments to see if those have received new replies, so that you don't miss anything. 

HN-Sonar can...

- be self-hosted so there are no privacy concerns with sharing your email address with another company/website. `hn-sonar` can still be centralized, and still does not need your email.

- is able to find the latest replies even if `hn-sonar` is not running all of the time.

- allow you to get replies on only stories, comments, or both (default).


## Usage

Run `hn-sonar` as `while true; do python3 hn-sonar.py -u <your-hn-username> | mail; sleep 1m; done;` in your favorite shell to check every minute and recieve an email when someone responds to your comment. Make sure not to check the comments too frequently as the API could throw a 403 forbidden error, so once every minute or so should be safe.

## Roadmap

Some cool features that we'd like to add to `hn-sonar` are:

- detect if the author edited their comment after submission, or deleted it*.

- don't recieve notifications on comments or stories posted after a certain date (e.g. one week.)

- don't recieve many hundreds of notifications on extremely popular comments or stories.

- whitelisting or blocking notifications based on usernames.

- get notifications when your comment gets a reply and it is in the grey zone (when your comment is downvoted and dimmed.)

- ability to include the original comment and the replied comment into the notification email for context.

### Example email

Reply to comment: http://news.ycombinator.com/item?id=xyz

*Important:* ensure that the directory where `hn-sonar` is being run in is writable, as `hn-sonar` uses a database to know which replies have been emailed.
