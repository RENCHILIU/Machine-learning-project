
# coding: utf-8



import pandas as pd
from pandas import DataFrame,Series
import math
import random
import copy



#return the size of data in @attribute
def countSize(attrName,dataframe):
    return dataframe[attrName].values.size



#return the number of @value in @attribute
def findValinAttr(attrName,value,dataframe):
    count = 0
    for val in dataframe[attrName].values:
        if val == value:
            count = count + 1
    return count




#filter the dataframe to small one according to the attribute value
def dataframe_Filter(attrName,value,dataframe):
    #value can only meaningfully be 0 or 1
    return dataframe[dataframe[attrName] == value]



#get all attributes in the dataframe
def getAllAttr(dataframe):
    return dataframe.columns.values



#calculate the Entropy 
def calEntropy(dataframe):
    if countSize('Class',dataframe) == 0:
        return 1
    p1 = float(findValinAttr('Class',1,dataframe))/countSize('Class',dataframe)
    p2 = 1 - p1
    if p1 == 1 or p1 ==0:
        return 0
    result = -p1 * math.log(p1,2) -p2 * math.log(p2,2)
    return result




#calculate the information gain, Gain(S, A)
def calGain(attrName,dataframe):
    
    x0 = float(findValinAttr(attrName,0,dataframe))/countSize(attrName,dataframe)
    x1 = 1 - x0
    
    result = x0 * calEntropy(dataframe_Filter(attrName,0,dataframe))
    result = result + x1 * calEntropy(dataframe_Filter(attrName,1,dataframe))
    result = calEntropy(dataframe) - result
    
    return result



#delete the item in one list but don't change original list
def delItem_List(item,list_):
    list1 = []
    for val in list_:
        if val != item:
            list1.append(val)
    return list1




# check if the data in one attribute is all equal the @value
def sameIteminAttr(attrName,value,dataframe):
    result = True
    for val in dataframe[attrName].values:
        if val != value:
            result = False
    return result




# print DecisionTree as required
def printDecisionTree(tree):
    for val in tree:
        if val == ' ':
            print ' '
        print val,




#reform the decisionTree_List to the new list in order to store in the real tree
#return reformed tree_list
def reform_Tree(tree):
    decision_T = []
    index = 0
    while index != len(tree):
        temp = ' '
        for i in range(index,len(tree)):
            if tree[i] == ' ':
                decision_T.append(temp)
                index = i+1
                break
            temp = temp + tree[i]
        
    return decision_T[1:len(decision_T)]




#Information gain heuristic without post pruning
def IDThreeAlg(dataframe,target_Attr,AttrList,num):
    #base case:
    if sameIteminAttr('Class',0,dataframe):
        decisionTree_List.append('0')
        decisionTree_List.append(' ')
        #print (0)
        return
    if sameIteminAttr('Class',1,dataframe):
        decisionTree_List.append('1')
        decisionTree_List.append(' ')
        #print (1)
        return
    
    #----
    #use the information gain, Gain(S, A) find the best attribute
    result = 0
    for item in AttrList:
        temp = calGain(item,dataframe)
        if temp > result:
            result = temp
            bestAttr = item 
    #---      
    AttrList2 = delItem_List(bestAttr,AttrList)
    num = num+1
    decisionTree_List.append(' ')
    #print ' '
    
    #---0
    #when sub-attribute is 0
    if findValinAttr(bestAttr,0,dataframe) != 0:
        for i in range(num):
            decisionTree_List.append('|')
            #print('|'),
        decisionTree_List.append('%s=0:' % bestAttr)
        #print ('%s=0:' % bestAttr),
        IDThreeAlg(dataframe_Filter(bestAttr,0,dataframe),bestAttr,AttrList2,num)
    #---1
    #when sub-attribute is 1
    if findValinAttr(bestAttr,1,dataframe) != 0:
        for i in range(num):
            decisionTree_List.append('|')
            #print('|'),
        decisionTree_List.append('%s=1:' % bestAttr)
        #print ('%s=1:' % bestAttr),
        IDThreeAlg(dataframe_Filter(bestAttr,1,dataframe),bestAttr,AttrList2,num)
    



#tree class
class BinaryTree:
    def __init__(self,rootObj):
        self.val = rootObj
        self.leftChild = None
        self.rightChild = None


    def insertNode(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            self.rightChild = BinaryTree(newNode)
    def fitChild(self,val):
       
        if self.leftChild == None:
            return self
        if self.leftChild.val == val:
            return self.leftChild
        if self.rightChild == None:
            return self
        if self.rightChild.val == val:
            return self.rightChild

        
        




#analize the output decisionTree_List , inorder to help func: convert_To_tree
def analListNode(ListNode):
    result1 = 0     #number of |
    result2 = ''    #attribute name
    result3 = ''    #attribute's node
    result4 = ''    #final value
    for i in range(0,len(ListNode)):
        if ListNode[i] == '|':
            result1 = result1+1
        if ListNode[i] == 'X':
            result2 = ListNode[i] + ListNode[i+1]
        if (ListNode[i] == '0' or ListNode[i] == '1') and ListNode[i-1] == '=':
            result3 = ListNode[i]
        if (ListNode[i] == '0' or ListNode[i] == '1') and ListNode[i-1] == ':':
            result4 = ListNode[i]
    return{'num':result1,'val':result2,'node':result3,'ans':result4}
            
            
        



#help to convert the convert_To_tree to the real tree
def convert_To_tree(tree,treelist,n):
    #base case:
    if len(treelist) == 0:
        return
    dic = analListNode(treelist.pop(0))

    
    if dic['num'] > n:

        tree.insertNode(dic['val'])
        tree.leftChild.insertNode(dic['node'])
        if dic['ans'] != '':
            tree.leftChild.leftChild.insertNode(dic['ans'])
        dic = convert_To_tree(tree.leftChild.leftChild,treelist,dic['num'])

        # if dic != None and dic['num'] == n:
        tree.leftChild.insertNode(dic['node'])
        if dic['ans'] != '':
            tree.leftChild.rightChild.insertNode(dic['ans'])
        dic = convert_To_tree(tree.leftChild.rightChild,treelist,dic['num'])
    
    if dic != None and dic['num'] == n:
        return dic
    else :
      
        return dic
    



#input one row data in dataframe, use the tree to find the tree's leaf node
def findTree_Leaf(row,tree,dataframe):
    while tree!= None and tree.leftChild != None and tree.leftChild.leftChild != None:
        tree = tree.fitChild(str(dataframe.ix[row][tree.val])).leftChild
    return tree.val




#the accuracy func,conpare the leaf_value form findTree_Leaf with dataframe['Class']'s value
def testAccuracy(tree,dataframe):
    accu = 0
    for i in range(0,dataframe.index.values.size):
        if findTree_Leaf(i,tree,dataframe) == str(dataframe['Class'][i]):
            accu = accu + 1
          
    result = float(accu)/dataframe.index.values.size
    return result
    




def calImpurity(dataframe):
    if countSize('Class',dataframe) == 0:
        return 1
    p1 = float(findValinAttr('Class',0,dataframe))/countSize('Class',dataframe)
    p2 = 1 - p1
    if p1 == 1 or p1 ==0:
        return 0
    result = p1 * p2
    return result



def calImpurityGain(attrName,dataframe):
    
    x0 = float(findValinAttr(attrName,0,dataframe))/countSize(attrName,dataframe)
    x1 = 1 - x0
    
    result = x0 * calImpurity(dataframe_Filter(attrName,0,dataframe))
    result = result + x1 * calImpurity(dataframe_Filter(attrName,1,dataframe))
    result = calImpurity(dataframe) - result
    
    return result





#Information gain heuristic without post pruning
def Impurity_Alg(dataframe,target_Attr,AttrList,num):
    #base case:
    if sameIteminAttr('Class',0,dataframe):
        decisionTree_List2.append('0')
        decisionTree_List2.append(' ')
        return
    if sameIteminAttr('Class',1,dataframe):
        decisionTree_List2.append('1')
        decisionTree_List2.append(' ')
        return
    
    #----
    #use the information gain, Gain(S, A) find the best attribute
    result = 0
    for item in AttrList:
        temp = calImpurityGain(item,dataframe)
        if temp > result:
            result = temp
            bestAttr = item 
    #---      
    AttrList2 = delItem_List(bestAttr,AttrList)
    num = num+1
    decisionTree_List2.append(' ')
    
    #---0
    #when sub-attribute is 0
    if findValinAttr(bestAttr,0,dataframe) != 0:
        for i in range(num):
            decisionTree_List2.append('|')
            #print('|'),
        decisionTree_List2.append('%s=0:' % bestAttr)
        Impurity_Alg(dataframe_Filter(bestAttr,0,dataframe),bestAttr,AttrList2,num)
    #---1
    #when sub-attribute is 1
    if findValinAttr(bestAttr,1,dataframe) != 0:
        for i in range(num):
            decisionTree_List2.append('|')
            #print('|'),
        decisionTree_List2.append('%s=1:' % bestAttr)
        Impurity_Alg(dataframe_Filter(bestAttr,1,dataframe),bestAttr,AttrList2,num)

def cutTree(tree,dataframe,subTree,value):
    if tree == None or tree.val== '1' or  tree.val== '0':
        return
   
    if tree == subTree:
        tree.leftChild = BinaryTree(str(value))
    
    cutTree(tree.leftChild.leftChild,dataframe_Filter(tree.val,int(tree.leftChild.val),dataframe),subTree,value)
    cutTree(tree.rightChild.leftChild,dataframe_Filter(tree.val,int(tree.leftChild.val),dataframe),subTree,value)
    #print tree.rightChild.rightChild.val
    




#get the all subTree of on Tree and return most value in datafram['Class']
def middle_Scan(tree,dataframe,subTreeSet):
    if tree == None or tree.val== '1' or  tree.val== '0':
        return
    if findValinAttr('Class',0,dataframe) > findValinAttr('Class',1,dataframe):
        zero_value = 0
    else:
        zero_value = 1
    subTreeSet.append([tree,zero_value])
    middle_Scan(tree.leftChild.leftChild,dataframe_Filter(tree.val,int(tree.leftChild.val),dataframe),subTreeSet)
    middle_Scan(tree.rightChild.leftChild,dataframe_Filter(tree.val,int(tree.leftChild.val),dataframe),subTreeSet)
    #print tree.rightChild.rightChild.val



#get the all subTree of on Tree and return the nmuber of zero in datafram['Class']
def findSubTree(tree,dataframe):
    subTreeSet = []
    middle_Scan(tree,dataframe,subTreeSet)
    return subTreeSet



#post pruning function 
def postpruning_Alg(integer_L,integer_K,tree,dataframe,accuracy_per):
    #build a decision tree
    #bestTree
    for i in range(1,integer_L+1):
        #deep copy
        tree2 = copy.deepcopy(tree)
        integer_M = random.randint(1,integer_K)
        for j in range(1,integer_M+1):
            tree_list = findSubTree(tree2,dataframe)
            n = len(tree_list)
            integer_P = random.randint(0,n-1)
            cutTree(tree2,dataframe,tree_list[integer_P][0],tree_list[integer_P][1])

        if testAccuracy(tree2,dataframe_validate) > accuracy_per:
            tree = copy.deepcopy(tree2)
          
    return tree
            




if __name__ == "__main__":
    input_L = input("please input L value:")
    input_K = input("please input K value:")
    input_ouputorNot = raw_input("output or not?(yes/no):")
    test_path = raw_input("input test_path")
    train_path = raw_input("input train_path")
    validte_path = raw_input("input validte_path")
    
    #data_open
    dataframe_test =  pd.read_csv(test_path)
    dataframe_train = pd.read_csv(train_path)
    dataframe_validate = pd.read_csv(validte_path)

    #decision_Tree_ALG (using training set)
    decisionTree_List = []
    list1 = getAllAttr(dataframe_train)
    list2 = delItem_List('Class',list1)
    IDThreeAlg(dataframe_train,'Class',list2,-1)
    dt = reform_Tree(decisionTree_List)
    mytree = BinaryTree('root')
    convert_To_tree(mytree, dt, -1)
    mytree = mytree.fitChild('XO')
    
    #Impurity_Alg (using training set)
    decisionTree_List2 = []
    list1 = getAllAttr(dataframe_train)
    list2 = delItem_List('Class',list1)
    Impurity_Alg(dataframe_train,'Class',list2,-1)
    dt2 = reform_Tree(decisionTree_List2)
    mytree2 = BinaryTree('root')
    convert_To_tree(mytree2, dt2, -1)
    mytree2 = mytree2.fitChild('XO')
    
    
    #test_accuracyFunc (using testing set)
    accu_1 = testAccuracy(mytree,dataframe_test)
    accu_2 = testAccuracy(mytree,dataframe_test)
    
    #post pruningFunc(using validate set)
    
    post_tree1 = postpruning_Alg(int(input_L),int(input_K),mytree,dataframe_validate,accu_1)
    post_tree2 = postpruning_Alg(int(input_L),int(input_K),mytree2,dataframe_validate,accu_2)
    
    #test_accuracyFunc after posting (using validate set)
    accu_3 = testAccuracy(post_tree1,dataframe_validate)
    accu_4 = testAccuracy(post_tree2,dataframe_validate)
    
    
    #printFunc
    if input_ouputorNot == 'yes':
        print '------------------'
        print ('using decision_Tree_ALG: accuracy is %s' % accu_1)
        print ('using Impurity_Alg: accuracy is %s' % accu_2)
        print '------------------'
        print ('decision_Tree_ALG after post:the accuracy is %s' % accu_3)
        print ('Impurity_Alg after post:accuracy is %s' % accu_4)
        print '------------------'
        printDecisionTree(decisionTree_List)
        print '------------------'
        printDecisionTree(decisionTree_List2)
        
    
    
    


