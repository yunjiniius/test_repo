import pandas as pd

# 데이터 로드
df1 = pd.read_excel('sample.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('sample.xlsx', sheet_name='Sheet2')

# 전처리

# 피벗
df1_pivot = df1.pivot_table(index=['ITEM_ID', 'ITEM_A', 'ITEM_B'], columns=['ITEM_NAME_1', 'ITEM_NAME_2'], values='ITEM_VALUE', aggfunc='first')
df2_pivot = df2.pivot_table(index=['ITEM_ID', 'ITEM_A', 'ITEM_B'], columns='ITEM_NAME', values='ITEM_VALUE', aggfunc='first')

# 병합을 위해 인덱스와 열 리셋
df1_pivot_reset = df1_pivot.reset_index()
df1_pivot_reset.columns = ['_'.join(col) if isinstance(col, tuple) else col for col in df1_pivot_reset.columns]

df2_pivot_reset = df2_pivot.reset_index()
df2_pivot_reset.columns = ['_'.join(col) if isinstance(col, tuple) else col for col in df2_pivot_reset.columns]

# 병합을 위한 join 데이터프레임 생성
df_join = pd.DataFrame({
    'df1': [1, 2],
    'df2': [11, 12]
})

# join df 병합
merged_df1 = pd.merge(df1_pivot_reset, df_join, left_on='ITEM_A_', right_on='df1', how='left')
merged_df2 = pd.merge(df2_pivot_reset, df_join, left_on='ITEM_A', right_on='df2', how='left')

# 최종 병합을 위해 두 데이터프레임의 열 이름 통일
merged_df1.rename(columns={'ITEM_ID_': 'ITEM_ID', 'ITEM_A_': 'ITEM_A', 'ITEM_B_': 'ITEM_B'}, inplace=True)

# 최종 병합
merged_final = pd.merge(merged_df1, merged_df2, on=['ITEM_ID', 'ITEM_A', 'ITEM_B'], how='outer')

# 데이터 추출
merged_final.to_excel('merged_final.xlsx', index=False)

print("작업이 완료되었습니다.")
