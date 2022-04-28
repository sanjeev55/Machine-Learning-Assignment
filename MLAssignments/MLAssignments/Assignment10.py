
import numpy as np
np.set_printoptions(threshold=10) # printing setup
import matplotlib.pyplot as plt


# This formula shall be imitated by the neural network
def formula_1(x):
    return x + 0.75

# This formula shall be imitated by the neural network, too
def formula_2(x):
    return(np.sin(x) + 0.5)


# Input data
X = np.random.uniform(low=-0.5, high=1.55, size=100)# make 100 uniformly distributed samples
X = X.reshape(-1, 1) # -1 indicates "as many rows as required"
X # input data as column vector

# Target values with formula_1
y_1 = np.array([formula_1(x) for x in X.flatten()]) # one output per sample, |X|-many samples
y_1 = y_1.reshape(-1, 1)
y_1 # target data as column vector


# Target values with formula_2
y_2 = np.array([formula_2(x) for x in X.flatten()]) # one output per sample, |X|-many samples
y_2 = y_2.reshape(-1, 1)
y_2 # target data as column vector


# ### Code below contains the parts to be edited

# Simple neural-network based regressor
class NeuralNetwork:
    
    # Function called at object initialization
    def __init__(self):
        
        # These are members of the class. You can access them in every method by "self.var_name" and from outside the class with "instance_name.var_name"
        
        # Sample to compute pass with
        self.X          = 0.0 # set me!
        self.y          = 0.0 # set me!
        
        # Parameters to be learned
        self.weight_1   = 1.0 # teach me!
        self.weight_2   = 1.0 # teach me!
        self.bias       = 1.0 # teach me!
        
        # State information
        self.hidden     = 0.0 # use me!
        self.output     = 0.0 # use me!
        self.error      = 0.0 # use me!
        
    # Set sample to be used in feed-forward and back-propagation pass
    def set_sample(self, X, y):
        self.X = float(X)
        self.y = float(y)
        
    # (a) Feed-forward pass
    def feed_forward(self):
        #net input for hidden layer
        self.netHidden = (self.X * self.weight_1) + self.bias
        #output froom the hidden layer
        self.outHidden = 1/(1 + np.exp(-1 * self.netHidden))
        
        #net input for the output layer
        self.netOutput = self.outHidden * self.weight_2
        
        #final output from the output layer
        self.finalOutput = 1/(1 + np.exp(-1*self.netOutput))
        
        #calculating error
        self.error = (1/2) * ((self.y - self.finalOutput) ** 2)
      
    # (b) Back-propagation pass
    def back_prop(self):
        learningRate = 0.01
        
        #For W2
        part1 = (self.y - self.finalOutput) * (-1) #wrt output
        part2 = self.finalOutput * (1 - self.finalOutput) #wrt net input
        part3 = self.outHidden #wrt weight2
        
        derivationW2 = part1 * part2 * part3
        
        #For W1
        derivationW1 = ((self.finalOutput - self.y) * 
                    (self.finalOutput * (1 - self.finalOutput)) * self.weight_2 * 
                    (self.outHidden * (1 - self.outHidden)) * (self.X))
        
        self.weight_1 = self.weight_1 - (derivationW1 * learningRate)
        self.weight_2 = self.weight_2 - (derivationW2 * learningRate)
        
def execute_nn(X, y):
    
    # Instantiate neural network
    nn = NeuralNetwork()
    
    # Collect mean error of each epoch to plot it later
    epoch_error = []

    # Perform multiple epochs, aka inputting the dataset multiple times
    for epoch in range(0,100):

        
        # Example use of neural network class
        # nn = NeuralNetwork() # instantiates neural network
        nn.set_sample(2,5) # sets sample with 2 as input and 5 as target
        nn.feed_forward() # perform feed-forward to calculate output
        nn.back_prop() # use difference between target and actual output to update parameters
        #Remember final error of each epoch in "epoch_error"

        epoch_error.append(nn.error)
        
    # Print final parameters of trained neural network
    print("Weight_1:"+ str(nn.weight_1))
    print("Weight_2:" + str(nn.weight_2))
    print("Bias:" + str(nn.bias))
    
    # Plot epoch errors with logarithmic transformation
    plt.plot(list(range(len(epoch_error))), np.log(epoch_error))
    ax = plt.gca()
    ax.set_xlabel('# Epoch')
    ax.set_ylabel('Error')
    plt.show()
    
    # Plot datapoints as originally transformed and as transformed by neural network
    computed = []
    for i in range(0, X.shape[0]):
        nn.set_sample(X[i], y[i])
        nn.feed_forward()
        computed.append(nn.output)
    plt.scatter(X.transpose().flatten(), y.transpose().flatten(), c='blue', s=16)
    plt.scatter(X.transpose().flatten(), computed, c='red', s=16)
    plt.show()

print("Imitation of formula 'x+0.75'")
execute_nn(X,y_1)
print()
print("Imitation of formula 'sin(x)+0.5'")
execute_nn(X,y_2)





