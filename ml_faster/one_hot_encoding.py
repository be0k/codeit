import pandas as pd

GENDER_FILE_PATH = './datasets/gender.csv'

gender_df = pd.read_csv(GENDER_FILE_PATH)
input_data = gender_df.drop(['Gender'], axis=1)

# 여기에 코드를 작성하세요
X = pd.get_dummies(data=input_data)
# 테스트 코드
X.head()