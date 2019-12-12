### Visual Tracking

* Estimating location of target object over time
* Target Object
  * Larger and more complex than pixel and local features
  * Given manually at the first time (single target tracking)
  * Or detected automatically by object detectors (multiple target tracking)
* Long-term tracking
  * Tracking objects until they exit
* Should be robust against
  * Illumination change
  * Deformation
  * Background clutter
  * Complex and abrupt motion
  * Occlusion
* Results
  * Trajectories
    * Video analysis
    * High-level event detection
  * Spatio-temporal localization of target
    * Action recognition
    * Location prediction

### Challenges of Visual Tracking

* Appearance Model
  * Illumination change
  * Background clutter
  * Deformation
  * Occlusion
* Motion Model
  * Abrupt motion
  * Shot change

### Appearance Model

* Single-object tracking
  * Sample candidates
  * Select the most similar one
* Multi-object tracking
  * Detect candidates
  * Find the match maximizing the sum of similarities

### Motion Model

* Searching around the previous location of target
  * Assuming temporal smoothness of target location
  * Two typical approaches
    * Random sampling
      * Probabilistic tracking
      * "Particle filtering"
    * Sliding window
      * Deterministic tracking
      * "Tracking by detection"

### Tracking Frameworks

* Single object tracking
  * Particle filtering
    * Probabilistic tracking
    * Generative apporach
  * Tracking by detection
    * Deterministic tracking
    * Discriminative apporach
* Multiple object tracking
  * Temporally associating detected objects
  * Mostly deterministic
  * Improving detection results

### Probabilistic Tracking

* Estimating a probability density function with respect to the target state
* Target state estimation
  * Finding the state with the largest probability

### Examples of Sequential Bayesian Filtering

* Kalman filter: Modeling p as a single Gaussian distribution
  * Limitations of Kalman filter
    * Single modality of the posterior density
      * Kalman filter cannot capture multiple hypotheses of target candidates
    * Linear motion model
      * Target motion is frequently non-linear in real world
  * Solution
    * Non-parametric representation of the posterior density function

### Particle Filtering

* Appearance model
  * Numerical representation of target appearance
    * Image itself
    * Color histogram
    * Histogram of Oriented Gradients (HOG)
    * Bag of local features in the target area
    * Convolutional neural network
  * Must adapt to apperance variation (deformation, illumination change, etc.)
    * Online update is essential for robust long-term tracking

### Tracking by Detection

* Motivation
  * Recent advances in object detection
  * Online learning algorithms for classifiers
* Examples
  * Support Vector Tracking, TPAMI 2004
  * Online Boosting and Vision, CVPR 2007
  * Tracking-Learning-Detection, TPAMI 2010
* Basic idea
  * Appearance model
    * Target classifier that distinguishes target from background
  * Motion model
    * Sliding window around the target location

### Tracking by Global Association
* Input
  * Video frames with object detection results (bounding boxes)
* Output
  * Trajectories of multiple objects
    * A trajectory = a sequence of bounding boxes ordered temporally
  * (Optionally) Improved object detections
* Pros
  * Free from initialization problem
  * More robust against abrupt changes in lighting condition and motion
  * More rigorous to deal with occlusion and entrance/leaving event
* Cons
  * Typically done in an offline manner
  * Costly
* Common issues
  * Robust matching between detections
    * Appearance model
      * Modeling smooth change in appearance
      * Discriminating target from others
    * Motion model
      * Modeling smooth change in location
  * How to find globally optimal associations
  * Handling noisy detections
  * Handling occlusions
