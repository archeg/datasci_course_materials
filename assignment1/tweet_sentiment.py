import sys
import json

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
    scores = getScoresDict(sys.argv[1])
    twitts = getTwitts(sys.argv[2])
    resultScores = [calculateScoreForTweet(scores, getTextFromTwitt(x)) for x in twitts]
    for result in resultScores:
        print(result)

if __name__ == '__main__':
    main()
