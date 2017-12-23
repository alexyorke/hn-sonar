# hn-sonar
Automatically be notified if someone replies to your comment on Hacker News. No email required. Wait! This one is different than the others (I know, that's what they all say.)

HN-Sonar can...

- be self-hosted so there are no privacy concerns with sharing your email address with another company/website. hn-sonar can still be centralized, and still does not need your email.

- be efficient with API requests so that you recieve notifications almost instantly by creating a tree-based cache on disk

- is able to find the latest replies even if hn-sonar is not running all of the time*

- be used to detect if the author edited their comment after submission, or deleted it*

* feature not implemented yet.

## Usage

Requires Python 3 and Beautiful Soup 4. If you have pip, you can install Beautiful Soup by running `pip install beautifulsoup4`. Run it as `while true; do python hn-sonar.py <your-hn-username> | mail; sleep 10; done;` to check every 10 seconds and recieve a mail message when someone responds to your comment.

*Important:* hn-sonar only checks the first page for comments, so if the delay is too long a reply may go off the page and hn-sonar will not see it. This will be fixed in future versions. Also, ensure that the directory where hn-sonar is being run in is writable, as hn-sonar uses a database to know which replies have been emailed.
