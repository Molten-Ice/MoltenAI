
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: docs/api_nn.ipynb

import sys
from pathlib import Path
sys.path.append(Path.cwd().parent.as_posix())

from nn.module import Module
from nn.lin import Lin
from nn.relu import Relu
from nn.softmaxCrossEntropy import SoftmaxCrossEntropy
from nn.mse import Mse
from nn.sequentialModel import SequentialModel

class nn():
    @classmethod
    def Lin(self, *args):
        return Lin(*args)
    @classmethod
    def Relu(self, *args):
        return Relu(*args)
    @classmethod
    def SoftmaxCrossEntropy(self, *args):
        return SoftmaxCrossEntropy(*args)
    @classmethod
    def Mse(self, *args):
        return Mse(*args)
    @classmethod
    def Sequential(self, *args):
        return SequentialModel(*args)