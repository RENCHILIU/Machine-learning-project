
__ All in Python 2.7, with pandas lib__

# Description:
    decision tree algorithm. using two heuristic functions to build the decision trees 

    also implement the post-pruned for each tree.


### running method:	python decision.py### 3-rd part library 	using pandas to take care of the csv file.	need install pandas to run this code	please use pip install pandas  to install pandas### input parameter:

    L and K are parameters for the pruning algorithm 
    **(see the task detial.pdf)**
        L : int value    K : int value    output or not : only can be yes or no    test_path:  ~data_sets1/test_set.csv    train_path: ~data_sets1/training_set.csv    validte_path:  ~data_sets1/validation_set.csv### Main Function_describe:    def IDThreeAlg(dataframe,target_Attr,AttrList,num)    Information gain heuristic without post pruning    def Impurity_Alg(dataframe,target_Attr,AttrList,num)
    Information gain heuristic without post pruning    def testAccuracy(tree,dataframe)    the accuracy func,conpare the leaf_value form findTree_Leaf with    dataframe['Class']'s value    def postpruning_Alg(integer_L,integer_K,tree,dataframe,accuracy_per)    post pruning function ### accuracy:    using decision_Tree_ALG: accuracy is 0.7465    using Impurity_Alg: accuracy is 0.765



