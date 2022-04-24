#!/usr/bin/python3

from Node import Node

# INPUTS:
#   root        - Node object representing the root of the tree
#   path        - list of (node objects/tuples of locations) representing the path to the goal
# 
# VARIABLES:
#   root        - Node object representing the root of the tree
#   path        - list of (node objects/tuples of locations) representing the path to the goal
#   treeFile    - string of path to file to output the tree to
#
class Tree():
    def __init__(self, root = Node()):
        self.root = root
        self.path = None

        self.treePath = "Output/Tree.txt"
        self.outputFile = open(self.treePath, "w")
        self.outputFile.close()

    def addNode(self, newNode, curNode = None):
        if curNode == None:
            curNode = self.root
        
        curNode.addChild(newNode)

    def createTreeStr(self, curNode, lvl):
        nodestr = '\t'*lvl + str(curNode.name) + '\n'

        for child in curNode.children:
            nodestr += self.createTreeStr(child, lvl + 1)

        return nodestr

    def printTree(self):
        self.outputFile = open(self.treePath, "a")
        trStr = self.createTreeStr(self.root, 0) 
        self.outputFile.write(trStr)
        self.outputFile.close()
        