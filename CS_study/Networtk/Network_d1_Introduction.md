# Network

## Introduction_d1_230304

1.  네트워크 구조
   
   - 네트워크 엣지
     
     - 앱과 호스트
   
   - 네트워크 코어
     
     - 라우터
     
     - 네트워크
   
   - 네트워크 접근
     
     - 링크로 네트워크들 이어줌

2.  네트워크 엣지
   
   - 엔드 시스템(호스트)
     
     - 프로그램 실행
   
   - 클라이언트/서버 모델
     
     - 클라이언트- 요청
     
     - 서버 -제공

3. connection-oriented service
   
   - TCP
     
     - reliable, in-order byte-stream data transfer 순차적인 데이터전송
     
     - flow control:  받는 쪽의 능력 고려해 전송
     
     - congestion control: 속도를 낮춰 전송
   
   - UDP
     
     - connectionless
     
     - unreliable data transfer
     
     - no flow control
     
     - no congestion control
     
     - 하지만 속도가 빠름

4. 네트워크 코어
   
   - 라우터들의 집합
   
   - circuit switching
     
     - 출발에서 목적지까지 가는 길 미리 설정
     
     - 동시 사용 인원 적음
   
   - packt shitching
     
     - 유저의 패킷 요청시 순서가 정해짐
     
     - 낭비 없음
     
     - 패킷 딜레이 발생

5.  패킷 딜레이
   
   - nodal processing: 새로운 패킷 받으면 검사하는 단계 -> 딜레이 발생
   
   - queueing: 큐에 순서대로 대기 시킴 -> 딜레이 발생
   
   - transmission delay: 패킷의 첫 bit가 나가는 순간부터 마지막 bit가 나가기까지의 시간 
   
   - propagation delay: 전송시간(케이블 길이에 비례)

6. 패킷 딜레이 줄이는 법
   
   - 라우터 성능 개선
   
   - 케이블 개선
   
   - queueing delay는 사용자들에 의한 것이기 때문에 조절 불가


