import sys
import json
from collections import defaultdict
import operator


def getTwitts(twitsFileName):
    file = open(twitsFileName)
    return [json.loads(x) for x in file]


def getTextFromTwitt(twitt):
    if twitt.has_key("text"):
        return twitt["text"]
    return ""


def getHashTags(twitt):
    if twitt.has_key("entities") and twitt["entities"]:
        entities = twitt["entities"]
        if entities.has_key("hashtags") and entities["hashtags"]:
            hashtags = entities["hashtags"]
            return [x["text"] for x in hashtags if x.has_key("text") and x["text"]]


def main():
    twitts = getTwitts(sys.argv[1])

    termCounter = defaultdict(int)

    for tweet in twitts:
        hashTags = getHashTags(tweet)
        if hashTags:
            for hashTag in hashTags:
                termCounter[hashTag] += 1

    counter = 0
    sortedDict = sorted(termCounter.iteritems(), key=operator.itemgetter(1), reverse=True)
    for k, v in sortedDict:
        counter += 1
        print k.encode("UTF-8"), v
        if counter >= 10:
            break


if __name__ == '__main__':
    main()
