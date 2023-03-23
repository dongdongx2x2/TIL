# Network

## Application layer2_d4_230323



### Reliable

- 신뢰성이 높다는 것은 프로세스 사이에 전달되는 데이터가 유실되지 않고 전달되도록 하는 것

- TCP 는 신뢰성이 높음



### RDT(Reliable data transfer) 신뢰성 있는 데이터 전송

- RDT 1.0: 완벽하게 데이터 전송
  
  - 에러, 유실 x
  
  - 이상적인 상황

- RDT 2.0 
  
  - 패킷 에러만 발생, 유실은 되지 않음
  
  - retransmission(재전송)
    
    - ACK (잘 받은경우) , NAK(에러발생)
    
    - NAK을 받게 되면 재전송 

- RDT 2.1
  
  - RDT 2.0 의 문제점 보완 - 피드백 신호에 에러가 발생하는경우 방지
  
  - Sequence number를 붙여 해결
  
  - Sequence number 0,1 두 개로 표현 -> 헤더의 크기가 늘어나는 것 방지

- RDT 2.2
  
  - NAK을 없앰
  
  - ACK 보내서 마지막으로 받은 정보랑 비교

- RDT 3.0: 패킷 유실, 패킷 에러
  
  - timer 도입 - 시간을 정해서 피드백이 없읍면 유실로 판단
  
  - timer 적절히 설정


