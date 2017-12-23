import re
from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import sys

try:
    hnName = sys.argv[1]
except IndexError:
    print("Usage: hn-sonar.py <hn-username>")
    sys.exit()

usedIdsFilePath = "hnSonarUsedIds.txt"
hnFirebaseAPI = "https://hacker-news.firebaseio.com/v0/"
# find traversed parent ids so that replies are not printed more than once

try:
    with open(usedIdsFilePath, "r+") as f:
        usedIds = f.readlines()
        usedIds = [x.strip('\n') for x in usedIds]
except IOError:
    usedIds = []


r = urllib.urlopen('http://news.ycombinator.com/newcomments').read()
soup = BeautifulSoup(r, "lxml")
commentItems = soup.find_all("tr", attrs={"class": "athing"})
with open(usedIdsFilePath, 'a') as f:
    for commentItem in commentItems:
        commentLinks = commentItem.find_all('a', href=True)
        # zeroth item is vote arrow (ignore)
        # first item is user name for comment
        # second item is comment isolated
        # third item is parent id
        # fourth item is not sure

        parentId = (re.findall(r'\d+', commentLinks[3]['href']))[0]
        if (parentId in usedIds):
            continue

        f.write(parentId + "\n")
        # check to see if the parent id is a post.
        # if it is not a post, find the username of the parent
        # if the username matches ours, then it is a comment reply
        post = json.loads(urllib2.urlopen(hnFirebaseAPI + "item/" +
                          str(parentId) + ".json").read())
        if (post is not None and post['type'] == 'comment'):
            postParentData = urllib2.urlopen(hnFirebaseAPI +
                                             "item/" + str(post['parent']) +
                                             ".json")
            if (json.loads(postParentData.read())['by'] == hnName):
                print("Reply to comment: " +
                      "https://news.ycombinator.com/item?id=" + str(parentId))
