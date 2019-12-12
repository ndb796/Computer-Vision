### Fitting Problems

* Finding vanishing point
* Image stitching
* 3D object recognition

### Fitting

* Goal: Choose a parametric model to fit a certain quantity from data
* Techniques
  * Least square methods
  * RANSAC
  * Hough transform
* Challenges
  * Noisy data
  * Outliers
  * Missing data
* Fitting이란 데이터에 잘 부합하는 parametric model을 찾는 과정을 의미한다.

### Least Square Method

* Parametric model: y = ax + b
* Goal: Estimating a and b that minimize the least square errors
* Objective function (convex)
    * Global optimum must satisfy "gradient = 0"
* Least square error를 최소화하는 파라미터를 찾는 방법이다.

### Limitation of Ordinary Least Square

* The solution may not be reasonable
  * Not rotation invariant
  * Unable to represent horizontal and vertical lines
  * Sensitive to noises when the slope is high
* Least square method based on the perpendicular distance (수직 거리) is more reasonable
* 기본적으로 Least Square Method는 outlier에 많은 영향을 받는다는 단점이 있다.

### RANSAC

* RANSAC (RANdom SAmple Consensus) can handle a large number of outliers
* Reduces model estimation time
* Iterative algorithm: hypothesizing and testing
* A sort of voting scheme
* Outline
  * Choose a small subset of points uniformly at random
  * Fit a model to that subset
  * Find all remaining points that are "close" to the model and reject the rest as outliers
  * Do this many times and choose the best model

### Explanation of RANSAC

1. Randomly select minimal subset of points
2. Hypothesize a model
3. Compute error function
4. Select points consistent with model and compute the ratio
5. Repeat hypothesize-and-verify loop for the pre-defined number of iterations

### RANSAC for Line Fitting

* Repeat N times
  1. Draw s points uniformly at random
  2. Fit a line to these s points
  3. Find inliers to this line among the remaining points (Inliers = points whose 'distance from the line < t')
  4. If there are d or more inliers, accept the line and refit using all inliers

### RANSAC Parameters

* s: Number of points for building a hypothesis
* N: Number of iterations
* t: Distance threshold
* d: Consensus set size

### Conclusion of RANSAC

* A good robust parameter estimation technique
* Widely used in many computer vision problems
* RANSAC은 outlier에 강하다는 특징이 있어서 이미지를 처리하는 분야에서 활용도가 높다.
* Pros
  * Simple and general
  * Applicable to many different problems
  * Often works well in practice
* Cons
  * Lots of parameters to tune
  * Does not work well for low inlier ratios
  * Does not guarantee the globally optimal solution

### Hough Transform

* Voting for parameter estimation
  * An early type of voting scheme
  * Convert from image space to parameter space

### Characteristics of Hough Transform

* Assumptions
  * The noise features will not vote consistently for any single model
  * There are enough data to agree on a good model
* Pros
  * Can deal with non-locality and missing data
  * Can detect multiple instances of a model
  * Some robustness against noise
    * noise points unlikely to contribute consistently to any single bin
* Cons
  * Complexity increases exponentially with the number of model parameters
  * Hard to pick a good grid size

### Feature Matching by Appearance

* Feature detection
  * Edges
  * Corners
  * Blobs

* Feature descriptors
  * Template
  * SIFT, PCA-SIFT
  * Speeded Up Robust Features (SURF)
  * Bias and gain normalization (MOPS)
  * Gradient location-orientation histogram (GLOH)

### Fitting Helps Matching

* Idea - Fitting an homography H that maps features from image 1 to image 2
  * Homography
    * Projective transformation
    * 2D projection of 3D planar surface
    * Represented by a 3x3 matrix H
    * At least 4 matching pairs required to estimate the matrix H
  * Using RANSAC to estimate H

### Review: Fitting and Matching

* If we know which points belong to the line, how do we find the "optimal" line parameters?
  * Least Square Method
* What if there are outliers?
  * RANSAC
* What if there are many lines?
  * Voting methods: RANSAC, Hough Transform
* Fitting helps matching
