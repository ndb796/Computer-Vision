### Motion and Perceptual Organization

* Even impoverished motion data can evoke a strong percept

### Uses of Motion

* 3D structure estimation
  * ex) 여러 장의 이미지로부터 포인트 클라우드 데이터 구하기
* Object segmentation
* Robust shape descriptor
* Recognizing human action and activities
* Improving video quality (motion stabilization)

### Computing Motion

* Direct methods (e.g., optical flow)
  * Recover motion directly from two consecutive video frames without feature extraction
  * Dense motion fields, but more sensitive to appearance variations
  * Suitable for video and when image motion is small
* Feature-based methods
  * Extract visual features (e.g., corners, blobs, textured areas) first
  * Track them over multiple frames
  * Obtain sparse motion fields, but possibly work robustly
  * Suitable especially when image motion is large
* Object tracking
  * Locate a moving object (or multiple objects) over time in a video
  * An object = a part of image enclosed by a bounding box

### Video

* A video is a squence of frames captured over time
* Now our image data is a function of space (x, y) and time t

### Optical Flow

* Computing pixel-wise 2D motion vector between two consecutive frames
* How to estimate pixel motion from image (t-1) to image (t)?
  * By solving pixel correspondence problem
  * Given a pixel in image (t-1), look for nearby pixels of the same color in image (t)
* Key assumptions (2가지)
  * Color constancy: A point in image (t-1) looks the same in image (t)
  * Small motion: Points do not move very far

### Lukas-Kanade Flow

* A widely used differential method for optical flow estimation
* Those conditions will be satisfied at corner points
* For robust motion estimation, the point should be a corner

### Good Feature To Track

* Corner: Significant change in all directions (Good to track)
* Edge: No change along the edge direction
* Flat region: No change in all directions

### Video Recognition with "Space-time Interesting Points"

* Also known as "action recognition"
* A common framework before the era of deep learning
* Feature Extraction (Human poses) → Video Representation (Bag of visual words) → Classification (SVM)

#### Video Representation

* Space-time interest point (STIP)
  * Corner point in a spatio-temporal domain
  * STIP descriptor: 162-D descriptor per interest point (HOG + HOF)
* Bag of visual words
  * Construction of visual vocabulary
  * Collecting STIPs and their descriptors from training videos
  * Estimating representative visual words via clustering
  * Representing a video as a histogram of the visual words
* Spatio-temporal pyramids
  * Structural information
  * Multi-channel representation
  * Greedy approach to find the best combination

#### Classification

* Support vector machine
  * Using kernel
    * Non-linear separation
    * Metric relation

### Video Recognition with "Dense Trajectory Descriptors"

