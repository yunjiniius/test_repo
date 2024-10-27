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

# 특정 컬럼값 일괄 변경
df1['SpecialColumn'] = 'UpdatedValue'
df2['SpecialColumn'] = 'UpdatedValue'
df3['SpecialColumn'] = 'UpdatedValue'

# 피벗
# aggfunc : 피벗 테이블에서 데이터를 집계할 때 사용할 함수(aggregate function)를 지정하는 매개변수 [sum, mean, max 등]
#           피벗 테이블이 동일한 그룹에 속하는 데이터를 어떻게 계산할지를 결정
# aggfunc='sum'을 사용하여 동일한 인덱스와 컬럼 값을 가진 데이터의 합계를 계산하도록 설정 (피벗 테이블에서 데이터를 그룹별로 합산하여 집계)
df1_pivot = df1.pivot_table(index='A', columns='B', values='C', aggfunc='sum')
df2_pivot = df2.pivot_table(index='A', columns='B', values='C', aggfunc='sum')
df3_pivot = df3.pivot_table(index='A', columns='B', values='C', aggfunc='sum')

# 병합
merged_df1 = pd.merge(df1_pivot, df2_pivot, left_on='A', right_on='A', how='inner')
merged_df2 = pd.merge(df2_pivot, df3_pivot, left_on='A', right_on='A', how='inner')
merged_df3 = pd.merge(df1_pivot, df3_pivot, left_on='A', right_on='A', how='inner')

# 데이터 추출
# index=False: 데이터프레임의 인덱스를 엑셀 파일에 포함시키지 않도록 설정
merged_df1.to_excel('merged_df1.xlsx', index=False)
merged_df2.to_excel('merged_df2.xlsx', index=False)
merged_df3.to_excel('merged_df3.xlsx', index=False)

print("작업이 완료되었습니다.")
 