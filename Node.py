#!/usr/bin/python3

import uuid

class Node():

    # INPUTS:
    #   location    - tuple of grid coordinates for Node
    #   parent      - Node object of parent node
    #
    # VARIABLES:
    #   name        - UUID identifying the node
    #   location    - tuple of grid coordinates for Node
    #   parent      - Node object of parent node
    #   children    - list of child node objects
    #
    def __init__(self, location = tuple(), parent = None):
        self.name = uuid.uuid4()
        self.location = location
        self.parent = parent
        self.children = []

    def changeParent(self):
        pass

    def addChild(self, newNode):
        self.children.append(newNode)

    def removeChild(self):
        pass