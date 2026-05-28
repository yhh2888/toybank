# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 


class Account:
   
    def __init__(self, id, account, balance):

        self.userid = id
        self.account = account
        self.balance = balance  
        self.userAccountDict = {}   

    def userAccountInfos(self): 

        self.account = int(input('계좌 번호를 입력하세요.'))
        self.balance = input('잔액을 입력하세요.')
    
        self.userAccountDict[self.userid] = {  
            'userid': self.userid,                                             
            'account': self.account,                         
            'balance': self.balance,
        }

        print('새로운 계좌가 탄생했네요!')

    def viewAccount(self):  

        print(f'전체입출금 내역: {self.userAccountDict[self.userid]}')

        return self.userAccountDict[self.userid]
            
    def sendMoney(self):
                
        depositaccountNum = int(input('입금할 계좌번호를 입력하세요: '))

        if  depositaccountNum in self.userAccountDict[self.userid]:

            userAddDeposit = int(input('입금액을 입력하세요(단, 천만원 이하): '))

            if userAddDeposit > 10000000:
                return
                
            elif userAddDeposit < 0 :
                return
                    
            else:
                passedDeposit = userAddDeposit 
                     
                self.userAccountDict[self.userid][depositaccountNum] += passedDeposit
        else: 
            print('계좌번호가 맞지 않습니다. 다시 입력해주세요.')
            return
            
    def withdrawal(self): 

        withdrawalAccountNum = int(input('출금할 계좌번호를 입력하세요: '))

        if  withdrawalAccountNum in self.userAccountDict[self.userid]:

            userAddWithdrawal = int(input('출금액을 입력하세요(단 100만원 이하):'))
                
            if userAddWithdrawal > 1000000:
                return
                
            elif userAddWithdrawal < 0 :
                return
                
            else: 
                passedWithdrawal = userAddWithdrawal  

            self.userAccountDict[self.userid][withdrawalAccountNum] += passedWithdrawal
        else: 
            print('계좌번호를 다시 입력해주세요.')

            return  
 
    def modifyAccount(self):

        userSelectedNumber = int(input('1. 계좌 추가, 2. 계좌 삭제, 99. 종료'))  

        return userSelectedNumber       

    def addAccount(self):

        userChoiceNum = self.modifyAccount(self) 
    
        if userChoiceNum == 1:

                additionalAccount = int(input('추가하고 싶은 계좌 번호를 입력하세요.'))

                if additionalAccount != self.userAccountDict[self.userid]:

                    self.userAccountDict[self.userid] = additionalAccount 

                    print(f"{additionalAccount} 계좌가 추가되었습니다")

                else:
                    print('이미 존재하는 계좌입니다. 다시 입력해주세요.')

    def deleteAccount(self):                

        userChoiceNum = self.modifyAccount(self)             

        if userChoiceNum == 2:

                print('계좌정보를 확인한 후 제거하고 싶은 계좌번호를 선택하세요')
                    
                self.viewAccount(self)

                wantedDelAccounted = int(input('계좌번호를 입력하세요.'))

                if wantedDelAccounted == self.userAccountDict[self.userid]:

                    del self.userAccountDict[wantedDelAccounted]

                    print(f'{wantedDelAccounted}가 삭제되었습니다.')

                else: 
                    print('없는 계좌입니다. 다시 입력해주세요.') 

    def shutdownAccount(self):

        userChoiceNum = self.modifyAccount(self)    
                
        if userChoiceNum == 99:
            print('종료하겠습니다.')
            return
                
        else: 
            print('잘못 적었습니다. 다시 입력해주세요.')

                
user1info = Account('tjdwlsl888', 12345678, 10000) 




           


