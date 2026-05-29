# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 

# 계좌별로 들어가서 입출금 내역을 확인하는게 좋겠다

import time
import os

class Account:
    def __init__(self):
        self.userAccountDict = {}

    def viewAccount(self, accounts, userId):  
        currentUserAccounts = self.userAccountDict[userId]

        for acc, accinfo in currentUserAccounts.items():
            balance = accinfo['balance']
            
            def format_flow(flow):
                if not flow: return "내역 없음"
                # 불필요한 텍스트 및 기호 제거 ('예금 내역 :', 대괄호, 따옴표 등)
                clean = flow.replace('예금 내역 : ', '').replace('출금 내역 : ', '')
                clean = clean.replace('[', '').replace(']', '').replace("'", "").replace('[]', '').strip()
                if not clean: return "내역 없음"
                
                # 구분자('|')를 기준으로 나누어 각 내역을 새 줄에 표시하도록 포맷팅
                # (기존 공백 구분 데이터와의 호환성을 위해 strip 처리 추가)
                records = [r.strip() for r in clean.split('|') if r.strip()]
                return "\n " + "\n ".join(records)

            deposit = format_flow(accinfo['depositFlow'])
            withdrawal = format_flow(accinfo['withdrawalFlow'])

            print(70*'-')    
            print(f'계좌번호: {acc} | 잔액: {balance}원')
            print(f' - 예금 현황: {deposit}')
            print(f' - 출금 현황: {withdrawal}')
            
    def sendMoney(self, accounts, userId):
        depositFromAccountNum = int(input('출금할 계좌번호를 입력하세요: '))
        print(70*'-')

        depositToAccountNum = int(input('입금할 계좌번호를 입력하세요: '))
        print(70*'-')
        if  depositToAccountNum in self.userAccountDict[userId]:
            userAddDeposit = int(input('입금액을 입력하세요(단, 천만원 이하): '))
            print(70*'-')

            if userAddDeposit > 10000000:
                print('입금 한도를 초과했습니다.')
                return
            elif userAddDeposit < 0 :
                return 
            else:
                if userAddDeposit > self.userAccountDict[userId][depositFromAccountNum]["balance"]:
                    print('잔액이 부족하여 송금이 거부되었습니다.')
                    print(70*'-')
                    return
                else:
                    depositTime = time.strftime('%Y-%m-%d %H:%M')
                    new_record = f"{userAddDeposit}원({depositTime})"
                    
                    # 출금 계좌 업데이트
                    self.userAccountDict[userId][depositFromAccountNum]['balance'] -= userAddDeposit
                    w_flow = self.userAccountDict[userId][depositFromAccountNum]['withdrawalFlow']
                    w_flow = "" if w_flow in ["출금 내역 : ", "[]", ""] else w_flow
                    self.userAccountDict[userId][depositFromAccountNum]['withdrawalFlow'] = (w_flow + " | " + new_record if w_flow else new_record)
                    
                    # 입금 계좌 업데이트
                    self.userAccountDict[userId][depositToAccountNum]['balance'] += userAddDeposit
                    d_flow = self.userAccountDict[userId][depositToAccountNum]['depositFlow']
                    d_flow = "" if d_flow in ["예금 내역 : ", "[]", ""] else d_flow
                    self.userAccountDict[userId][depositToAccountNum]['depositFlow'] = (d_flow + " | " + new_record if d_flow else new_record)
                    print(f'{userAddDeposit}원이 성공적으로 송금되었습니다.')
        else: 
            print('계좌번호가 맞지 않습니다. 다시 입력해주세요.')
            print(70*'-')
            return
            
    def withdrawal(self, accounts, userId): 
        withdrawalAccountNum = int(input('출금할 계좌번호를 입력하세요: '))
        print(70*'-')
        if  withdrawalAccountNum in self.userAccountDict[userId]:
            print(f'현재 잔액 : {self.userAccountDict[userId][withdrawalAccountNum]["balance"]}')
            userAddWithdrawal = int(input('출금액을 입력하세요(단 100만원 이하):'))
            print(70*'-')
                
            if userAddWithdrawal > 1000000:
                print('출금 한도를 초과했습니다.')
                print(70*'-')
                return
                
            elif userAddWithdrawal <= 0 :
                print('0보다 작거나 같은 돈을 출금할 수는 없습니다.')
                print(70*'-')
                return
                
            passedWithdrawal = userAddWithdrawal

            if passedWithdrawal > self.userAccountDict[userId][withdrawalAccountNum]["balance"]:
                print('잔액이 부족하여 출금이 거부되었습니다.')
                print(70*'-')
                return
            else: 
                self.userAccountDict[userId][withdrawalAccountNum]['balance'] -= passedWithdrawal
                withdrawalTime = time.strftime('%Y-%m-%d %H:%M')
                new_record = f"{passedWithdrawal}원({withdrawalTime})"
                w_flow = self.userAccountDict[userId][withdrawalAccountNum]['withdrawalFlow']
                w_flow = "" if w_flow in ["출금 내역 : ", "[]", ""] else w_flow
                self.userAccountDict[userId][withdrawalAccountNum]['withdrawalFlow'] = (w_flow + " | " + new_record if w_flow else new_record)
        else: 
            print('계좌번호를 다시 입력해주세요.')
            print(70*'-') 
 
    def modifyAccount(self, accounts, userId):
        userAccountNumber = int(input('변경할 계좌의 번호를 입력하세요 : '))
        print(70*'-')
        if userAccountNumber in self.userAccountDict[userId]:    
            newAccountNumber = int(input('새로운 계좌번호를 입력하세요 : '))
            print(70*'-')
            if newAccountNumber in self.userAccountDict[userId]: 
                print('이미 누군가 사용하고 있는 계좌번호입니다.')
                print(70*'-')
            else: 
                self.userAccountDict[userId][newAccountNumber] = self.userAccountDict[userId].pop(userAccountNumber)
                print('계좌번호가 변경되었습니다.')
                print(70*'-')

    def addAccount(self, accounts, userId):
        userAccountInitNum = int(input('추가할 계좌의 계좌번호를 입력하세요. : '))
        print(70*'-')
        if userAccountInitNum in self.userAccountDict[userId]:
            print('이미 누군가 사용하고 있는 계좌번호입니다.')
            print(70*'-')
        else:
            self.userAccountDict[userId][userAccountInitNum] = {
                'balance': 0,
                'depositFlow': '',
                'withdrawalFlow': ''
            }
            print(70*'-')
            print(f'{userAccountInitNum} 계좌가 추가되었습니다.')
            print(70*'-')
            
    def deleteAccount(self, accounts, userId):                
        while True: 
            print('계좌정보를 확인한 후 제거하고 싶은 계좌번호를 선택하세요')
            print(70*'-')
            self.viewAccount(accounts, userId)
            wantedDelAccounted = int(input('계좌번호를 입력하세요.'))
            print(70*'-')

            if wantedDelAccounted in self.userAccountDict[userId]:
                del self.userAccountDict[userId][wantedDelAccounted]
                print(f'{wantedDelAccounted}가 삭제되었습니다.')
                print(70*'-')
                break

            else: 
                print('없는 계좌입니다. 다시 입력해주세요.') 
                print(70*'-')

    def saveAccounts(self, accounts):
        with open(os.getcwd() + '/accounts.txt', 'w', encoding='utf-8') as file:
            for userId, userAccounts in accounts.userAccountDict.items():
                for accNum, accInfo in userAccounts.items():
                    balance = accInfo['balance']
                    depositFlow = accInfo['depositFlow']
                    withdrawalFlow = accInfo['withdrawalFlow']
                    file.write(f'{userId},{accNum},{balance},{depositFlow},{withdrawalFlow}\n')
        
    def loadAccounts(self, accounts):
        try: # 'cp949' codec can't decode byte 0xec in position 22: illegal multibyte sequence 오류 해결을 위해 encoding='utf-8' 추가
            with open(os.getcwd() + '/accounts.txt', 'r', encoding='utf-8') as file:
                 for line in file:
                    line = line.strip()
                    if not line: # 파일 끝의 빈 줄이나 공백만 있는 줄은 건너뜁니다.
                        continue
                    userId, accNum, balance, depositFlow, withdrawalFlow = line.split(',')
                    accNum = int(accNum)
                    balance = int(balance)
                    depositFlow = str(depositFlow)
                    withdrawalFlow = str(withdrawalFlow)

                    if userId not in accounts.userAccountDict:
                        accounts.userAccountDict[userId] = {}
                    accounts.userAccountDict[userId][accNum] = {
                        'balance': balance,
                        'depositFlow': depositFlow,
                        'withdrawalFlow': withdrawalFlow
                    }
        except FileNotFoundError:
            print('저장된 계좌 정보가 없습니다.')

if __name__ == "__main__":
    user1info = Account() 
    user1info.registUserAccount()
    user1info.addAccount()
    user1info.sendMoney()   
    user1info.withdrawal()  
    user1info.viewAccount()
    user1info.deleteAccount()
   




           
