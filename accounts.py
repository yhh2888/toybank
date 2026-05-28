# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 

import UserSystem

UserSystem. 

userId = int(input('ID:'))
accountNum = int(input('계좌번호:'))

class Account:
   
accountsDict = {}
userTotalBalence = {}

def __init__(self, id, account, balance):
        self.idkey = id 
        self.useracc = account
        self.userbudget = balance
       
        Account.accountsDict[id] = account
        userTotalBalence.append(balance)
        
def isaccount(self):
    
    if accountNum in accountsDict:
            return '계좌가 이미 있습니다.'
    else:
            return '계좌가 없습니다.'
    
def Deposit(self):
        userDeposit= int(input('입금액을 입력하세요:'))
        userTotalBalence += userDeposit
        return userTotalBalence
    
def Withdrawal(self):   
        userwithdrawal = int(input('출금액을 입력하세요:'))
        userTotalBalence += userwithdrawal
        return userTotalBalence

def DepWithInfos(self):  
    print(f'전체입출금 내역: {userTotalBalence}')

def manageAccount(self):
    userSelectedNumber = int(input('1. 계좌 추가(구현가능?), 2. 계좌 삭제, 99. 종료'))  
    if userSelectedNumber == 1:
        input('계좌 번호를 입력:')
        append()  
        


