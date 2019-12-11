### Metric Learning

* A Metric is a function that quantifies a distance between every pair of elements in a set, thus inducing a measure of similarity
* Learning D and/or f satisfying the relations from data
* Metric은 집합에서의 각 원소 쌍의 거리(Distance)를 계산해주는 함수이다. (얼마나 두 원소가 닮았는지를 평가하는 척도가 된다.)
* KNN처럼 Distance Metric에 의존하는 기법에 대해서는 적절한 D(Distance Metric)을 찾는 것이 중요하다.

### Similarity in Computer Vision

* Person re-identification: 인간 재식별화 (특정 카메라에서 인식한 사람을 다른 카메라에서도 인식하는 작업)
* Visual tracking: 연속적인 프레임(Frame)에서 매 번 특정한 Object의 Bounding Box를 찾는 작업
* Local patch matching for stereo imaging: Stereo Images에서, 동일한 Object를 나타내는 두 패치를 매칭하는 작업
* Visual representation learning

### Mahalanobis Distance

* Euclidean distance에서는 거리가 짧은 두 점도, Manifold 상에서는 거리가 멀 수 있다.
* Mahalanobis Distance는 Manifold를 고려하여 두 점의 Semantic한 거리를 계산하기 위해 사용된다.
* Euclidean distance is a special case of Mahalanobis distance, where M = I

### A First Approach to Distance Metric Learning

* S+: The set of similar pairs
* S-: The set of dissimilar pairs
* S+끼리의 Mahalanobis Distance 값의 제곱의 합을 줄이고, S-끼리의 Mahalanobis Distance 값의 제곱의 합을 Threshold 이상으로 유지한다.
* M은 positive semi-definite matrix이다.

### Large Margin Nearest Neighbor

* 서로 다른 클래스를 가지는 쌍에 대하여 Margin을 극대화 시키는 방법
* 서로 같은 클래스를 가지는 쌍에 대하여 당기고(Pull), 서로 다른 클래스를 가지는 쌍에 대하여 미는(Push) 방향으로 학습한다.
* 하나의 Objective Function을 이용하고 있으며, 단순히 원소들을 뽑아서 Objective Function에 넣은 뒤에 그 Loss 값으로 학습한다.

### Metric Learning Before the Era of Deep Learning

* Learning parameters of D
  * Mahalanobis distance의 M
* Fixing the data representation f
  * Image data itself
  * Off-the-shelf, hand-crafted image descriptors
  * 함수 f로는 그냥 이미지 그 자체를 사용해도 되고, 이미지의 Descriptor를 사용해도 된다는 의미이다.

### Deep Metric Learning

* Data representation and decision maker in a single network architecture
* Learning representation from data
* DNN 모델을 함수 f라고 칭하며, 이를 data representation 목적으로 사용한다.
* 거리를 계산할 때는, 이미지를 함수 f에 넣어서 나온 값(feature space에서의 값)끼리의 Euclidean distance를 계산한다.

### Siamese Network

* A pair of neural networks sharing parameters
* Contrastive loss designed for learning architecture
* LMNN과 형태가 유사하고, margin을 위하여 1 대신에 m을 이용한다.
* 같은 클래스의 이미지는 거리를 줄이고, 다른 클래스의 이미지는 거리를 늘리는 방향으로 학습한다.
* 일반적인 DNN을 학습시키는 방법과 동일하다.

### Triplet Network

* Exploiting relations among a triplet of examples
* Given an anchor, the distance between a positive pair should be smaller than that of a negative pair in the feature space
* 한 장의 이미지, 같은 클래스의 이미지, 다른 클래스의 이미지(총 3장)를 뽑아서 Objective Function에 넣어 Loss를 계산한다.
* 같은 클래스의 이미지는 거리를 줄이고 다른 클래스의 이미지는 거리를 늘리는 방향으로 학습한다.
* margin 값이 의미 있게 적용되기 위하여 embedding feature에서의 L2 normalization이 필요하다.
* 실제로는 mini-batch 단위로 입력을 구성하여 넣는다.

### Sample Selection Also Matters

* Triplet Network에서 N개의 이미지에서 3개를 선택하는 조합은 3중 반복문에 해당한다.
* Easy Positive: 너무 쉬운 Pair나 Triplet을 선택하는 경우 Loss가 0이 되므로 학습이 잘 안 된다.
* Hard Negative: 너무 어려운 Pair나 Triplet을 선택하는 경우에도 학습 과정이 Unstable하게 된다.
* 따라서 Triplet Network를 잘 학습시키기 위해서 효과적인 샘플링 방법이 필요하다.

### Uniform Sampling

* Assuming an L2 normalized embedding space, distances between uniformly sampled points on the space are biased.
* If we select samples in such a naive way, they will be biased as well, which will damage the quality of embedding.

### Distance Weighted Margin-based Loss

* Biased된 구간이 아니라, 넓은 범위에서의 샘플링을 위한 방법
* Biased된 거리에 대하여 Distribution을 계산한 뒤에 높은 확률 구간에서 적게, 낮은 확률 구간에서 많이 샘플링한다.
* 기존의 Triplet Network보다 개선된 성능을 보인다.

### Quadruplet Network

* Sometimes, the relationship among a triplet is not sufficient
* Multi-object tracking: Different relationships among positive samples according to their time indices
* Person re-identification: Enlarging inter-class distances with additional constraints for better generalization
* Loss: a linear combination of two triplet rank losses
* 시간적으로 가까운 positive sample은 anchor와 feature space 상에서 가깝고, negative sample은 anchor와 멀리 떨어지도록 학습한다.

### Nearest Neighbor Search

* Finding nearest ones among training examples in a specific space
* Applications in computer vision
  * Nearest neighbor classification
  * Image completion
  * Label transfer
* Key determinant of success: Distance metric and/or feature space that are appropriate for the target task
  * Metric learning is a solution

### Image Retrieval

* Content-based image retrieval
  * A most straightforward way: Nearest neighbor search in the embedding space
  * Working even for unseen classes or concepts (class-agnostic similarity)

### Face Verification

* Deciding if two face images (a query and a known face) are the same or not
* Done simply by applying a threshold to their distance in the embedding space

### Person Re-identification

* Identifying people across different cameras
  * A most straightforward way: Nearest neighbor search in the embedding space
  * Working for general (unseen) people (class-agnostic similarity)

### Online Visual Tracking

* Tracking a target manually annotated at the first frame of input sequence
* Done by particle filtering with the learned embedding function
* Particle filtering
  * Drawing random samples around the location of the target in the previous time step
  * Selecting the sample most similar with the target object
  * Key component: Comparing the initial target to candidate boxes
  * Solution: Similarity as an inverse of distance in the embedding space
    * Learned similarity (distance metric) specialized to visual object tracking
    * Invariant to target object

### Unsupervised Representation Learning

* Motivation
  * Representation learning is a key determinant of success in visual recognition
  * However, it requires significant amounts of supervision
  * Most large-scale datasets are only about image classification
    * Network architectures are limited to those for image classification
* Solution: Unsupervised representation learning
* Learning Similarity with a neural network and triplets of video patches
  * Supervision for similarity can be obtained easily; even automatically in the case of videos

### Pose-aware Representation Learning

* Learning pose-aware representation by human pose similarity between images
* Extracting pose information immediately without explicit pose estimation
  * Nearest neighbor search in the learned embedding space: human pose retrieval
