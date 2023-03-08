# Algorithm 배열1(Array1)

1.  카운팅 정렬(Counting Sort)
   
   - 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적 알고리즘
   
   - 제한 사항
     
     - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
     
     - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함
   
   - 시간복잡도
     
     -  O(n+k): n은 리스트 길이, k는 정수의 최댓값

2.  완전 검색
   
   - 완전 검색은 생각할 수 있는 모든 경우의 수를 나열해 확인하는방법
   
   - Brute-force 혹은 generate-and-test 기법이라고도 불림
   
   - 일반적으로 경우의 수가 상대적으로 작을 떄 유용

3.  탐욕(Greedy ) 알고리즘
   
   - 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적 방법
   
   - 여러 겅우 중 하나를 결정해야할 때 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식
   
   - 각 선택의 시점에서 이루어지는 결정은 지역적으로 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다 하여 그것이 최적이라는 보장이 없음



