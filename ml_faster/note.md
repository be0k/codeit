# ml_faster
## Feature Scaling
- min-max normalization   
0과 1사이의 숫자로 바꿈
- standardization


## one-hot encoding
labeling을 0,1,2,3 이런 식으로 하는게 아니라   
\[1,0,0,0]   
\[0,1,0,0]
\[0,0,1,0]
\[0,0,0,1]

## bias-variance tradeoff
분산이 줄고 편향이 늘어난다 : 직선모델(underfit)
분산이 늘고 편향이 줄어든다 : 곡선모델(overfit)
bias-variance tradeoff : 분산과 편향과의 적절한 관계를 찾아내는 것

## 정규화
모델의 parameter값들이 커지지 않도록 제한을 걸어두는것
- L1 정규화(Lasso Regression, Lasso모델)
평군제곱오차같은 손실함수에 파라미터 값들을 더해서 손실을 적게 하면서 파라미터 값도 감소시키는 방향으로 학습(파라미터 값들을 더한 값에 람다(또는 alpha)를 곱함)
-L2 정규화(Ridge Regressin, Ridge모델)

로지스틱회귀에 l1, l2정규화를 적용시키고 싶다
- LogisticRegression(penalty='none')  # 정규화 사용 안함
- LogisticRegression(penalty='l1')  # L1 정규화 사용
- LogisticRegression(penalty='l2')  # L2 정규화 사용
- LogisticRegression()  # 위와 똑같음: L2 정규화 사용

차이점
L1 정규화는 여러 값들을 0으로 만들어 준다 모델에 중요하지 않다고 생각되는 속성들을 아예 없애줌
L2 정규화는 값들을 0으로 만들기보다는 조금씩 줄여 줌. 모델에 사용되는 속성들을 L1처럼 없애지는 않음

## k겹 교차검증
training dataset을 k개로 나누고 학습 한번에 한번씩 validation해보는것


max_iter = 경사 하강법을 몇번 할건지