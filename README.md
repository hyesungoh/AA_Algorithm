## After Army Algorithm
___
#### 20.06.16
- BOJ 2588
  간단한 문제, input을 어떻게 사용하는 지 까먹은 내가 레전드.
  조금 더 잘 풀어볼 수 있을 거 같다.
#### 20.06.17
- BOJ 1330
  동시에 입력되는 두 수를 비교한 결과를 출력하는 문제,
  map 함수를 이용하여 아주 조금은 효율적으로 풀지 않았나 생각한다.
- BOJ 2753
  윤년인지 확인하는 문제, 단순히 문제에서 말해준 규칙을 if문으로 나열해 풀었다. 이게 최선인가?
#### 20.06.22
- BOJ 14681
  두 수를 입력받고 어느 사분면에 속하는 지 출력하는 문제, 변수를 사용하지 않고 if문에 input을 사용했다.
- BOJ 2884
  24시간 기준으로 45분을 뺀 시각을 출력하는 문제, 입력받은 분에 45를 뺀 값으로 비교를 했으며 0시 일 때를 따로 확인하여 23시로 바꿔주었다.
#### 20.06.23
- BOJ 5543
  5개의 수를 입력받고, 각 3개, 2개 중 제일 작은 수를 더한 값에 50을 뺀 값이 정답인 단순 구현문제, lambda를 쓸 생각은 했지만 접근 방법이 달랐던 것 같다. min 함수를 쓸 생각은 했다는 것에 일단 만족
- BOJ 2523
  입력받은 수까지 올라갔다가 다시 내려가는 별 찍기 문제, 처음엔 1부터 n까지, n에서 1까지의 range를 합치고 n이 1일 때를 예외처리 했다. ([,1] 이렇게 되기 때문)
  다른 풀이는 출력문에 + n * 절댓값(i)를 해주고 n-1 ~ -n 까지 -1되는 range를 만들었다.
  (n이 3일 때 [2,1,0,-1,-2])
  역시 별 찍기가 뇌를 깨우기 좋은 것 같다.
#### 20.06.24
- BOJ 10996
  별 찍기, 처음보는 유형의 별 찍기여서 상당히 헤맸다.
  찾은 규칙으로는 열의 수는 n*2인 것과 / 한 열에 별과 공백의 총 수는 n / 홀수열일 때 별으로 시작이였다.
  첫 풀이는 이를 가지고 이중 반복문으로 구현을 했다.
  다른 풀이는 나와 달리 반복문 한 개를 가지고 구현했는데 n을 2로 나눈 값을 가지고 구현했는데 조금 더 생각해보면 나도 생각할 수 있었을 것 같다. ~~화이팅~~
- BOJ 10818
  한 열에 여러 수를 입력받고 그 중 제일 큰 수와 작은 수를 출력하는 문제, min과 max를 사용해서 풂
- BOJ 1193
  입대 전에 풀었다가 실패한 문제, [위 글](https://wlstyql.tistory.com/53)을 참조하여 풀었으며 분모, 분자의 합과 stage + 1이 같다는 것을 이용하면 다르게도 풀 수 있을 것 같다.
#### 20.06.26
- BOJ 2562
  9가지의 수를 입력받고 그 중 재일 큰 수와, 그 수가 몇 번째로 입력 되었는 지 출력하는 문제.
  max를 이용하여 숏코딩을 할 수 있었지만 반복문을 한 번 사용하여 확인을 하는 것이 더욱 효율적이라 생각돼 이 방법을 택했다.
- BOJ 3052
  입력받는 10개의 수들을 42로 나눈 나머지 값이 겹치지 않게 몇 개인지 출력하는 문제.
  중복되는 요소가 없는 set 자료형을 이용하여 간편하게 풀었다.
#### 20.06.28
- BOJ 11650
  2차원 좌표를 받고 X 좌표가 증가하는 순으로 정렬, X 좌표가 같을 시 Y 좌표가 증가하는 순으로 정렬하여 출력하는 문제. 파이썬의 sort 메소드의 key를 lambda식을 사용해서 풀었다.
- BOJ 11651
  위 문제의 우선순위가 XY에서 YX로 바뀐 문제 lambda식을 바꿔서 풀었다.
- BOJ 15596
  list를 매개변수로 갖는 함수 solve는 list에 들은 모든 값을 더한 값을 반환해준다. 위 함수를 구현하는 문제. sum 메소드를 사용해서 간단히 풀었다.
#### 20.06.29
- BOJ 2798
  n과 m을 입력 받은 후, 길이가 n인 수들의 배열 l을 입력 받는다. l에 존재하는 수들 중 3개를 합친 값이 m이 넘지 않으며, m과 최대한 가까운 값을 구하는 문제. 3중 반복문을 이용하여 브루트포스 방법을 통해 풀었다.
#### 20.06.30
- BOJ 10828
  스택을 구현하는 문제이다. 처음엔 전역 변수 list, l과 함수들로 구현하였지만 백준 체점 도중 런타임 에러로 인하여 class로 스택을 구현하였으나 이 또한 백준 체점 도중 시간초과로 인해 input = sys.stdin.readline를 이용하여 시간을 단축시켰다. 풀이는 쉬웠으나 체점 기준에 맞추기 힘들었다.
#### 20.07.02
- BOJ 15719
  n과 1 ~ n-1까지 이루어진 수열을 입력받는 다. 수열에는 중복된 수가 한 개 존재하며, 그 것이 문제의 정답이다. 첫 풀이는 단순히 수열을 기준으로 반복문을 수행하고 dictionary에 key에 수열의 수를 넣어 이미 존재하는 수일 때 break하여 그 수를 출력하는 것으로 풀이를 하였으나 백준 체점 기준으로 메모리 초과 결과가 나와 검색해보니 sys.stdin.read()를 사용해야한다 ... 해서 사용해봤으나 EOF를 따로 입력해야하는 read() 특성상 마음대로 구현이 되지 않아 이 부분은 다른 분 풀이를 참고하여 read() 함수를 구현했다.
  read()를 참고하며 본 방법인데 중복된 문자는 1개, 1 ~ n-1까지의 수로 이루어진 수열이라는 특징을 이용해 __1 ~ n-1의 총 합(n*(n-1)//2)에서 수열에 존재하는 모든 수를 뺀 값에 -를 붙이면__+ 정답이 나오게 된다.. 역시 배울 게 남아도 너무 많이 남았다고 생각한다.
#### 20.07.03
- BOJ 1436
  666이 들어간 수 중에 n번째로 큰 수를 출력하는 문제. 브루트포스 방법으로 풀었다.
#### 20.07.05
- BOJ 15668
  숫자 n을 입력받고 n = n1 + n2 방식으로 표현할 때 n1과 n2에서 0~9까지 겹치는 수가 없는 경우를 출력하는 문제. 파이썬의 i "in" word와 같이 사용하는 메소드를 사용하여 풀었다. 첫 풀이에서 큰 수는 생각하지 못한체 반복문의 범위를 n//2+1으로 설정하여 시간초과가 나왔지만 range(1, min(100000, n))으로 바꾸었더니 정상적으로 정답을 맞을 수 있었다. 추가적으로 exit() 함수를 배웠다. 앞으로 유용하게 사용할 것 같다.
#### 20.07.06
- BOJ 13420
  숫자 n만큼 '2 + 2 = 4'와 같은 수식을 입력받고 정답이 맞을 때와 아닐 때 출력을 나눠 하는 문제. 문자열 형식을 실행하는 eval() 메소드를 이용하여 풀었다.
- BOJ 5524
  숫자 n만큼 대문자와 소문자가 섞여있는 문자열을 입력받고 모든 문자열을 소문자로 출력하는 문제. 문자열의 lower() 메소드를 이용하여 풀었다.
- BOJ 2935
  10의 제곱 형태인 두 수와 +, * 중 하나를 입력받고 연산된 수를 출력하는 문제. 첫 풀이에서는 연산 속도를 위해 * 일 때 두 수의 0을 세어 더한 값 A를 '1', '0' * A해서 풀었다. 두 번째 풀이는 eval을 이용하여 숏코딩 스타일로 풀었다.
#### 20.07.07
- BOJ 1408
  12:30:30과 같은 형식으로 입력되는 두 시간들의 차를 구하는 문제. 파이썬의 datetime을 이용하여 풀었으나 백준 기준으로 런타임 에러로 인해 두번째 풀이는 시간과 분을 초로 바꿔 연산하여 풀었다.
#### 20.07.08
- BOJ 12090
  한글로 이루어진 문자열을 입력받은 후 그 문자열의 초성을 출력하는 문제. 한글 초성의 유니코드 상 순서로 이루어진 list를 만들고 각 글자마다 계산하여 ans 문자열에 추가하여 풀었다.
- BOJ 10845
  큐를 구현하는 문제이다. 스택과 마찬가지로 클래스를 이용하여 구현하였다. 백준 풀이상 시간초과 오류로 인해 sys.stdin.readline을 사용하였다.
#### 20.07.09
- BOJ 16394
  1946 이상의 수를 입력받고 해당 년도에 홍익대학교의 개교 몇주년인지 출력하는 문제.
- BOJ 16503
  1 + 2 * 3와 같은 형태로 연산자 + - * /, 4가지와 1 이상의 수 3가지를 입력받는다. 계산 순서에 따라 달라지는 두 값중에 작은 순으로 출력하는 문제. 하지만 나눗셈 연산중에 피연산자 중 하나가 음수이면 양수로 바꿔 계산한 값에 음숫값을 취한다. 첫 풀이는 입력받은 값을 list형으로 변환하여 괄호를 넣어 eval을 이용하여 풀었으나 피연산자가 음수인 나눗셈 연산일 경우를 위해 새롭게 풀기로 하였다. 두번째 풀이는 리스트 슬라이싱을 통해 먼저 계산을 하고 입력되는 숫자는 모두 양수인 것을 이용하여 먼저 계산한 값과 연사자만을 확인하여 연산해주었다. 다른 사람 풀이는 5개의 수, 연산자만 입력되는 것을 이용하여 eval을 이용하여 간단히 푼 것을 볼 수 있는데, 연산 과정에서 나눗셈 연산을 위와 같이하는 줄 모른 내 잘못이 컸다.
#### 20.07.10
- BOJ 10866
  덱을 구햔하는 문제이다. 위 스택과 큐와 같이 클래스를 이용하여 구현했으며 백준 풀이상 시간초과 오류로 인해 sys.stdin.realine을 사용하였다. list.pop(-1)도 마지막 요소를 pop해준 다는 것 또한 알게 되었다.
- BOJ 2789
  문자열을 입력받은 후 'CAMBRIDGE'에 포함된 알파벳을 모두 지워 출력하는 문제. 파이썬의 in 연산자를 사용하여 풀었다.
#### 20.07.11
- BOJ 3040
  9개의 수를 입력받고 합이 100인 7개의 수를 찾는 문제. 이중 반복문을 이용하여 9개의 수를 전부 합한 값에 100을 뺀 값과 비교를 하여 찾은 후 list.remove()하여 풀었다. 다른 풀이는 sum - 100 - 현재 반복중인 값 i으로 비교할 수를 구하고 그 수를 in 연산자를 이용하여 찾아 없애는 풀이다.
- BOJ 3046
  a + X / 2 = b일 때, a와 b를 입력받고 X를 구하는 문제. b*2-a하여 간단히 풀었다.
#### 20.07.13
- BOJ 1026
  n개의 수로 이루어진 두개의 배열을 입력받는다. 두 배열의 요소들을 각각 곱한 값들 중 최솟값을 출력하는 문제. 첫 풀이는 n번 반복하며 min과 max를 이용하여 곱한 값을 더해주었다. 두번째 풀이는 sorted와 map, lambda를 이용하여 조금 더 간단히 풀었다.
#### 20.07.15
- BOJ 2420
  -2,000,000,000 ≤ N, M ≤ 2,000,000,000의 범위를 가진 두 수를 입력받고 두 수의 차이값을 출력하는 문제. n-m값에 abs함수를 이용하여 풀었다.
#### 20.07.17
- BOJ 11784
  1000줄 이하의 16진수로 된 문자열을 입력받은 후 이를 영어로 디코딩하여 출력하는 문제. sys.stdin.read를 이용하여 eof까지 읽어왔으며 .split('\n')을 이용하여 줄바꿈마다 나눠준 후 나눠진 각 문자열들을 bytearray.fromhex(str).decode()을 이용하여 번역 후 출력하였다.
#### 20.07.18
- BOJ 1009
  n과 m을 입력받은 후 n**m의 일의 자릿수를 (0일 때는 10) 출력하는 문제. 첫 풀이는 단순히 str(n**m)[-1]을 통해 풀었으나 수가 커질 수록 걸리는 시간이 크게 늘기 때문에 l = [[10], [1], [6,2,4,8], [1,3,9,7], [6,4], [5], [6], [1,7,9,3], [6,8,4,2], [1,9]] 위와 같이 규칙을 찾아 2차원 리스트로 만든 후 n과 m에 나머지 연산을 통해 출력하였다.
#### 20.07.19
- BOJ 18258
  큐를 구현하는 문제. 첫 풀이는 저번과 같이 sys.stdin.readline으로 시간을 줄이고 class로 구현을 하였다. 하지만 이번 문제에서는 pop후에 요소들을 1칸씩 당기는 과정에ㅐ서 O(n)의 계산량때문에 시간초과 결과를 받게 되어 from collections import deque를 사용하여 구현하였다.
#### 20.07.23
- BOJ 2824
  정수 n을 입력받은 후 n개의 수를 입력받는다. 모든 수를 곱한 값이 A, 같은 방식으로 m과 B를 입력받는다. A와 B의 최대공약수를 출력하는데 만약, 9자리보다 길다면, 마지막 9자리만 출력하는 문제.
  a % b = r일 떄, b % r = r1, r % r1 = r2와 같은 방식으로 나머지값이 0일 때까지 연산하는 유클리드 호제법을 이용하여 풀었으며 파이썬의 문자열 슬라이싱을 이용하여 9자리 이상일 때 예외처리를 하였다.
- BOJ 16430
  1kg의 치즈가 있을 때, a/b kg을 도둑맞았다고 할 때 남은 치즈의 무게를 출력하는 문제. b-a와 b를 공백으로 나누어 출력하여 풀었다.
#### 20.07.27
- BOJ 1712
  노트북을 만들어서 판매할 때 기본 비용 x, 1대 생산시 소모되는 비용 y, 1대가 판매되는 가격이 z라고 했을 때 흑자가 되는 판매 개수를 출력하는 문제. z가 y보다 작을 때는 손익분기점을 넘지 못하므로 -1을 출력하고 그 외의 상황에서는 x//(z-y)+1, 1대 생산하여 보는 이득을 기본 비용에 나눈 값에 1을 더하는 수식을 이용하여 풀었다.
- BOJ 2869
  v라는 높이에 있는 곳을 오르려는 달팽이는 낮에 a만큼 올라가며 밤에는 b만큼 미끌어진다고 한다. v에 도달했을 때는 미끄러지지 않을 때 며칠째에 도착하게 되는 지를 출력하는 문제. 첫번째 풀이는 반복문을 수행하며 v <= (a-b) * t + a라는 수식될 때까지 t를 1씩 더하며 풀었으나 당연히 시간초과를 만났다. 두번째 풀이는 t, (v-b) // (a-b)을 두고 (v-b) % (a-b)가 0일 때, t를 출력하고 아닐 시 t + 1을 출력하여 풀었다. a가 v보다 클 때를 위해 위처럼 풀었으며 다른 사람의 풀이는 (v-b-1)//(a-b)+1를 출력하여 단순히 푼 것을 배웠다. 수학적 사고능력의 부족함을 뼈저리 느꼈다.
#### 20.07.29
- BOJ 2231
  245의 분해합은 (245+2+4+5)하여 256이며 245는 256의 생성자일 때, n을 입력받고 그 수의 생성자를 출력하며 생성자가 없는 수일 때는 0을, 여러 개일 때는 제일 작은 수를 출력하는 문제. 브루트포스 방식을 이용하여 n까지 for문을 수행하며 수를 문자열 타입으로 바꾼 후 sum 함수를 이용한 후 비교해 주었다. 제일 작은 생성자만 출력하면 되기 때문에 출력 후 exit() 해주었으며 반복문이 끝났을 때 0을 출력 해 주었다.
#### 20.07.31
- BOJ 2407
  두 수, n과 m을 입력받은 후 조합 nCm을 출력하는 문제. 팩토리얼은 알았어도 수열과 조합은 무지했던 나는 공식을 찾아본 후에야 풀 수 있었다. 파이썬 itertools의 combinations는 리스트를 반환하므로 문제와 맞지 않아 math의 팩토리얼을 import하여 n! / m! * (n-m)!하여 풀 수 있었다. 부족한 부분이 너무 많다
#### 20.08.02
- BOJ 3009
  x y 형태로 입력되는 3개의 점의 좌표를 입력받은 후 직사각형을 만들기 위해 필요한 네 번째 점의 좌표를 구하는 문제. 첫 풀이는 x와 y 좌표의 딕셔너리를 만들어 몇 번 나왔는 지 확인하기 위해 key에 좌표를, value에 in 연산자를 이용하여 해당하는 값을 넣어주었다. 그 후 dict.items()를 반복돌며 value가 1인 key를 출력하는 형태로 풀었다. 이 과정이 직관적이긴 하여도 효율적이지 못하다는 생각이 들어 두 번째 풀이는 XOR 연산자를 이용하여 풀 수 있다는 참고를 받아 풀어보았다. 첫 번째 풀이보다 상당히 효율적이라 생각한다.
#### 20.08.03
- BOJ 9093
  숫자 n과 n개의 문자열을 입력받는다. 문자열의 공백을 기준으로 단어별 거꾸로 출력하는 문제. 파이썬의 reversed를 이용하여 풀었다.
#### 20.08.04
- BOJ 17413
  <ab cd>abc<abc>와 같은 문자열이 입력됐을 때 <ab cd>cba<abc>같이 <>안의 문자열은 반대로 출력하지 않고 <>밖의 문자열은 반대로 출력하는 문제.
  문자열을 리스트화하여 반복문을 수행하고 현재 문자가 '<', '>', ' '일 때 예외를 두어 출력하고 그 외에 빈문자열에 문자를 계속 더하는 방법으로 풀었다
#### 20.08.05
- BOJ 9987
  포켓몬스터의 번호를 입력받으면 해당 포켓몬의 이름과 속성을 출력하는 문제. 포켓몬스터 홈페이지 크롤링을 직접하지는 않았고 복사하여 딕셔너리 형태와 배열 형태로 저장된 것을 이용하여 풀었다. 첫번째 풀이에서 런타임 에러를 단순 배열이 잘못된 줄 알았지만 포켓몬의 속성이 한 개인 포켓몬도 있었기 때문에 발생한 오류였다. 해당 포켓몬의 속성 배열을 기준으로 for문을 사용하여 출럭하였다.
#### 20.08.06
- BOJ 17298
  n만큼의 수열을 입력받는다. 그 수열들의 오큰수를 출력하는 문제인데, 오큰수란 수열의 오른쪽에 있으면서 자기보다 크며 가장 왼쪽에 있는 수를 뜻한다. 첫 풀이는 이중 반복문을 이용하여 풀었는데 백준 상 시간초과로 인하여 스택을 이용하여 풀어 볼 예정이다.
#### 20.08.07
- BOJ 14918
  두 수를 공백으로 나눠 입력받은 후 더한 값을 출력하는 문제 sum, map, split을 이용하여 간단하게 풀었다.
#### 20.08.10
- BOJ 17298
  위 문제의 시간초과로 인하여 스택을 이용하여 풀어 보았다. range(n-1)을 반복하며 s[i]보다 s[i+1]이 클 떄 정답 리스트인 ans_l에 [i]에 넣었다. 그렇지 못할 때 스택에 push하는데 스택에는 s[i]를 저장하는 list와 i를 저장하는 init_len 리스트를 두어 반복문 수행안에 while 스택의 길이가 0보다 크며 s[i+1]이 스택의 맨 마지막에 들어온 것보다 클 때 ans_l에 추가하여 풀었다. 다른 사람의 풀이를 보니 아직 배울 점이 많은 걸 또 깨달았다.
- BOJ 10818
  태국은 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 불기 연도를 입력받은 후 서기 연도를 출력하는 문제. 543년 차이가 나기 때문에 간단한 사칙연산을 이용하여 풀었다.
#### 20.08.11
- BOJ 17496
  작물을 판매할 수 있는 총 가격을 출력하는 문제. 입력받는 d, g, n, p는 각 기를 수 있는 일 수, 자라는 데 걸리는 일 수, 한 번에 심을 수 있는 수, 가격이다. 문제에서 처음 심는 날을 1일으로 정해놓았기 때문에 (d-1)//g*n*p를 계산하여 풀었다.
- BOJ 11931
  n개의 수를 각 줄마다 입력받고 내림차순으로 정렬하여 각 줄마다 출력하는 문제. 첫풀이에서 시간초과 결과를 받게 되어 sys.stdin.readline을 import하였디. 그 후 sorted(퀵 정렬)와 reverse=True를 이용하여 풀었다.
- BOJ 4470
  n개의 문자열을 입력받고 각 입력받은 문자열 앞에 '1. ~', '2. ~', '3. ~'과 같이 줄 번호를 붙여서 출력하는 문제. for 반복문을 range(n)을 기준으로 돌며 i+1과 '. '을 input()한 것에 더 한 것을 출력하여 풀었다
#### 20.08.12
- BOJ 17293
  n을 입력받은 후 n ~ 0까지 이어지는 노래 가사를 출력하는데 가사의 첫 줄은 n bottles, n이 1일 때는 bottle, 0일 때는 no more bottles로 나누어 출력해야 한다. 두번째 줄은 n-1 bottles, n-1이 1일 때는 bottle, i-1이 0일 때는 no more bottles로 출력해야 한다. 추가적으로 마지막 문장은 다르며 n bottles 혹은 bottle을 출력해야한다. 첫 풀이는 단순 if문과 삼항연산자를 이용하여 풀었으며 두번째 풀이는 함수를 이용하여 풀었으나 백준 풀이상에서는 틀렸다고 나오는 데 이유를 아직 못찾았다.
#### 20.08.13
- BOJ 2455
  4개의 줄을 입력받으며 각 줄마다 열차에 '하차한 승객 수' '승차한 승객 수'를 입력받는 다. 승객이 가장 많이 탑승하고 있을 때가 몇명인지 출력하는 문제. 반복문을 4번 수행하며 t 변수에 t + 승차한 승객 수 - 하차한 승객 수를 계산하였고 max 함수를 이용하여 t와 저번 반복문에 수행된 ans와 비교를 하여 풀었다.
- BOJ 2460
  위 문제와 동일하며 다른 점은 10번 반복을 한다는 점. 반복문을 10번 수행하게 바꾸어서 풀었다.
#### 20.08.14
- BOJ 15963
  한 문자열에 공백을 기준으로 두 개의 수를 입력받고 같으면 1 다르면 0을 출력하는 문제. split()과 삼항연산자를 이용하여 풀었다.
- BOJ 14405
  문자열이 입력되고 'pi', 'ka', 'chu'를 제외한 다른 단어가 있을 때 NO, 세 단어로만 이루어져 있을 때 YES를 출력하는 문제. 첫 풀이 때 replace('pi', '')와 같이 단어를 공백으로 바꿔주었는데 'kpia'와 같은 문자열에서 pi가 없어져 'ka'가 있다고 판단하기 때문에 replace를 '/'로 하였고 최대 문자열의 길이인 '/'*5000과 in 연산자로 비교하여 '/'가 아닌 다른 문자가 있을 때 NO를 출력하게 풀었다. 다른 풀이는 replace를 ' '으로 하여 strip 함수를 이용하여 푸는 것이다
#### 20.08.16
- BOJ 1271
  숫자 n과 m을 입력받은 후 나눈 값과 나머지를 출력하는 문제
- BOJ 2338
  숫자 n과 m을 입력받은 후 +, -, x 연산을 하야 출력하는 문제
- BOJ 2475
  5가지 수를 입력받은 후 각 수를 제곱한 수들의 합에 10으로 나눈 나머지를 출력하는 문제. 함수를 만들어서 풀었다.
- BOJ 2845
  두 수 n, m을 입력 받은 후 곱한 값에 다음 줄에 입력되는 5가지 수와 비교한 값을 출력하는 문제. input.split한 값을 기준으로 for문을 수행하여 풀었다.
- BOJ 2914
  n과 m을 입력받은 후 A를 구하면 된다. A / n이 m이지만 A / n에서 소수값이 있을 때 m은 +1한 정수가 되게 된다. n * (m-1) + 1 수식을 이용하여 풀었다.
- BOJ 3003
  정해진 수들과 비교하여 차이값을 출력하는 문제 input.split한 리스트와 range(6)을 기준으로 수행되는 for문을 이용하여 풀었다.
- BOJ 5522
  5개의 줄에 입력되는 수들의 총합을 출력하는 문제.
- BOJ 5554
  4개의 줄에 입력되는 수들을 분과 초로 출력하는 문제. 60으로 나눈 값과 나머지를 출력하여 풀었다.
- BOJ 1085
  x, y, w, h를 입력받는 다. (x, y)는 현재 내 위치이고, 사각형의 왼쪽 아랫점은 (0, 0), 오른쪽 위의 점은 (w, h)라고 할 때 사각형 밖으로 나갈 수 있는 제일 짧은 거리를 출력하는 문제. min을 사용하여 x, y, w-x, h-y를 비교하여 풀었다.
#### 20.08.19
- BOJ 17256
  숫자 세개로 이루어진 두 개의 문자열을 각각 a,b,c / x,y,z라고 할 때 x-c, y//b, z-a라는 수식을 도출해 출력하는 문제
#### 20.08.21
- BOJ 5596
  공백으로 나누어진 4개의 수를 두 줄 입력받은 후, 총합이 큰 것을 출력하는 문제. max와 sum 함수를 이용하여 풀었다.
- BOJ 1247
  3번에 걸쳐 정수 n만큼 수를 입력받은 후 총합의 부호를 출력하는 문제. 현재 시간초과 결과를 보여주어, sys.stdin.readline을 import하여 해결하였다.
#### 20.08.23
- BOJ 2480
  공백으로 나누어진 3개의 수를 입력받은 후, 같은 수가 3개일 때 10000 + (같은 수) * 1000, 같은 수가 2개일 때 1000 + (같은 수) * 100, 같은 수가 없을 때는 (제일 높은 수) * 100 한 값을 출력하는 문제. 내 풀이는 리스트의 count 메소드를 사용하여 a, b 각 count하여 변수 n과 num에 같은 수가 몇 개인지, 그 수는 무엇인지 저장을 하여 if문으로 나누어 따로 출력하는 부분을 만들었다. 상당히 비효율 적으로 풀었다 생각하여 다른 사람의 풀이를 본 결과 sorted 함수를 사용하여 간단히 풀 수 있는 걸 배우게 되었다.
#### 20.08.26
- BOJ 2530
  공백을 기준으로 나누어진 시간, 분, 초를 입력받은 후 초를 입력받아 시간을 계산해서 출력하는 문제. 입력받은 시간을 초로 계산 후 더한 다음, 다시 계산하여 풀었다.
#### 20.08.28
- BOJ 1267
  휴대폰 요금제 2개가 있을 떄 어떤 요금제가 더욱 싼지 출력하는 문제. 나누기 연산과 삼항 연산자를 이용하여 풀었다.
#### 20.08.29
- BOJ 1254
  문자열 s를 입력받은 후 문자열의 뒤부터 0개 이상의 단어를 추가해서 만들 수 있는 펠린드롬 단어중 제일 짧은 단어의 길이를 출력하는 문제. 내 풀이는 펠린드롬 인지를 확인하는 함수를 만든 후, 문자열의 길이만큼 반복문을 수행하며 s에 s[0:i+1]을 reversed하여 더한 문자열을 펠린드롬 확인 함수를 사용하여 정답을 출력하였다. <i>1234 + 1 > 1234 + 21 > 1234 + 321 </i> 다른 사람의 풀이는 s를 앞에서부터 슬라이싱한 값에 reversed한 문자열이 있는 지 확인하는 방식이다.
#### 20.08.30
- BOJ 1260
  정점의 개수 n, 간선의 개수 m, 시작할 정점의 번호 start를 입력받은 후 그래프를 dfs, bfs로 읽었을 때 순서를 출력하는 문제. 그래프는 양방향으로 이어지는 정점 x y를 입력받는데, 이를 딕셔너리로 저장을 하였다. bfs와 dfs 모두 함수로 구현을 하였으며 deque를 import하여 사용을 하였으며 bfs는 큐를 이용하여 sorted한 연결된 정점들을 큐에 넣으며 풀었으며, dfs는 스택을 이용, reverse=True한 sorted한 연결된 정점들을 스택에 넣으며 풀었다.
#### 20.09.01
- BOJ 2606
  정점 1과 연결된 모든 정점들의 수를 출력하는 문제. 스택을 사용하는 dfs를 구현하여 len(visit)-1 하여 풀었다.
#### 20.09.03
- BOJ 2667
  n*n의 크기의 0과 1로 이루어진 2차원 배열을 입력받은 후, 상하좌우 연결된 1의 수의 집합들의 수와 각 집합의 수를 정렬하여 출력하는 문제. 재귀적으로 배열의 상하좌우가 1인지 확인하며 count에 1씩 더하며 count를 반환하며 해당 배열 인자를 0으로 바꾸는 함수 dfs를 만들었으며, 이 중 배열의 크기를 넘는 경우를 위해 두 개의 조건문 중에 배열의 크기 확인을 and 앞에두는 것으로 방지할 수 있다는 것을 배웠다. 이후 배열의 모든 부분을 2중 반복문을 사용하여 1인지 확인하여 ans 리스트에 append한 후 sorted와 len 함수를 사용하여 풀었다.
- BOJ 10872
  숫자 n을 입력받은 후 n!을 출력하는 문제. math 라이브러리의 factorial을 import해서 풀었으며, 재귀 함수를 구현해서 풀기도 하였다.
#### 20.09.04
- BOJ 13752
  테스트케이스 횟수 n을 입력받은 후 입력되는 숫자만큼 '='을 출력하는 문제 반복문과 문자열 곱하기 연산을 이용하여 풀었다.
- BOJ 15000
  입력되는 문자열을 대문자로 변환하여 출력하는 문제. 문자열 내장 함수 upper을 이용하여 풀었다.
#### 20.09.05
- BOJ 2178
  미로의 크기 n, m이 주어진 후 1과 0으로 이루어진 미로가 입력된다 1은 이동할 수 있는 곳, 0은 이동할 수 없는 곳이라고 하였을 때, (0, 0)에서 출발하여 (n-1, m-1)까지 걸리는 최단 거리를 계산하는 문제. 방문했는지 확인, 거리를 저장할 2차원 배열을 만들었으며, 상하좌우 방문 확인 배열의 값이 False인지, 그래프의 값이 1인지를 확인한 후 deque에 append하여 풀었다.
#### 20.09.06
- BOJ 1325
  두 개의 컴퓨터 번호 x, y가 주어졌을 때 y를 해킹하면 x도 해킹할 수 있다고 한다. 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 문제. 첫 풀이는 dfs, 깊이우선탐색으로 구현을 하였으나 백준풀이상 시간초과 결과를 받게 되었고, 검색 후 deque를 사용한 bfs와 sys.stdin.readline을 사용하여 시간을 줄이고 기존 내 풀이와 다르게 그래프를 2차원 배열로 저장하였다. 그렇게 하여도 백준 python3 채점 기준에는 통과하지 못하여 pypy3로 변경하여 풀 수 있게 되었다.
- BOJ 5567
  정해진 수만큼의 x y와 같이 연결된 정점이 입력된다. 정점 1과 연결된 정점들의 정점까지 갯수를 출력해야 한다. 정점 1과 연결된 정점이 2와 3이면 정점 2, 3을 포함한 2, 3 정점과 연결된 정점의 수를 출력하는 문제. 입력되는 수를 바탕으로 양방향 그래프를 만든 후, extend를 사용하여 1과 연결된 정점들을 리스트 que에, 중복을 제거하기 위해 집합 자료형 visit에 graph[1]을 넣었다. que에 든 정점 1과 연결된 정점 i를 사용하여 반복문을 수행하며 그 안에 graph[i]를 기준으로 반복문을 수행하며 안의 값을 집합 자료형 visit에 넣었다. 정답은 1을 제외해야하기 때문에 len(visit) - 1을 하여 풀었다.
