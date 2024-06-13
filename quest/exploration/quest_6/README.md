🔑 **PRT(Peer Review Template)**
리뷰어: 윤소정

- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부
        - 1. Abstractive 모델 구성을 위한 텍스트 전처리 단계가 체계적으로 진행되었다.
             분석단계, 정제단계, 정규화와 불용어 제거, 데이터셋 분리, 인코딩 과정이 빠짐없이 체계적으로 진행.
             분석,정제단계<br>
             ![image](https://github.com/zave7/aiffel-research/assets/104029654/7e41f395-df23-49f4-8690-6a0605a9729a) <br>
     
             정규화와 불용어 제거<br>
             ![image](https://github.com/zave7/aiffel-research/assets/104029654/cf9379a5-c9b9-4ef4-ad54-810abb3f98a6)<br>
     
             데이터셋 분리<br>
             ![image](https://github.com/zave7/aiffel-research/assets/104029654/36a88c62-ad99-4787-8b02-8f1e6fdf6180) <br>
     
             인코더, 디코더 설계 <br>
             ![image](https://github.com/zave7/aiffel-research/assets/104029654/57eb1996-9e57-425d-adf5-06d76832fb18)<br>
         
             
        - 2.텍스트 요약모델이 성공적으로 학습되었음을 확인하였다.
          * 모델 학습이 진행되면서 train loss와 validation loss가 감소하는 경향을 그래프를 통해 확인했으며, 실제 요약문에 있는 핵심 단어들이 요약 문장 안에 포함되었다.<br>
            ![image](https://github.com/zave7/aiffel-research/assets/104029654/451c9720-3689-4d4d-9625-2176ca1a0bef) <br>

          
        - 3.Extractive 요약을 시도해 보고 Abstractive 요약 결과과 함께 비교해 보았다.<br>
            * 추상적 요약<br>
          ![image](https://github.com/zave7/aiffel-research/assets/104029654/65bc0508-946b-4664-ad38-0ca45c5e4346) <br>
            * 추출적 요약 <br>
            ![image](https://github.com/zave7/aiffel-research/assets/104029654/5fdfabd1-94e3-49ba-8ea1-32acf2cfd7ee) <br>




- [X]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [X] 코드 내용에 대한 설명이 잘 기록되어있음 <br>
       ![image](https://github.com/zave7/aiffel-research/assets/104029654/29c8ce0b-f81f-4269-ab11-61c640aed879)


- [ ]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [X]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등) - 아직 거기까지는 하지 못했다고 하심
    - [ ]  각 실험을 시각화하여 비교하였나요? - 아직 거기까지는 하지 못했다고 하심
    - [ ]  모든 실험 결과가 기록되었나요? - 아직 거기까지는 하지 못했다고 하심

- [X]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [X]  배운 점
    - [X]  아쉬운 점
    - [X]  느낀 점
    - [X]  어려웠던 점
  ![image](https://github.com/zave7/aiffel-research/assets/104029654/5c7952c7-3026-4f80-bac9-6f468e1f4959)

_________________________________________________________________________________________________
### 리뷰자 느낀점
깔끔하게 보고서를 잘 작성해주신 것 같습니다. 그리고 AddictiveAttention이 무엇인지에 대해서도 알아보시고 같이 공유해주셔서 덕분에 지식을 하나 더 얻게되었습니다. 노드 학습때 예측 요약이 잘 되지 않아 제 모델이 문제가 크다고 생각했는데 대부분 다 비슷한 결과를 나온 것을 보고 모델을 많이 발전시켜야 좋은 결과가 나오겠다는 것을 알게된 좋은 시간이었던 것 같습니다.
