import math


# gcd(최대공약수) : 공약수 중 가장 큰 값(ex. 30과 15의 최대공약수는 15)
# *공약수 : 두 수 이상의 여러 수의 공통된 약수
# *문제 유형 : 똑같이 나누기, 크기 쪼개기 등(가장 큰이라는 단어 등장)

# lcm(최소공배수) : 양의 공배수 중 가장 작은 값(ex. 3과 5의 최소공배수는 15)
# *공배수 : 두 수의 공통 배수
# *문제 유형 : 동시에 출발해서 다시 만날 때, 연결하기, 쌓기 등(가장 작은이라는 단어 등장)

# *유클리드 호제법 : 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

def gcd_use_math(a, b):
    '''python3--version >= 3.5'''
    # Python 3.9 버전부터는 math.gcd의 인수로 여러개 사용 가능, 3.9 미만 버전에서는 2개까지만 가능
    return math.gcd(a, b)

def lcm_use_math(a, b):
    '''python3--version >= 3.9'''
    return math.lcm(a, b)

def gcd_use_euclidean(a, b):
    return b if a & b == 0 else gcd_use_euclidean(b, a%b)

def lcm_use_euclidean(a, b):
    return (a*b) // math.gcd(a, b)

a, b = 8, 12
print(gcd_use_math(a, b))
print(gcd_use_euclidean(a, b))
print(lcm_use_math(a, b))
print(lcm_use_euclidean(a, b))