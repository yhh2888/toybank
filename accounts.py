# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 

# 계좌별로 들어가서 입출금 내역을 확인하는게 좋겠다


import time


class Account:
   
    def __init__(self, id):

        self.userid = id

        self.userAccountDict = {
            id:{}
        }

    def registUserAccount(self): 

        Flag = True

        while Flag:

            accountNum = int(input('개설할 계좌번호를 입력하세요.'))

            if accountNum in self.userAccountDict[self.userid]: 
                  
                print('이미 누군가 사용하고 있는 계좌번호입니다.')

                continue

            else: 
                Flag = True    

            Flag = True

            while Flag:
            
                selectedNum = int(input('계좌가 신설되었습니다. 입금하시겠습니까? 1.입금, 99.종료 : '))
                print(70*'-')

                if selectedNum == 99:

                    userBalance = 0
                    depositFlow = []     
                    print('종료합니다.')
                    print(70*'-')
                    Flag = False
                    
                elif selectedNum == 1:

                    userBalance = int(input('입금액: '))

                    depositTime = time.strftime('%Y-%m-%d %H:%M')
                    depositFlow = [{userBalance : depositTime}]
                        
                    print('새로운 계좌가 탄생했네요! 축하드립니다.')
                    print(70*'-')
                    Flag = False
        
                else:
                    print("오타입니다. 다시 적어주세요!")
                    print(70*'-')

        self.userAccountDict[self.userid][accountNum] = {                                                                      
                'balance': userBalance,
                'depositFlow': depositFlow,
                'withdrawalFlow': []
        }
               
    def viewAccount(self):  

        currentUserAccounts = self.userAccountDict[self.userid]

        for acc, accinfo in currentUserAccounts.items():

            balance = accinfo['balance']
            deposit =  accinfo['depositFlow']
            withdrawal = accinfo['withdrawalFlow']

            print(70*'-')    
            print(f'계좌번호: {acc}, 잔액: {balance}원, \n 예금 현황: {deposit}, \n 출금 현황: {withdrawal}')
            
    def sendMoney(self):
                
        depositaccountNum = int(input('입금할 계좌번호를 입력하세요: '))
        print(70*'-')

        if  depositaccountNum in self.userAccountDict[self.userid]:

            userAddDeposit = int(input('입금액을 입력하세요(단, 천만원 이하): '))
            print(70*'-')

            if userAddDeposit > 10000000:
                print('입금 한도를 초과했습니다.')
                return
                
            elif userAddDeposit < 0 :
                return
                    
            else:
                passedDeposit = userAddDeposit 
                     
                self.userAccountDict[self.userid][depositaccountNum]['balance'] += passedDeposit 

                depositTime = time.strftime('%Y-%m-%d %H:%M')

                self.userAccountDict[self.userid][depositaccountNum]['depositFlow'].append({passedDeposit:depositTime})
        else: 
            print('계좌번호가 맞지 않습니다. 다시 입력해주세요.')
            print(70*'-')
            return
            
    def withdrawal(self): 

        withdrawalAccountNum = int(input('출금할 계좌번호를 입력하세요: '))
        print(70*'-')

        if  withdrawalAccountNum in self.userAccountDict[self.userid]:

            print(f'현재 잔액 : {self.userAccountDict[self.userid][withdrawalAccountNum]['balance']}')

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

            if passedWithdrawal > self.userAccountDict[self.userid][withdrawalAccountNum]['balance']:
                print('잔액이 부족하여 출금이 거부되었습니다.')
                print(70*'-')
                return
            else: 
                self.userAccountDict[self.userid][withdrawalAccountNum]['balance'] -= passedWithdrawal

                withdrawalTime = time.strftime('%Y-%m-%d %H:%M')

                self.userAccountDict[self.userid][withdrawalAccountNum]['withdrawalFlow'].append({passedWithdrawal:withdrawalTime})

        else: 
            print('계좌번호를 다시 입력해주세요.')
            print(70*'-') 
 
    def modifyAccount(self):

        userSelectedNumber = int(input('1. 계좌 추가, 2. 계좌 삭제, 99. 종료 :  '))
        print(70*'-')  

        Flag = True

        while Flag:

            if userSelectedNumber == 1:
                return self.registUserAccount()

            elif userSelectedNumber == 2:

                return self.deleteAccount()

            elif userSelectedNumber == 99:

                return self.shutdownAccount()

            else: 
                print('오타입니다. 다시 입력해주세요.')            
            
    def deleteAccount(self):                

        print('계좌정보를 확인한 후 제거하고 싶은 계좌번호를 선택하세요')
        print(70*'-')

        self.viewAccount()

        wantedDelAccounted = int(input('계좌번호를 입력하세요.'))
        print(70*'-')
       
        while True:       
                
            if wantedDelAccounted in self.userAccountDict[self.userid]:

                del self.userAccountDict[self.userid][wantedDelAccounted]

                print(f'{wantedDelAccounted}가 삭제되었습니다.')
                print(70*'-')

                break

            else: 
                print('없는 계좌입니다. 다시 입력해주세요.') 
                print(70*'-')

    def shutdownAccount(self):

        print('프로그램을 종료하겠습니다. 이용해 주셔서 감사합니다.')

        print(70*'-')


user1info = Account('tjdwlsl888') 
user1info.registUserAccount()
user1info.modifyAccount()
user1info.sendMoney()   
user1info.withdrawal()  
user1info.viewAccount()
user1info.deleteAccount()
   




           


