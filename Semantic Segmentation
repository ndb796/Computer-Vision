### Semantic Segmentation

* Grouping pixels based on their semantics (class labels)
* In semantic segmentation, they should be in the same segment since they come from the same semantic entity "person"

### Early Approaches

* Object proposal
  * Detecting (candidate) boxes likely to enclose objects
* Semantic Segmentation = Mask Localization (Object proposals) + Mask Classification (CNN for image classification)
* Some object proposals are based on segmentation (selective search) thus readily provide object candidate masks.
* Limitations
  * The segmentation performance is bounded by region-proposal accuracy

### Recent Approaches

* End-to-End CNN Architectures
* Category
  * <b>Fully Convolutional Networks (FCN)</b> in CVPR 2015
    * FCN
    * DeepLab
  * Convolutional Encoder-Decoders
    * U-Net
    * Deconvolution Network in ICCV 2015

### Issues on end-to-end CNN architectures

* Semantic segmentation = Pixel-level classification
* Trade-off between the resolution and the semantic level of prediction

### Fully Convolution Networks (FCN)

* The first end-to-end architecture for semantic segmentation
* No fully connected layers, only convolutional layers
* Able to handle images of any arbitrary sizes and aspect ratios
* Interpreting fully connected layers of classification nets as 1 x 1 convolutions
  * The output can be interpreted as class scores over local image regions.
* Limitation: Predicted score map in a very low-resolution
* For enlarging the score map
  * Adding a simple bilinear interpolation on the top of the network
  * Adding skip-connections
