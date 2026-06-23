import time
import random

def cdprt(S):
    line = S.split("\n")
    for i in line:
        for k in i:
            time.sleep(0.05)
            print(k, end = "", flush = True)
        k = random.random()
        if(k<0.05):
            print()
            progress_bar()
        print()


def progress_bar():
    print()
    for i in range(40):
        a = "■"*i
        b = " "*(40-i)
        p = round(((i+1)/40)*10000) / 100
        print(f"\r[{a}{b}] {p}%", end = "")
        time.sleep(0.1)
        

S1 = '''Sen = input("문장:").split(" ")
Find = input("찾을 단어:")
L1 = {}
L2 = {}

for word in Sen:
    if word in L1:
        L1[word] += 1
    else:
        L1[word] = 1

for word in Sen:
    word = word.lower()
    if word in L2:
        L2[word] += 1
    else:
        L2[word] = 1

if Find in L2:
    print(f"등장 횟수: {L1[Find]}")
    print(f"대소문자 없이 등장 횟수: {L2[Find]}")
else:
    print("단어를 찾을 수 없습니다.")'''

S2 = '''Sentence = input("입력:")
chars = {"대문자":0, "소문자":0, "숫자":0, "공백":0}

for s in Sentence:
    if s.isupper():
        chars["대문자"] +=1
    if s.islower():
        chars["소문자"] +=1
    if s.isnumeric():
        chars["숫자"] +=1
    if s.isspace():
        chars["공백"] +=1

for i in chars:
    print(f"{i}: {chars[i]}")


print(f"거꾸로: {Sentence[::-1]}")
'''

S3 = '''class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, mbal):
        self.balance = self.balance + mbal

    def withdraw(self, money):
        if money <= self.balance:
            self.balance = self.balance - money
        else:
            print("잔액이 부족합니다.")

    def getBalance(self):
        return self.balance

    def __str__(self):
        return f"이름: {self.name}\n잔액: {self.balance}"

name = input("이름:")
balance = int(input("초기 잔액:"))
mbal = int(input("입금액:"))
money = int(input("출금액:"))

Account = BankAccount(name, balance)
Account.deposit(mbal)
Account.withdraw(money)

print(Account.__str__())
'''

S4 = '''p = 8

for i in range(p):
    b = " "
    print(b*((p-i)*2 + 1), end = " ")
    for k in range(i):
        time.sleep(0.05)
        print (k+1, end = " ", flush = True)
    for k in range(i-1):
        time.sleep(0.05)
        print (i-k-1, end = " ", flush = True)
    time.sleep(0.05)
    print()
'''

S5 = '''
scL = []
nmL = []

with open("names.txt","r",encoding = "utf-8") as file:
    for name in file:
        name = name.rstrip()
        nmL.append(name)
        scL.append(int(input(f"{name} 점수:")))

with open("score.txt","w",encoding = "utf-8") as file:
    for i in range(len(nmL)):
        file.write(f"{nmL[i]} {str(scL[i])}\n")

total = sum(scL)
average = total / len(nmL)

print(f"총합 : {total}\n평균 : {average}")

with open("names.txt", "w", encoding = "utf-8") as file:
    file.write(input("이름 1:"))
    file.write("\n")
    file.write(input("이름 2:"))
    file.write("\n")
    file.write(input("이름 3:"))
    file.write("\n")
    print("저장 완료")
'''

Army = '''높은 산 깊은 골 적막한 산하
눈 내린 전선을 우리는 간다
젊은 넋 숨져간 그 때 그 자리
상처 입은 노송(老松)은 말을 잊었네
전우여 들리는가 그 성난 목소리
전우여 보이는가 한 맺힌 눈동자
'''

Never = '''We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
'''


L = [S1, S2, S3, S5]
Special = [S4]

print("이 프로그램은 어떠한 동작도 하지 않으며, \n그냥 코딩 잘하는것처럼 보이게 만드는 프로그햄입니다.")
print("프로그램을 종료하고 싶다면 '->'가 나왔을때 -1을 입력해 주십시오(이스터에그 있음)")


while (1):
    s = input("->")
    if s == "-1":
        break

    if s == "Army":
        progress_bar()
        print()
        cdprt(Army)
        continue

    if s == "Never":
        progress_bar()
        print()
        cdprt(Never)
        continue

    choice = random.choice(L + Special)
    if choice in Special:
        exec(choice,globals())
    cdprt(choice)
    if(random.random()<0.5):
        progress_bar()
        print()


























