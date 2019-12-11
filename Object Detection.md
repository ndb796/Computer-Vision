### Support Vector Machine (SVM)

* Characteristics
  * Supervised learning technique
  * Finding the hyperplane that separates two classes with the largest margin
    * The hyperplane that has the largest distance to the nearest training data points of any class
    * (Generally) the larger the margin, the lower the generalization error
* Pros
  * Very powerful classifier, especially when combined with kernel method
  * Works very well in practice, even with very small training sample size
* Cons
  * No "direct" extension to multi-class SVM

### Non-Linear SVM

* If dataset is not linearly separable, we can map data to the higher-dimensional space using kernel method
* Kernel method: The original input space can always be mapped to some higher dimensional space where separation of training dataset may be easier.

### Histogram of Oriented Gradients (HOG)

* No Gaussian smoothing
* Filters to compute horizontal-vertical gradient images

### Deep Learning for Object Detection: A Naive Approach

* Object Detection = Box Localization (Object Proposals) + Box Classification (CNN)

### Region-Based CNN (R-CNN)

* Summary
  * Independent evaluation of each proposal
  * Bounding box regression improves detection accuracy
  * Mean average precision (mAP): 53.7% with bounding box regression in VOC 2010 test set
  * R-CNN family achieves the state-of-the-art performance in object detection
  * Stronger backbone network, better detection performance

* Learning a transformation of bounding box

### Fast R-CNN

* A fast version of R-CNN
  * 9x faster in training and 213x faster in testing than R-CNN
  * A single feature computation and ROI pooling using object proposals
  * Bounding box regression into network
  * Single stage training using multi-task loss

* RoI pooling in details
  * The resolution of pooled feature maps is 7 x 7 in practice
  * An advanced version of RoI pooling: RoI align
  
### Faster R-CNN

* Fast R-CNN + Region Proposal Network
  * Proposal computation into network (Region Proposal Network)
  * Marginal cost of proposals: 10ms

* Details of the region proposal network
  * 9 anchors per location
  * Groundtruth label per anchor
