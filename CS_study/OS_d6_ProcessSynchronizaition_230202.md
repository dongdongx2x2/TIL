# CS 스터디 - day06_230202

## 운영체제(Operating systems, OS)

### Process Synchronization

1.  Race condition
   
   <img src="OS_d6_ProcessSynchronizaition_230202_assets/2023-02-01-22-34-06-image.png" title="" alt="" width="476">
   
   - 하나의 공유 data에 여럿이 접근하려고 할 때, 즉 연산할 수 있는 주체가 여러 개일 떄 발생하는 문제
   
   - S-box를 공유하는 E-box가 여럿 있는 경우 , race condition의 가능성이 있음

2.  OS에서 race condition 발생 하는 경우
   
   - kernel 수행 중 인터럽트 발생 시
     
     - <img src="OS_d6_ProcessSynchronizaition_230202_assets/2023-02-01-22-41-07-image.png" title="" alt="" width="333">
     
     - 커널 모드에서 수행중 더 급하고 중요한 인터럽트가 발생해 인터럽트 처리 루틴이 수행하도록 CPU를 넘길 떄
     
     - 양쪽다 커널 코드이므로 kernal address space를 공유한다
     
     - 해결법 : count 변수를 건드리기전에 interrupt disable 시켜둠.
   
   - 프로세스가 시스템 콜을 하여 커널 모드로 수행 중인데 context switch가 일어나는 경우
     
     - <img src="OS_d6_ProcessSynchronizaition_230202_assets/2023-02-01-22-43-28-image.png" title="" alt="" width="344">
     
     - 두 프로세스의 address space 간에는 data sharing이 없음
     
     - 그러나 시스템콜을 하는동안에는 kernel address space의 data를 access하게 됨
     
     - 이 작업 중간에 CPU를 preempt 해가면 race condition 발생
     
     - 해결책: 커널 모드에서 수행 중일 때는 CPU를 preempt하지 않음, 커널 모드에서 사용자 모드로 돌아갈 떄 preempt
   
   - Multiprocessor에서 shared memory 내의 kernel data
     
     <img src="OS_d6_ProcessSynchronizaition_230202_assets/2023-02-01-22-47-06-image.png" title="" alt="" width="499">
     
     - 해결 법 1 : 한번에 하나의 CPU만이 커널에 들어갈 수 있게 하는 법
     
     - 해결 법 2: 커널 내부에 있는 각 공유 데이터에 접근할 때마다 그데이터에 대한 lock / unlock을 하는 방법
       
       
