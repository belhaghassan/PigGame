#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-4
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#

"""Player class for our Pig Game."""

class Player:
    def __init__(self, name):
        self._name = name
    
    @property
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._name
    def name(self):
        return self._name


