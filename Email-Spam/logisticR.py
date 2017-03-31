import os
import math
from numpy import *

#logistic class
class logisticRegression():

    def __init__(self):
        self.weigh = 0
        self.wholefile = []
        self.Mat_X = []
        self.Mat_Y = []
        self.remove_stop = 'no'

     #readFile method
    def readFile(self,path):
        wordfile = ''
        ofp = open(path)
        wordfile = ofp.read()
        return wordfile.split()

    #readFileinFolder method
    def readFileinFolder(self,path):
        wordfile = ''
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                ofp = open(os.path.join(path, filename),"r")
                wordfile += ofp.read()
        return wordfile.split()

    #string process , remove stop words
    def pureWordDic(self,wordsdic):

        if self.remove_stop == 'no':
            words = []
            for word in wordsdic:
                if word.isalpha() & (len(word) != 1):
                    if word not in StopWords:
                        words.append(word)
        else:
            words = []
            for word in wordsdic:
                if word.isalpha() & (len(word) != 1):
                        words.append(word)
        return words

    #file process,read all file and save in the matrix
    def fileProcess(self,pathSet):
        wholefile = []

        for path in pathSet:
            wholefile += set(self.pureWordDic(self.readFileinFolder(path)))


        Mat_X = []
        Mat_Y = []
        count = -1
        for path in pathSet:
            count += 1
            for filename in os.listdir(path):
                if filename.endswith('.txt'):
                    ofp = open(os.path.join(path, filename),"r")
                    wordfile = set(self.pureWordDic(ofp.read().split()))

                    Mat_Y.append(count)
                    Ver_X = []
                    countword = 0
                    for item in wholefile:
                        if item in wordfile:
                            Ver_X.append(1)
                        else:
                            Ver_X.append(0)
                    Mat_X.append(Ver_X)

        self.wholefile = wholefile
        self.Mat_X = Mat_X
        self.Mat_Y = Mat_Y


    #logistic&sigmoid function
    def sigmoid(self,inX):
        return 1.0/(1+exp(-inX))


    #gradAscent method
    def gradAscent(self,dataArray,labelArray,alpha,maxCycles,lambda_value):
        dataMat=mat(dataArray)    #size:m*n
        labelMat=mat(labelArray).transpose()      #size:m*1
        m,n=shape(dataMat)
        weigh=ones((n,1))

        count = 0
        for i in range(maxCycles):
            h=self.sigmoid(dataMat*weigh)
            error=labelMat-h    #size:m*1
            old_weigh = weigh
            weigh=weigh+alpha*dataMat.transpose()*error - lambda_value*alpha*weigh
            if (weigh - old_weigh).all() < 0.001:
                break
        self.weigh = weigh
        return weigh

    #training method
    def train_LR(self,pathSet,alpha,maxCycles,lambda_value):
        self.fileProcess(pathSet)
        self.gradAscent(self.Mat_X,self.Mat_Y,alpha,maxCycles,lambda_value)

    #check the spam of ham
    def verify_file(self,path,wholefile,weigh):

        wordfile = self.pureWordDic(self.readFile(path))

        Ver_X = []
        countword = 0
        for item in wholefile:
            if item in wordfile:
                Ver_X.append(1)
            else:
                Ver_X.append(0)

        weigh = weigh.transpose()
        Ver_X = mat(Ver_X).transpose()
        Y_value = float(self.sigmoid(weigh*Ver_X))
        if Y_value > 0.5:

            return 'spam'

        else:

            return 'ham'

    #check mail
    def checkMail(self,filepath):
        return self.verify_file(filepath,self.wholefile,self.weigh)


    #accuracy rate
    def testLRAccuracy(self,filepath,result):
        scuessNum = 0
        totalNum = 0
        for filename in os.listdir(filepath):
                if filename.endswith('.txt'):
                    totalNum +=1
                    path = os.path.join(filepath, filename)
                    if result == self.checkMail(path):
                        scuessNum += 1
        return  float(scuessNum) / totalNum

if __name__ == "__main__":

        #ham_path = input("please input  ham train data :")
        #spam_path = input("please input  spam train data :")
        #filePath1 = input("please input ham test data path:")
        #filePath2 = input("please input spam test data path:")
        print 'automatically add path:'
        pathSet = ['train/ham','train/spam','test/ham','test/spam']
        for p in pathSet:
            print p
        ham_path = pathSet[0]
        spam_path = pathSet[1]
        filePath1 = pathSet[2]
        filePath2 = pathSet[3]


        remove_stop = raw_input("remove stopWord or not?(yes/no):")
        learning_rate = raw_input("input your leaning rate (such as 0.01,0.025,0.05):")
        running_time = raw_input("input your running_time number (such as 50,100,500):")
        lambda_value = raw_input("input your lambda_value number (such as 0.01,0.1,0.5):")







        path = [ham_path,spam_path]
        #path = ['/Users/liurenchi/Desktop/6375 hw2/train/ham','/Users/liurenchi/Desktop/6375 hw2/train/spam']
        #filePath1 = '/Users/liurenchi/Desktop/6375 hw2/test/ham'
        #filePath2 = '/Users/liurenchi/Desktop/6375 hw2/test/spam'

        logic = logisticRegression()
        StopWords = logic.readFile('stopword.txt')
        logic.remove_stop = remove_stop
        logic.train_LR(path,float(learning_rate),int(running_time),float(lambda_value))
        accuracyRate = (logic.testLRAccuracy(filePath1,'ham')+logic.testLRAccuracy(filePath2,'spam'))/2

        if remove_stop == 'yes':
            print 'after remove stopWord,the accuracyRate is :'
        else:
            print 'before remove stopWord,the accuracyRate is :'

        print accuracyRate
"""
# test main
if __name__ == "__main__":
        print 'automatically add path:'
        pathSet = ['train/ham','train/spam','test/ham','test/spam']
        for p in pathSet:
            print p
        ham_path = pathSet[0]
        spam_path = pathSet[1]
        filePath1 = pathSet[2]
        filePath2 = pathSet[3]
        remove_stop = ['yes','no']
        learning_rate = 0.05
        running_time = [50,100,500]
        lambda_value = [0.01,0.1,0.5]

        result = []
        path = [ham_path,spam_path]
        for time in running_time:
            resultlime = []
            for lam in lambda_value:

                for stop in remove_stop:
                    logic = logisticRegression()
                    StopWords = logic.readFile('stopword.txt')
                    logic.remove_stop = stop
                    logic.train_LR(path,learning_rate,time,lam)
                    accuracyRate = (logic.testLRAccuracy(filePath1,'ham')+logic.testLRAccuracy(filePath2,'spam'))/2
                    resultlime.append(accuracyRate)

            result.append(resultlime)


        for item in result:
            print item
"""
