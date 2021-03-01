### chap03에 쓰이는 func들 ###
print("hello world")
import numpy as np

## 단위샘플시퀀스(단위샘플위치, 순서시퀀스 시작, 끝)
def impseq(n0,n1,n2):
    N = n2-n1+1             # 시퀀스 길이
    n = np.arange(N)        # 순서 시퀀스
    xn = np.zeros(N)        # 데이터 어레이 설정
    for i in range(N):      # 단위 샘플 시퀀스 생성
        if (n1+i) == n0:    # 시작점에서 i만큼 이동한 곳이 단위샘플 위치라면
            xn[i] = 1        # i번째에 1
    return xn               # i번째에 단위 임펄스를 갖고 있는 xn을 리턴

## 단위계단시퀀스(계단시작 위치, 순서시퀀스 시작, 순서시퀀스 끝
def stepseq(n0,n1,n2):
    N = n2-n1+1             # 시퀀스 길이
    n = np.arange(N)        # 순서 시퀀스
    xn = np.zeros(N)        # 데이터 어레이 설정
    for i in range(N):      # 단위계단 시퀀스 생성
        if (n1+i) >= n0:
            xn[i] = 1
    return xn

## 신호덧셈(x1,x2라는 두 개의 순서 시퀀스가 n1,n2라는 순서 시퀀스에 맞게 들어온다)
# x1 = {0,0,0(b),1,2,3,4,5,6,7,9}      n1 = {0,1,2,3,4,5,6,7,8,9,10}      <- 당연히 x1과 n1의 크기는 같아야함
# x2 = {1,2,3,4,5,6(b),7,8,9,10,11}    n2 = {-5,-4,-3,-2,-1,0,1,2,3,4,5}  <- 당연히 x2와 n2의 크기는 같아야함
# 이처럼 두 시퀀스의 길이와 순서가 다르기 때문에 이들을 일치시켜줘야 연산이 가능 -> Zero Padding
def sigadd(n1,x1,n2,x2):
    nk = np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)     # 전체 시퀀스 축 -> arange(-5,14) -5~13까지
    N = len(nk)                                                     # 시퀀스 축 길이
    y1 = np.zeros(N)                                                # x1에 대한 zero padding
    y2 = np.zeros(N)                                                # x2에 대한 zero padding
    aa = abs(min(min(n1),min(n2)))                                  # 순서 시퀀스를 0부터 시작하게끔 맞추기 위한 이동폭
    n1 = n1 + aa; n2 = n2 + aa                                      # np.array([])라 가능, list는 불가능
    y1[int(min(n1)):int(max(n1)) + 1] = x1                          # 샘플저장
    y2[int(min(n2)):int(max(n2)) + 1] = x2                          # 샘플저장
    y = y1 + y2
    return nk,y,y1,y2

## 신호곱셈
def sigmult(n1,x1,n2,x2):
    nk = np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
    N = len(nk)
    y1 = np.zeros(N); y2 = np.zeros(N)
    aa = abs(min(min(n1),min(n2)))
    n1 = n1 + aa; n2 = n2 + aa
    y1[int(min(n1)):int(max(n1)) + 1] = x1
    y2[int(min(n2)):int(max(n2)) + 1] = x2
    y = y1.T*y2                                                      # 샘플대 샘플 곱셈
    return nk,y,y1,y2