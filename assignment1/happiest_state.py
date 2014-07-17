import json
import sys


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


def getTwittField(twitt, fieldName):
    if twitt.has_key(fieldName) and twitt[fieldName]:
        return twitt[fieldName]

    return ""


def searchTwittForAState(twitt, states):
    place = getTwittField(twitt, "place")
    if place:
        if getTwittField(twitt, "country_code") == 'US':
            locationString = getTwittField(twitt, "full_name")

            for stateList in states:
                for state in stateList:
                    if state in locationString:
                        return stateList

    return None


def main():
    scores = getScoresDict(sys.argv[1])
    twitts = getTwitts(sys.argv[2])
    states = (("Alabama", "AL"), ("Alaska", "AK"), ("Arizona", "AZ"), ("Arkansas", "AR"), ("California", "CA"), ("Colorado", "CO"), ("Connecticut", "CT"), ("Delaware", "DE"), ("Florida", "FL"), ("Georgia", "GA"), ("Hawaii", "HI"), ("Idaho", "ID"), ("Illinois", "IL"), ("Indiana", "IN"), ("Iowa", "IA"), ("Kansas", "KS"), ("Kentucky[C]", "KY"), ("Louisiana", "LA"), ("Maine", "ME"), ("Maryland", "MD"), ("Massachusetts[D]", "MA"), ("Michigan", "MI"), ("Minnesota", "MN"), ("Mississippi", "MS"), ("Missouri", "MO"), ("Montana", "MT"), ("Nebraska", "NE"), ("Nevada", "NV"), ("New Hampshire", "NH"), ("New Jersey", "NJ"), ("New Mexico", "NM"), ("New York", "NY"), ("North Carolina", "NC"), ("North Dakota", "ND"), ("Ohio", "OH"), ("Oklahoma", "OK"), ("Oregon", "OR"), ("Pennsylvania[E]", "PA"), ("Rhode Island[F]", "RI"), ("South Carolina", "SC"), ("South Dakota", "SD"), ("Tennessee", "TN"), ("Texas", "TX"), ("Utah", "UT"), ("Vermont", "VT"), ("Virginia[G]", "VA"), ("Washington", "WA"), ("West Virginia", "WV"), ("Wisconsin", "WI"), ("Wyoming", "WY"), ("District of Columbia", "DC"))

    statesHappiness = dict((x, 0) for x in states)

    for twitt in twitts:
        score = calculateScoreForTweet(scores, getTextFromTwitt(twitt))
        twittState = searchTwittForAState(twitt, states)
        if twittState:
            statesHappiness[twittState] += score

    print max(statesHappiness, key=statesHappiness.get)[1]


def test():
    twitts = getTwitts(sys.argv[2])

    skipCount = 0
    for twitt in twitts:
        if twitt.has_key("place") and twitt["place"]:
            if twitt["place"].has_key("country_code") and twitt["place"]["country_code"] == 'US':
                print " "
                print " "
                print twitt["place"].keys()
                print "------------"
                print twitt["place"]
                skipCount += 1
                if skipCount == 1:
                    break

if __name__ == '__main__':
    main()
