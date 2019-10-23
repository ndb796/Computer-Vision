### Local Image Feature

* An interesting part of an image
* A starting point of many computer vision algorithms

### Use of Local Image Features

* Stereo Matching
* 3D Reconstruction
* Image Stitching

### Good Local Feature (Interest Point)

* Good local feature should be unambiguous for matching

### Conditions to be a good local visual-feature

* Repeatability (반복성): The same feature should be detected in many images of the same scene.
* Saliency (특징성): A feature includes an interesting part of an image.
* Locality (지역성): A feature occupies a small area in an image.

### Convolution (Linear Filtering)

* Convolution output is a linear combination of input.
* Smoothing, Sharpening, Gradient, ...

#### Horizontal filter

||||
|:-:|:-:|:-:|
|-1|0|1|
|-2|0|2|
|-1|0|1|

#### Vertical Filter

||||
|:-:|:-:|:-:|
|-1|-2|-1|
|0|0|0|
|1|2|1|

### Padding

* Removing boundary effect of image filtering

### Edge

* A set of points lying on a boundary between distinct regions
* With sudden changes of intensity

### Edge Detection

* Convolution of smoothing (denoising) and graident (edge detection) filteres

### Corners

* Junctions of contours
* Good local features to match

### Harris Corner Detection's Basic Idea

* Corner: significant change in all directions
* Edge: No change along the edge direction
* Flat region: No change in all directions
