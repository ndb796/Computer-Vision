### 2D Points

* Pixel coordinates in an image
* Using inhomogeneous coordinates
  * Ordinay coordinate system
  * x = [x, y]
* Using homogeneous coordinates
  * Augmented vector = [x, y, 1]
  * Vectors that differ only by scale are considered to be equivalent

### 2D Lines

* Represented in homogeneous coordinates

### 2D Transformations

* Basic set of 2D planar transformations
* Translation: Modifying location only
* Euclidean transformation: Rotation + Translation
* Similarity transformation: Scaling + Rotation + Translation
* Affine transformation
  * Non-singular linear transform + Translation
  * Parallel lines remain parallel
* Projective transformation
  * Also known as "Perspective transformation" or "Homography"
  * Parallel lines can be non-parallel in projective transformation

### 3D Points

* Identical to the case of 2D points

### 3D Lines

* Presented by using two points on the line
  * Any point on the line can be expressed as a linear combination of the two points

### 3D Planes

* Represented in homogeneous coordinates

### Pinhole model

* Basic concept
  * An idealization of the thin lens model as aperture shrinks to zero
  * Rays of light emitted from a point travel along one path through the pinhole
  * Inverted image is observed in image plane
  * Virtual image: plane in front of pinhole with same distance to the image plane
