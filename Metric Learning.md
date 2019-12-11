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
