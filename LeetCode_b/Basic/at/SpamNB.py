# -*- coding: utf-8 -*-
"""
Created on

@author: Don
"""
import re
import random
from array import array
import numpy as np


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


def createVocabList(dataset):
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my vocabulary!" % word)
    return returnVec


def trainNB(trainMat, trainCat):
    numTrainDoc = len(trainMat)
    # print("--" + str(numTrainDoc))
    numWords = len(trainMat[0])
    pAbusive = sum(trainCat) / float(numTrainDoc)
    # print(pAbusive)
    p0Num = np.zeros(numWords)
    p1Num = np.zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDoc):
        if trainCat[i] == 1.0:
            p1Num += trainMat[i]
            # print(p1Num)
            p1Denom += sum(trainMat[i])
        else:
            p0Num += trainMat[i]
            # print(p0Num)
            p0Denom += sum(trainMat[i])
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p1Denom
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    p1 = sum(vec2Classify * p1Vect) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vect) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def textParse(bigStr):
    regEx = re.compile('\\W*')
    listOfTokens = re.split(regEx, bigStr)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    f = line_reader('../dataset/spam_train.txt')
    line = next(f)  # next(iterator[, default])    Return the next item from the iterator.
    print('loading training set...')
    cnt = 0
    while line:
        content = re.split('\s+', line)
        doc = content[1]
        score = float(content[0])
        docList.append(doc)
        classList.append(score)
        cnt += 1
        line = next(f)

    trainVocabList = createVocabList(docList)
    # print(len(wordList))
    testSet = []
    testClassList = []
    f = line_reader('../dataset/spam_test.txt')
    line = next(f)  # next(iterator[, default])    Return the next item from the iterator.
    print('loading test set...')
    while line:
        content = re.split('\s+', line)
        doc = content[1]
        score = float(content[0])
        testSet.append(doc)
        testClassList.append(score)
        line = next(f)

    trainMat = []
    trainClass = []
    for docIdx in range(len(docList)):
        trainMat.append(setOfWords2Vec(trainVocabList, docList[docIdx]))
        trainClass.append(classList[docIdx])
    p0V, p1V, pSpam = trainNB(np.array(trainMat), np.array(trainClass))
    # print(p0V, p1V, pSpam)

    testVocabList = createVocabList(testSet)
    errorCnt = 0
    print(len(testSet))
    for docIdx in range(len(testSet)):
        wordVect = setOfWords2Vec(testVocabList, testSet[docIdx])

        if classifyNB(np.array(wordVect), p0V, p1V, pSpam) != testClassList[docIdx]:
            # print(classifyNB(np.array(wordVect), p0V, p1V, pSpam))
            # print(testClassList[docIdx])
            errorCnt += 1
    print("the error rate is : ", float(errorCnt) / len(testSet))


if __name__ == '__main__':
    spamTest()
