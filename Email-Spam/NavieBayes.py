import os
import math

#Bayes class
class Bayes():

    def __init__(self):
        self.V_set = []
        self.prior = []
        self.condprobArr = []
        self.remove_stop = 'no'

    #process the text,remove letter and non-letter
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

    #readFileinFolder method
    def readFileinFolder(self,path):
        wordfile = ''
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                ofp = open(os.path.join(path, filename),"r")
                wordfile += ofp.read()
        return wordfile.split()

     #readFile method
    def readFile(self,path):
        wordfile = ''
        ofp = open(path)
        wordfile = ofp.read()
        return wordfile.split()

    # extact in d & V
    def EXTRACTTOKENSFROMDOC(self,V,d):
        result = []
        for item in d:
            if item not in result and item in V:
                result.append(item)
        return result


    #get the number of the file in the folder
    def getFilenum(self,path):
        fileNum = 0
        for filename in os.listdir(path):
            fileNum += 1
        return fileNum

    #training method 
    def TRAINMULTINOMIALNB(self,Is_Spam,pathSet):
        #prior of spam and ham
        #condprob of each word and [spam or ham]
        prior = []
        condprob = {}
        #D,whole file
        D_data = self.pureWordDic(self.readFileinFolder(pathSet[0]) + self.readFileinFolder(pathSet[1]))
        #get V set of wholefile
        V_set = list(set(D_data))
        #len of V
        V_len = len(V_set)
        #len of total file
        D_len = len(D_data)
        #condprob
        condprobArr = [{},{}]

        for c in Is_Spam:
            #c = 0 or 1
            #total number of spam or ham email
            Nc = self.getFilenum(pathSet[c])
            #prior cal
            prior.append(float(Nc)/(self.getFilenum(pathSet[0])+self.getFilenum(pathSet[1])))

            #current spam or ham file
            textC = self.pureWordDic(self.readFileinFolder(pathSet[c]))


            #cal each word
            for word in V_set:
                Tct = textC.count(word)
                condprobArr[c][word] = float(Tct+1)/(len(textC)+V_len)


        self.V_set = V_set
        self.prior = prior
        self.condprobArr = condprobArr
        return [V_set,prior,condprobArr]

    # filePath = '/Users/liurenchi/Desktop/6375 hw2/test/spam/0073.2003-12-24.GP.spam.txt'
    def APPLYMULTINOMIALNB(self,Is_Spam,V_set,prior,condprobArr,filepath):
        d = bayes.readFile(filepath)
        W = self.EXTRACTTOKENSFROMDOC(V_set,d)
        score = [0,0]
        for c in Is_Spam:
            score[c] = math.log(prior[c])

            for t in W:
                score[c] += math.log(condprobArr[c][t])


        if score[0] > score[1]:
            return 'spam'
        else:
            return 'ham'



    # training process
    def trainBayes(self,pathSet):
        self.TRAINMULTINOMIALNB([0,1],pathSet)
    # check email is spam or ham
    def checkMail(self,filepath):
        result = self.APPLYMULTINOMIALNB([0,1],self.V_set,self.prior,self.condprobArr,filepath)
        return result

    def testBayesAccuracy(self,filepath,result):
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





    path = [spam_path,ham_path]
    #path = ['/Users/liurenchi/Desktop/6375 hw2/train/ham','/Users/liurenchi/Desktop/6375 hw2/train/spam']
    #filePath1 = '/Users/liurenchi/Desktop/6375 hw2/test/ham'
    #filePath2 = '/Users/liurenchi/Desktop/6375 hw2/test/spam'

    bayes = Bayes()
    StopWords = bayes.readFile('stopword.txt')
    bayes.remove_stop = remove_stop
    bayes.trainBayes(path)
    accuracyRate = (bayes.testBayesAccuracy(filePath1,'ham')+bayes.testBayesAccuracy(filePath2,'spam'))/2

    if remove_stop == 'yes':
        print 'after remove stopWord,the accuracyRate is :'
    else:
        print 'before remove stopWord,the accuracyRate is :'

    print accuracyRate





#debug
#filePath = '/Users/liurenchi/Desktop/6375 hw2/test/spam/2211.2004-09-19.GP.spam.txt'
#bayes.APPLYMULTINOMIALNB([0,1],bayes.V_set,bayes.prior,bayes.condprobArr,filePath)
