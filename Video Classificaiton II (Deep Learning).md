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
* Multi-resolution CNN for efficient and effective video recognition
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
