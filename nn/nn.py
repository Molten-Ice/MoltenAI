
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: docs/nn_nn.ipynb

import sys
from pathlib import Path
sys.path.append(Path.cwd().parent.as_posix())

from nn.lin import Lin
from nn.relu import Relu
from nn.softmaxCrossEntropy import SoftmaxCrossEntropy
from nn.mse import Mse

class nn():
    @classmethod
    def Lin(*args):
        self.Lin = Lin(*args)
    @classmethod
    def Relu(*args):
        self.Relu = Relu(*args)
    @classmethod
    def softmaxCrossEntropy(*args):
        self.softmaxCrossEntropy = softmaxCrossEntropy(*args)
    @classmethod
    def Mse(*args):
        self.Mse = Mse(*args)