#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from math import log


# In[3]:


df = pd.read_csv('./example_data.csv', dtype={'windy': 'str'})
df


# In[5]:


def entropy(ele):
    probs = [ele.count(i)/len(ele) for i in set(ele)]
    entropy = -sum([prob*log(prob, 2) for prob in probs])
    return entropy


# In[6]:


entropy(df['play'].tolist())


# In[7]:


def split_dataframe(data, col):
    unique_values = data[col].unique()
    result_dict = {elem : pd.DataFrame for elem in unique_values}
    for key in result_dict.keys():
        result_dict[key] = data[:][data[col] == key]
    return result_dict

split_example = split_dataframe(df, 'temp')


# In[8]:


for item, value in split_example.items():
    print(item, value)


# In[9]:


def choose_best_col(df, label):
    entropy_D = entropy(df[label].tolist())
    cols = [col for col in df.columns if col not in [label]]
    max_value, best_col = -999, None
    max_splited = None
    for col in cols:
        splited_set = split_dataframe(df, col)
        entropy_DA = 0
        for subset_col, subset in splited_set.items():
            entropy_Di = entropy(subset[label].tolist())
            entropy_DA += len(subset)/len(df) * entropy_Di
        info_gain = entropy_D - entropy_DA
        
        if info_gain > max_value:
            max_value, best_col = info_gain, col
            max_splited = splited_set
    return max_value, best_col, max_splited
    
choose_best_col(df, 'play')


# In[14]:


class ID3Tree:
    class Node:
        def __init__(self, name):
            self.name = name
            self.connections = {}

        def connect(self, label, node):
            self.connections[label] = node
            
    def __init__(self, data, label):
        self.columns = data.columns
        self.data = data
        self.label = label
        self.root = self.Node("Root")
        
    def print_tree(self, node, tabs):
        print(tabs + node.name)
        for connection, child_node in node.connections.items():
            print(tabs + "\t" + "(" + connection + ")")
            self.print_tree(child_node, tabs + "\t\t")

    def construct_tree(self):
        self.construct(self.root, "", self.data, self.columns)
        
    def construct(self, parent_node, parent_connection_label, input_data, columns):
        max_value, best_col, max_splited = choose_best_col(input_data[columns], self.label)
        
        if not best_col:
            node = self.Node(input_data[self.label].iloc[0])
            parent_node.connect(parent_connection_label, node)
            return

        node = self.Node(best_col)
        parent_node.connect(parent_connection_label, node)
        
        new_columns = [col for col in columns if col != best_col]
        
        for splited_value, splited_data in max_splited.items():
            self.construct(node, splited_value, splited_data, new_columns)


# In[23]:


tree1 = ID3Tree(df, 'play')
tree1.construct_tree()


# In[24]:


tree1.print_tree(tree1.root, "")


# In[25]:


from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
clf.predict([[2, 2]])


# In[32]:


from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best')
clf = clf.fit(iris.data, iris.target)


# In[33]:


import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('iris')


# In[34]:


dot_data = tree.export_graphviz(clf, out_file=None,
                               feature_names=iris.feature_names,
                               class_names=iris.target_names,
                               filled=True, 
                               rounded=True,
                               special_characters=True)
graph = graphviz.Source(dot_data)
graph


# In[ ]:




