# Plotly

- [https://plotly.com/python/](https://plotly.com/python/)

---

## Plotly란?

Plotly는 데이터 시각화를 위한 강력한 라이브러리입니다. 이 라이브러리는 사용자가 인터랙티브한 차트를 쉽게 만들 수 있도록 도와줍니다. Plotly는 파이썬뿐만 아니라 R, 자바스크립트 등 다양한 언어에서 사용 가능하며, 웹 기반의 상호작용이 가능한 차트를 만들 수 있어 데이터를 더욱 직관적으로 분석할 수 있게 합니다. 특히 Plotly는 그래프가 동적이어서, 마우스 클릭이나 확대/축소와 같은 동작으로 차트를 자유롭게 탐색할 수 있는 점이 큰 장점입니다.

## Plotly의 주요 기능

- **다양한 차트 유형 지원**: 선 그래프, 막대 그래프, 원 그래프, Sunburst 차트, 지도 등을 포함한 여러 유형의 차트를 지원합니다.
- **인터랙티브 기능**: 데이터 포인트를 클릭하거나, 그래프 영역을 확대/축소하는 등 상호작용이 가능합니다.
- **웹 기반 시각화**: Plotly로 만든 차트는 웹 페이지에 포함할 수 있어, 대시보드나 웹 애플리케이션에서 사용하기 좋습니다.

## Plotly 설치 및 기본 사용법

먼저 Plotly를 사용하기 위해서는 해당 라이브러리를 설치해야 합니다. 다음 명령어를 통해 설치할 수 있습니다:

```
pip install plotly
```

## Plotly의 주요 기능과 차트 유형

### 1. 선 그래프 (Line Chart)

선 그래프는 데이터의 시간 변화나 트렌드를 시각화할 때 사용됩니다.

```python
import plotly.express as px
import pandas as pd

data = {'날짜': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        '매출': [100, 200, 150, 300]}
df = pd.DataFrame(data)

fig = px.line(df, x='날짜', y='매출', title='날짜별 매출 변화')
fig.show()
```

- `px.line()` 함수로 선 그래프를 생성합니다. `x`와 `y` 매개변수로 각각 축의 값을 설정할 수 있습니다.

### 2. 막대 그래프 (Bar Chart)

막대 그래프는 카테고리별 수치를 비교할 때 유용합니다.

```python
import plotly.express as px

data = {'제품': ['A', 'B', 'C', 'D'],
        '판매량': [100, 150, 200, 130]}
df = pd.DataFrame(data)

fig = px.bar(df, x='제품', y='판매량', title='제품별 판매량')
fig.show()
```

- `px.bar()` 함수를 사용하여 카테고리와 그 수치를 막대 그래프로 표현합니다.

### 3. 산점도 (Scatter Plot)

산점도는 두 변수 간의 관계를 시각화하는 데 사용됩니다.

```python
import numpy as np

data = {'x': np.random.rand(100), 'y': np.random.rand(100)}
df = pd.DataFrame(data)

fig = px.scatter(df, x='x', y='y', title='산점도 예제')
fig.show()
```

- `px.scatter()` 함수를 사용하여 데이터 포인트의 분포를 확인할 수 있습니다.

### 4. 원 그래프 (Pie Chart)

원 그래프는 전체에서 각 부분이 차지하는 비율을 보여줍니다.

```python
data = {'카테고리': ['식당', '카페', '베이커리'], '비율': [50, 30, 20]}
df = pd.DataFrame(data)

fig = px.pie(df, names='카테고리', values='비율', title='카테고리별 비율')
fig.show()
```

- `px.pie()` 함수를 사용하여 각 카테고리가 전체에서 차지하는 비율을 나타낼 수 있습니다.

### 5. 히스토그램 (Histogram)

히스토그램은 데이터를 구간별로 나누어 분포를 시각화하는 데 유용합니다.

```python
import plotly.express as px

data = {'값': np.random.randn(500)}
df = pd.DataFrame(data)

fig = px.histogram(df, x='값', nbins=20, title='데이터 분포')
fig.show()
```

- `px.histogram()` 함수는 연속형 데이터의 분포를 확인하는 데 유용합니다.

### 6. 박스 플롯 (Box Plot)

박스 플롯은 데이터의 분포, 중앙값, 사분위수 등을 한눈에 보여줍니다.

```python
import plotly.express as px

data = {'카테고리': ['A', 'A', 'B', 'B', 'C', 'C'], '값': [10, 20, 15, 25, 30, 40]}
df = pd.DataFrame(data)

fig = px.box(df, x='카테고리', y='값', title='카테고리별 값 분포')
fig.show()
```

- `px.box()` 함수를 사용하여 카테고리별 데이터의 범위를 시각화합니다.

### 7. 바이올린 플롯 (Violin Plot)

바이올린 플롯은 데이터의 분포와 밀도를 시각화하는 데 유용합니다.

```python
fig = px.violin(df, x='카테고리', y='값', title='카테고리별 값 밀도')
fig.show()
```

- `px.violin()` 함수는 박스 플롯과 비슷하지만 데이터의 밀도를 더 잘 표현합니다.

### 8. Sunburst 차트 (Sunburst Chart)

Sunburst 차트는 계층적 데이터를 시각화하는 데 사용됩니다.

```python
data = {'지역': ['서울', '서울', '부산'], '구': ['강남구', '송파구', '해운대구'], '매출': [500, 300, 250]}
df = pd.DataFrame(data)

fig = px.sunburst(df, path=['지역', '구'], values='매출', title='지역별 매출 분포')
fig.show()
```

- `px.sunburst()` 함수를 사용하여 계층적 데이터를 표현할 수 있습니다.

### 9. 트리맵 (Treemap)

트리맵은 Sunburst와 유사하지만 직사각형으로 계층을 표현합니다.

```python
fig = px.treemap(df, path=['지역', '구'], values='매출', title='지역별 매출 분포')
fig.show()
```

- `px.treemap()` 함수는 계층 구조를 직사각형으로 시각화합니다.

### 10. 3D 산점도 (3D Scatter Plot)

3D 산점도는 세 변수 간의 관계를 시각화하는 데 사용됩니다.

```python
import plotly.express as px

data = {'x': np.random.rand(100), 'y': np.random.rand(100), 'z': np.random.rand(100)}
df = pd.DataFrame(data)

fig = px.scatter_3d(df, x='x', y='y', z='z', title='3D 산점도 예제')
fig.show()
```

- `px.scatter_3d()` 함수로 3D 공간에서 변수 간의 관계를 시각화할 수 있습니다.