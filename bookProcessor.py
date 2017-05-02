def freq(w, l):
    return reduce(lambda a,b: a + b, map(lambda x: 1 if x == w else 0, l))

def groupFreq(wL, l):
    return reduce(lambda a,b: a + b, map(lambda x: 1 if x in wL else 0, l))

#turn list into list of frequencies with list comp
#def maxFreqWord(l):
#    wordFreq = {}
#    return reduce(lambda a,b: a if a > b else b, wordFreq)


def freqFile(w, filename):
    with open (filename, "r") as myfile:
        data=myfile.read()
        print "Frequency of " + w + ": " + str(freq(w, data.split(" ")))
    
def groupFreqFile(wL, filename):
    with open (filename, "r") as myfile:
        data=myfile.read()
        print "Group frequency of " + wL + ": " + str(groupFreq(wL.split(" "), data.split(" ")))
    
def maxFreqWordFile(filename):
    with open (filename, "r") as myfile:
        data = myfile.read()
        print "Max frequency word: " + maxFreqWord(data.split(" "))


freqFile("the", "mobyDick.txt")
