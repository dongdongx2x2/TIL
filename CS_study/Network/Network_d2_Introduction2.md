# Network

## Introduction2_d2_230311

### Socket

- 프로세스는  socket을 통해 message 주고 받음

- socket은 OS에서 제공하는 API 중 하나

- socket의 주소에 해당하는 것이 IP주소와 포트 번호

- 포트번호는 원한느 프로세스를 찾아가는 역할



### What transport service does an app nee?

- application layer가 transport layer에 원하는 기능
  
  - data integrity: 데이터 유실되지 않고 목적지에 도착
  
  - timing: 시간 내에 보냄
  
  - throughput : 처리량
  
  - security: 안전성

- TCP를 사용할경우 data integrity만 보장됨. 나머지 요소들은 application layer에서 알아서 처리



### HTTP

- hyperteext transfer progocol: 하이퍼 텍스트를 전달하는 프로토콜

- 하이퍼텍스트:다른 파일들의 링크되어있는 텍스트

- request와 response를 주고받음

- TCP를 사용

- stateless:클라이언트 상태를 저장하지않음



### HTTP Connections

- non-persistent HTTP
  
  - 지속적이지 않운 HTTP
  
  - TCP 커넥션을 HTTP 사용후 close
  
  - 매 http마다 TCP 커넥션을 요청(비효율적)
  
  - 응답시간이 persistent보다 오래 걸림

- persistent HTTP
  
  - 지속되는 HTTP
  
  - client/server 간 하나의 TCP 커넥션으로 수행(효율)


