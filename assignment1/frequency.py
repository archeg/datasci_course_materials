import sys
import json
from collections import defaultdict


def getTwitts(twitsFileName):
    file = open(twitsFileName)
    return [json.loads(x) for x in file]


def getTextFromTwitt(twitt):
    if twitt.has_key("text"):
        return twitt["text"]
    return ""


def main():
    twitts = getTwitts(sys.argv[1])

    termCounter = defaultdict(float)
    for twitt in twitts:
        for term in getTextFromTwitt(twitt).split():
            termCounter[term] += 1.

    allTermsCounter = len(termCounter.keys())

    for k, v in termCounter.iteritems():
        print k.encode("UTF-8"), (v / allTermsCounter)


if __name__ == '__main__':
    main()
