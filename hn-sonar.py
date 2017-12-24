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

# check if we should check previous pages for comments
# if hn-sonar was not running for a while
try:
    if (sys.argv[2] == "--continue"):
        shouldContinue = True
except IndexError:
    shouldContinue = False

usedIdsFilePath = "hnSonarUsedIds.txt"
hnFirebaseAPI = "https://hacker-news.firebaseio.com/v0/"

# find traversed parent ids so that replies are not printed more than once
try:
    with open(usedIdsFilePath, "r+") as f:
        usedIds = f.readlines()
        usedIds = [x.strip('\n') for x in usedIds]
except IOError:
    usedIds = []

lastId = None
hasEncounteredLastId = False

pageUrl = "https://news.ycombinator.com/newcomments"

# keep going until we find this id (the last id that hn-sonar saw)
lastId = max(usedIds)

while True:
    r = urllib.urlopen(pageUrl).read()

    soup = BeautifulSoup(r, "lxml")
    nextPageId = soup.find_all("a", attrs={"class": "morelink"})[0]['href']
    nextPageId = re.findall(r'\d+', nextPageId)

    pageUrl = "http://news.ycombinator.com/" + soup.find_all("a", attrs={"class": "morelink"})[0]['href']
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

            if int(nextPageId[0]) < int(lastId):
                hasEncounteredLastId = True

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
    # if the user ids array is empty, then we should not check for previous comments
    # because it would go through all of the pages forever and forever until the beginning
    # of time, which would be bad.
    # It would go forever because there would be no place to stop
    if not shouldContinue or usedIds == [] or not hasEncounteredLastId:
        break
