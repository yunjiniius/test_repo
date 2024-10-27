import pandas as pd

# 데이터 로드
df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')
df3 = pd.read_excel('file3.xlsx')

# 전처리
# 컬럼 필터
columns_to_keep = ['A', 'B', 'C', 'SpecialColumn']
df1 = df1[columns_to_keep]
df2 = df2[columns_to_keep]
df3 = df3[columns_to_keep]

# 특정 컬럼값 일괄 변경 (연산)
df1['SpecialColumn'] = df1['SpecialColumn'] * 2  # 예시: 값을 2배로 변경
df2['SpecialColumn'] = df2['SpecialColumn'] * 2
df3['SpecialColumn'] = df3['SpecialColumn'] * 2

# 피벗
df1_pivot = df1.pivot_table(index='A', columns='B', values='C', aggfunc='sum')
df2_pivot = df2.pivot_table(index='A', columns='B', values='C', aggfunc='sum')
df3_pivot = df3.pivot_table(index='A', columns='B', values='C', aggfunc='sum')

# 병합
merged_df1 = pd.merge(df1_pivot, df2_pivot, left_on='A', right_on='A', how='inner')
merged_df2 = pd.merge(df2_pivot, df3_pivot, left_on='A', right_on='A', how='inner')
merged_df3 = pd.merge(df1_pivot, df3_pivot, left_on='A', right_on='A', how='inner')

# 데이터 추출
merged_df1.to_excel('merged_df1.xlsx', index=False)
merged_df2.to_excel('merged_df2.xlsx', index=False)
merged_df3.to_excel('merged_df3.xlsx', index=False)

print("작업이 완료되었습니다.")
 