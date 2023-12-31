from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

import numpy as np
import pandas as pd

# 경고 메시지 출력 억제 코드
import warnings
warnings.simplefilter(action='ignore')

GENDER_FILE_PATH = './datasets/gender.csv'

# 데이터 셋을 가지고 온다
gender_df = pd.read_csv(GENDER_FILE_PATH)

X = pd.get_dummies(gender_df.drop(['Gender'], axis=1)) # 입력 변수를 one-hot encode한다
y = gender_df[['Gender']].values.ravel()

# 여기에 코드를 작성하세요
dc = {'penalty': ['l1', 'l2'],
'max_iter': [500, 1000, 1500, 2000]}
model = LogisticRegression()
ml = GridSearchCV(model,dc,cv=5)
ml.fit(X,y)
best_params = ml.best_params_
# 테스트 코드
best_params