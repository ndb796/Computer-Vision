### Semantic Segmentation

* Grouping pixels based on their semantics (class labels)
* In semantic segmentation, they should be in the same segment since they come from the same semantic entity "person"

#### Early Approaches

* Object proposal
  * Detecting (candidate) boxes likely to enclose objects
* Semantic Segmentation = Mask Localization (Object proposals) + Mask Classification (CNN for image classification)
* Some object proposals are based on segmentation (selective search) thus readily provide object candidate masks.
* Limitations
  * The segmentation performance is bounded by region-proposal accuracy

#### Recent Approaches

* End-to-End CNN Architectures
* Category
  * <b>Fully Convolutional Networks (FCN)</b> in CVPR 2015
    * FCN
    * DeepLab
  * Convolutional Encoder-Decoders
    * U-Net
    * Deconvolution Network in ICCV 2015

#### Issues on end-to-end CNN architectures

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
* Experimental results: Faster and more accurate than the previous approaches based on CNNs
  * Faster: The end-to-end architecture that does not rely on off-the-shelf proposals
  * More Accurate: Not bounded by quality of proposals

### DeepLab

* An advanced version of FCN
  * <b>Atrous convolutions</b> that enlarge receptive fields
  * <b>Fully-connected Conditional Random Field (CRF)</b>, a post-processing technique
  * A more powerful backbone network: ResNet101
* Atrous convolution
  * Convolution kernel with "holes"
* CNN with atrous convolution layers
  * Add Atrous Spatial Pyramid Pooling (ASPP) on top of a convolutional feature map

### Deconvolution Network

* Limitations of FCN
  * Fixed-size receptive field (RF)
    * Object larger than the RF may be fragmented
    * Those smaller than the RF may be mislabeled or totally missing
* Overall architecture: Convolutional encoder-decoder
  * A convolutional encoder
    * A series of convolution and max-pooling layers
  * A decoder with deconvolution layers
    * A series of deconvolution (transposed convolution) and un-pooling layers
  * Paired pooling and unpooling layers
    * An unpooling layer is associated with a pooling layer
* Training
  * A batch normalization layer is added to the output of every convolution and deconvolution layer
  * Object proposals are used to generate training examples
* Inference
  * Apply DeconvNet to every object proposal images
  * Aggregate class confidence maps of the proposals by max-pooling per pixel
* Conclusion
  * Convolutional encoder-decoder architecture
  * Aggregating proposal-wise semantic segmentation results
* Pros
  * It achieved the state-of-the-art performance
  * The architecture is well-suited to be trained in semi-supervised manners
* Cons
  * Very heavy architecture
  
### Instance-aware Semantic Segmentation

* Semantic segmentation cannot distinguish different objects of the same class
  * It is because semantic segmentation is formulated as pixel-wise classification
  
#### Early Approaches

* Limitation
  * The segmentation performance is bounded by region-proposal accuracy
* Solution: End-to-end CNN architecture
  * No longer depends on off-the-shelf region-proposals
  * Jointly optimizing following tasks
    * Object localization
    * Mask prediction
    * Object (mask) classification

### Multi-task Network Cascades

* Cascade of detection, segmentation, and classification in a single network
  * Stage 1: box instances (RoIs)
  * Stage 2: mask instances
  * Stage 3: categorized instances

* Limitation
  * Mask estimation per detected object
    * Small mask resolution due to the limited memory
    * Overly smoothed segmentation

### Multi-scale Patch Aggregation

* Learning a CNN for patch-wise segmentation and classification
* Aggregating patch-wise masks for object segmentation
  * Two patches are merged when
    * They have the same class label, and
    * Their masks are overlapped sufficiently
   
### Mask R-CNN

* An extension of Faster R-CNN
* Two additional contributions
  * Adding a branch for predicting segmentation masks on each Region of Interest (RoI)
  * A simple, quantization-free pooling layer, called <b>RoI Align</b>
