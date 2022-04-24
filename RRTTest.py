#!/usr/bin/python3

from Tree import Tree
from Node import Node

testTree = Tree()
testNode1 = Node()
testNode2 = Node()
testTree.addNode(testNode1)
testTree.addNode(testNode2)
testNode3 = Node()
testNode4 = Node()
testNode5 = Node()
testNode6 = Node()
testTree.addNode(testNode3, testNode1)
testTree.addNode(testNode4, testNode1)
testTree.addNode(testNode5, testNode2)
testTree.addNode(testNode6, testNode2)

testTree.printTree()