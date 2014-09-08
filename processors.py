__author__ = 'Роман'

class ProcessorVector:
    def __init__(self):
        self.processors = []
    def add_processor(self, proc):
        self.processors.append(proc)
    def get_len(self):
        return self.processors.__len__()
    def remove(self, proc):
        self.processors.remove(proc)
