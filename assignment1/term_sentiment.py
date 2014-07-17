import sys
import json
from collections import defaultdict


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def getScoresDict(scoresFileName):
    file = open(scoresFileName)
    scores = {}
    for line in file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def getTwitts(twitsFileName):
    file = open(twitsFileName)
    return [json.loads(x) for x in file]


def calculateScoreForTweet(scores, twitt):
    totalScore = 0
    for word in twitt.split(" "):
        if scores.has_key(word):
            totalScore += scores[word]
    return totalScore


def getTextFromTwitt(twitt):
    if twitt.has_key("text"):
        return twitt["text"]
    return ""


def main():
    alpha = .1

    scores = getScoresDict(sys.argv[1])
    twitts = getTwitts(sys.argv[2])
    twittScores = [(getTextFromTwitt(x), calculateScoreForTweet(scores, getTextFromTwitt(x))) for x in twitts]

    assignedScores = defaultdict(int)

    for twitt in twitts:
        text = getTextFromTwitt(twitt)
        score = calculateScoreForTweet(scores, text)

        for word in text.split(" "):
            if not scores.has_key(word):
                # Grade word as current twitt score
                assignedScores[word] += score * alpha
    for k, v in assignedScores.iteritems():
        print "%s %g" % (k.encode("UTF-8"), v)

if __name__ == '__main__':
    main()
