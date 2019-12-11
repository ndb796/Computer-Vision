### Time Information Fusion

* A video = A bag of short fixed-sized clips
  * Classifying each clip, aggregating the class scores of individual clips for final decision
* 4 different approaches to fusing information across temporal domain
  * Single Frame
  * Early Fusion
    * Allowing the network to precisely detect local motion direction and speed
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

