import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 환경에서 맑은 고딕 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# COMPAS 데이터셋 로드
df = pd.read_csv("compas.csv")

# 성별과 폭력적 재범 여부의 상관관계 분석
sns.countplot(x='sex', hue='is_violent_recid', data=df)
plt.title('성별과 폭력적 재범 여부의 상관관계')
plt.show()

# 나이와 일반적 재범 여부의 상관관계 분석
sns.countplot(x='age', hue='is_recid', data=df)
plt.title('나이와 일반적 재범 여부의 상관관계')
plt.show()
