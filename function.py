#예제1) 리턴문도 없고, 인자도 없는 함수
def printHello():
    print("Hello, user")

printHello()

#예제2) 리턴문이 없는 함수, 인자는 있고
def printHi(name):
    print("Hi",name)

#아래의 name 은 위의 name 과 다른 것
#name = input("당신의 이름은? ")
#printHi(name)

#예제3) 리턴문이 있는 함수
def printWelcome(user):
    word = "Welcome, " + str(user) #str은 안에 있는 값을 무조건 문자열로 바꿔줌
    return word

#user = input("당신의 학번은? ") #input 은 문자열?
#print(printWelcome(user))


#예제4) 세 개의 값을 동시에 리턴하는 함수
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

a = func_mul(10)
#print(type(a), a)
#fuc_mul 함수 사용시 여러 개 선언하면 값도 abc 처럼 그 수를 맞춰줘야 함

#문자열 안에 우리가 원하는 값을 쉽게 삽입해보자 -> formatting
#파이썬에는 여러 문자열 포매팅 방법이 있습니다!
#여기서는 format 함수를 사용한 포매팅만 알고 넘어갑시다!
#더 자세한 포매팅방법을 알고 싶다면 https://wikidocs.net/13 을 참고해주세요!

#1_문자열에 숫자를 바로 대입하기
print("저는 덕성 멋자 {0}기 입니다.".format(9))

#2_문자열에 문자열 입력받아 대입하기
#fruit = input("당신이 좋아하는 과일은? ")
#print("내가 좋아하는 과일은 {}입니다.".format(fruit))

#3_2개 이상의 값 넣기(숫자는 인덱스, 문자는 이름으로 삽입)
print("저는 {0}학번 {major}과입니다.".format(21,major = "글로벌융합대학"))