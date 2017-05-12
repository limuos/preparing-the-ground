from nltk.corpus import sentiwordnet as swn

# n - NOUN
# v - VERB
# a - ADJECTIVE
# s - ADJECTIVE SATELLITE
# r - ADVERB

posFile = open("posScore.txt", "w")
negFile = open("negScore.txt", "w")
objFile = open("objScore.txt", "w")

errorLog = open("errorLog.txt", "w")

condition = 0

for line in open("sampleBengFormat.txt", encoding="utf-8").read().split("\n"):
    tokens = line.split(",")

    testLex = str(tokens[0].strip()) + "." + str(tokens[1].strip()) + "." + "01"    # test with lexicon posTag
    testAdj = str(tokens[0].strip()) + ".a." + "01"   # test with adjective tag
    testAdv = str(tokens[0].strip()) + ".r." + "01"   # test with adverb tag
    testVrb = str(tokens[0].strip()) + ".v." + "01"   # test with verb tag
    testNou = str(tokens[0].strip()) + ".n." + "01"   # test with noun tag
    testAds = str(tokens[0].strip()) + ".s." + "01"   # test with adjective satellite tag

    try:
        posFile.write(str(swn.senti_synset(testLex).pos_score())+"\n")
        negFile.write(str(swn.senti_synset(testLex).neg_score())+"\n")
        objFile.write(str(swn.senti_synset(testLex).obj_score())+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : " + str(tokens[1].strip()) + "\n")

    try:
        posFile.write(str(swn.senti_synset(testAdj).pos_score())+"\n")
        negFile.write(str(swn.senti_synset(testAdj).neg_score())+"\n")
        objFile.write(str(swn.senti_synset(testAdj).obj_score())+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : a\n")

    try:
        posFile.write(str(swn.senti_synset(testAdv).pos_score())+"\n")
        negFile.write(str(swn.senti_synset(testAdv).neg_score())+"\n")
        objFile.write(str(swn.senti_synset(testAdv).obj_score())+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : r\n")

    try:
        verbTagPos = swn.senti_synset(testVrb).pos_score()
        verbTagNeg = swn.senti_synset(testVrb).neg_score()
        verbTagObj = swn.senti_synset(testVrb).obj_score()
        posFile.write(str(verbTagPos)+"\n")
        negFile.write(str(verbTagNeg)+"\n")
        objFile.write(str(verbTagObj)+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : v\n")

    try:
        posFile.write(str(swn.senti_synset(testNou).pos_score())+"\n")
        negFile.write(str(swn.senti_synset(testNou).neg_score())+"\n")
        objFile.write(str(swn.senti_synset(testNou).obj_score())+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : n\n")

    try:
        posFile.write(str(swn.senti_synset(testAds).pos_score())+"\n")
        negFile.write(str(swn.senti_synset(testAds).neg_score())+"\n")
        objFile.write(str(swn.senti_synset(testAds).obj_score())+"\n")
        continue
    except:
        errorLog.write(str(tokens[0].strip()) + " not found with POS Tag : s\n")

    posFile.write("NF\n")
    negFile.write("NF\n")
    objFile.write("NF\n")
    errorLog.write("\n")


posFile.close()
negFile.close()
objFile.close()
errorLog.close()

print("PROGRAM SUCCESSFULLY EXECUTED")