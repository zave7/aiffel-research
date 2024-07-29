# 캘리포니아 주택 데이터셋 요약

**인스턴스 수:** 20,640

**속성 수:** 8개의 수치형 예측 속성과 1개의 목표 변수

**속성 정보:**
- **MedInc:** 블록 그룹의 중간 소득
- **HouseAge:** 블록 그룹의 중간 주택 연령
- **AveRooms:** 가구당 평균 방 개수
- **AveBedrms:** 가구당 평균 침실 개수
- **Population:** 블록 그룹 인구
- **AveOccup:** 가구당 평균 인원수
- **Latitude:** 블록 그룹 위도
- **Longitude:** 블록 그룹 경도

**목표 변수:** 캘리포니아 지역의 중간 주택 가격 (단위: 10만 달러)

**누락된 속성 값:** 없음

**데이터셋 출처:** StatLib 저장소에서 제공된 1990년 미국 인구 조사

**배경:**
- 각 행은 블록 그룹을 나타내며, 이는 미국 인구 조사국이 데이터 샘플을 공개하는 가장 작은 지리적 단위입니다. 블록 그룹은 보통 600명에서 3,000명 사이의 인구를 가집니다.
- 가구당 평균 방 개수와 침실 개수는 휴양지와 같이 가구 수가 적고 빈 집이 많은 블록 그룹에서 큰 값을 가질 수 있습니다.

**사용 방법:**
- `sklearn.datasets.fetch_california_housing` 함수를 사용하여 다운로드/로드할 수 있습니다.

**참고문헌:**
- Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions, Statistics and Probability Letters, 33 (1997) 291-297

[데이터셋 링크](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)