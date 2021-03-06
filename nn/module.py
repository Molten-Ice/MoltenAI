
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/nn_module.ipynb

class Module():
    def __repr__(self):
        repr = "Model(" + "\n"
        for i, l in enumerate (self.layers):
            repr+= f"(layer_{i}):" + str(l) + "\n"
        repr+=f"(layer_{i+1}):" + str(self.loss) + "\n"
        repr+=")"
        return repr

    def parameters(self):
        for l in self.layers:
            for p in l.parameters(): yield p

    def update_parameters(self, lr):
        for parameter in self.parameters():
            parameter-=lr*parameter.g

    def __call__(self, x, targ):
        for l in self.layers: x = l(x)
        return self.loss(x, targ)

    def forward(self, x):
        for l in self.layers: x = l(x)
        return self.loss.softmax_forward(x)

    def backward(self, y_train):
        self.loss.backward()
        for l in reversed(self.layers): l.backward()