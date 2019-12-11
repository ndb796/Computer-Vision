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

### Least Square Method

* Parametric model: y = ax + b
* Goal: Estimating a and b that minimize the least square errors
* Objective function (convex)
    * Global optimum must satisfy "gradient = 0"

### Limitation of Ordinary Least Square

* The solution may not be reasonable
  * Not rotation invariant
  * Unable to represent horizontal and vertical lines
  * Sensitive to noises when the slope is high
* Least square method based on the perpendicular distance (수직 거리) is more reasonable

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
* Pros
  * Simple and general
  * Applicable to many different problems
  * Often works well in practice
* Cons
  * Lots of parameters to tune
  * Does not work well for low inlier ratios
  * Does not guarantee the globally optimal solution
