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
