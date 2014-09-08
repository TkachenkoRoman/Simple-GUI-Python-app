__author__ = 'Роман'

from computer import computer

class ComputerVector:
    def __init__(self):
        self.computers = []
    def add_computer(self, comp):
        self.computers.append(comp)
    def get_len(self):
        return self.computers.__len__()
    def remove(self, comp):
        self.computers.remove(comp)
