### Time Information Fusion

* A video = A bag of short fixed-sized clips
  * Classifying each clip, aggregating the class scores of individual clips for final decision
* 4 different approaches to fusing information across temporal domain
  * Single Frame
  * Early Fusion
    * Pixel-level fusion: Allowing the network to precisely detect local motion direction and speed
  * Late Fusion
    * Fusion by the first fully-connected layer
  * Slow Fusion
    * 3D convolution for the fusion in the middle of the networks
  * 기본적으로 Slow Fusion 방식이 다른 방법들에 비하여 높은 성능을 보인다.
* Multi-resolution CNN for efficient and effective video recognition
  * Multi-resolution CNN은 서로 다른 Stream에서 고해상도 및 저해상도를 각각 처리한 뒤에, 결과를 구하는 아키텍처이다.
  * Motivation: Video recognition is computationally heavy
  * A naive solution: Decreasing video resolution
    * Enhancing the computational efficiency
    * Degrading the recognition accuracy
  * Proposed: Multi-resolution architecture
    * Context stream
      * Receiving downsampled video
      * Capturing context of whole scene
    * Fovea stream
      * Focusing on the center crop of input video in high-resolution

### Conclusion of Time Information Fusion

* Contribution
  * Investigating various archictectures that fuse visual information across time
  * A new multi-resolution architecture for efficient and effective video recognition
* Limitation
  * Underperformance: Worse than "hand-crafted features + SVM"
  * Inappropriate use of motion cue
  * 기본적인 "Time Information Fusion" 방법들은 전통적인 방법보다 오히려 성능이 떨어진다는 한계점이 있다.

### 3D Convolutional Neural Network

* Extracting features from both spatial and temporal dimensions by 3D convolutions
* Capturing the motion information encoded in multiple adjacent frames
* 인접한 프레임 사이에서의 모션(motion) 정보를 처리할 수 있다.
* An old architecture trained with a small number of videos
* A shallow architecture trained with a small number of videos
* Explicit motion computation
  * Computationally heavy
  * Cannot fully leverage the advantage of 3D convolution
* Underperformance
  * Worse in accuracy than previous work based on hand-crafted features
* 초기의 3D CNN은 오래된 방법이며, 기존의 전통적인 방법보다 성능이 떨어진다.

### C3D

* A modern 3D CNN architecture
  * VGGNet style network
  * 3 x 3 x 3 (3D) convolution kernels
  * 2 x 2 x 2 max pooling with stride 1
  * ReLU activation functions
* Achieving state-of-the-art scores on most of existing video recognition benchmarks
* C3D는 전통적인 방법보다 높은 정확도(Accuracy)를 보인다.
* Limitations
  * Still to expensive in terms of the number of parameters, computation, and memory
  * Hard to capture large-displacement motion
  * Limited temporal receptive fields
  * 3D CNN은 무겁다는 단점이 있는데, C3D에서도 이러한 문제를 여전히 가지고 있다.

### Two-Stream Convolutional Network

* CNN with two seperate streams
  * Spatial stream: Action recognition from still frame images
  * Temporal stream: Action recognition from dense motion fields (optical flows)
  * 두 개의 Stream에서의 결과를 Fusion하는 방식
* Motivated by human visual cortex that contains two pathways
  * Ventral stream which performs object recognition
  * Dorsal stream which recognizes motion
* Advantage of decoupling spatial and temporal networks
  * Able to exploit large-scale image recognition datasets or pretrained networks for the spatial stream
* Spatial stream
  * ImageNet pretrained network, whose architecture is similar to ZFNet
  * Fairly competitive on its own
* Temporal stream
  * A CNN whose architecture is similar to ZFNet
  * Taking a stacked optical flow images as input
  * Learned from scratch: lack of training data
  * Solution: Multi-task learning
* Limitations
  * It doubles the number of network parameters and the amount of computation
  * Explicit optical flow estimation is computationally too heavy
  * 역시나 두 개의 모델을 결합해야 한다는 점에서 비용이 큰 편이다.
