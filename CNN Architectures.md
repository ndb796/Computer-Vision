### ImageNet Large Scale Classification Challenge

* 2012 AlexNet's error rate is 16.4 (8 Layers)
* 2013 ZFNet's error rate is 11.7 (8 Layers)
* 2014 VGGNet's error rate is 7.3 (19 Layers) / GoogLeNet's error rate is 6.7 (22 Layers)
* 2015 ResNet's error rate is 3.57 (152 Layers)

### Classification CNN

* Backbone of many other networks
* Backbone network extracts feature maps and score values.

### Well-known CNN Architectures

* LeNet-5: A very simple CNN architecture introduced by Yann LeCun in 1998
  * Overall architecture: Conv - Pool - Conv - Pool - FC - FC
  * Convolution: 5 x 5 Convolution filters with stride 1
  * Pooling: 2 x 2 Max pooling with stride 2

* AlexNet: 2012 Winner
  * Overall architecture: Conv - Pool - Norm - Conv - Pool - Norm - Conv - Conv - Conv - Pool - FC - FC - FC
  * Bigger
  * Trained with a larger amount of data
  * Using better activation function (ReLU) and regularization techinique (Dropout)
  * Norm: Local Response Normalization (LRN)
  
* VGGNet: 2014 Winner
  * Deeper architecture: 16 and 19 layers
  * Simpler architecture: Only 3 x 3 conv filters, 2 x 2 max pooling, and a few FC layers
  * Better performance: Significant performance improvement over AlexNet on the ImageNet challenge
  * Better generalization
  * Using many 3 x 3 conv layers instead of a small number of larger conv filters: Keeping receptive field sizes large enough
  
* ResNet: 2015 Winner
  * Ultra-deep networks: 152 layers
  * Depth is of crucial importance as deeper networks learn more powerful features
  * Larger receptive fields: Capturing semantic concepts with larger context
  * More non-linearities: Modeling more complicated and richer feature space

### Revolution of Depth

* Known obstacles
  * Backward gradients that are easily vanished or exploded
  * Forward responses that are easily vanished or exploded
 
* Enablers
  * ReLU activations
  * An appropriate initialization technique
  * Batch normalization
 
### Batch Normalization

* Alleviating the <b>internal covariate shift</b> by normalizing intermediate features
* Summary
  * Normalizing each layer, for each mini-batch
  * Greatly accelerate training
  * Less sensitive to initialization
  * Improve regularization
 
### Degradation Problem

* Problem
  * With the network initilization and batch normalization, is learning better networks as simple as staking more layers? Unfortunately, <b>NO</b>.
  * 56-layer network has higher training error and test error than 20-layer network when 3 x 3 conv layers are simply stacked, but this is not caused by overfitting.
  * Solvers might have difficulities in approximating identity mapping by multiple non-linear layers.
 
* Solution: Deep residual learning
  * Plain Net aims to fit the desired mapping <b>H(x)</b>.
  * Residual Net aims to fit <b>F(x) = H(x) - x</b> instead of <b>H(x)</b>.
  
