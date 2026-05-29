# my dashboard service
# 복잡한 데이터와 핵심지표를 시각화하여 한눈에 파악
# 중앙집중식 인터페이스?

'''
toy project
my dashboard service
- member service
- signup, signin, signout, modify, delete
- bank account
 - 회원 1인당 1개의 계좌만 관리
 - 회원 1인당 n개의 계좌 관리
 - 입/출금 내역
- memo
 - write, read, update, delete
- todo list
 - write, read, update, delete
 - expired date

- 시나리오 정립
- 업무분장
- 프로젝트 생성 및 저장소
- 각각의 개발자가 개발 시작
'''

# --------------------------------------------------------------------
import registry
import addOn
import todolistnumber
import accounts

# import accounts

class UserSystem:
    def __init__(self):
        self.users = {
            "administrator": "1234",
            "userexample": "p@ssword"
        }
        registry.loadData(self.users)
        self.currentUser = None
        self.accounts = {}
        self.memos = {}
        self.todos = {}
        self.todolists = todolistnumber.TodoManager()
        self.accounts = accounts.Account()
        for users in self.users.keys():
            if users not in self.accounts.userAccountDict:
                self.accounts.userAccountDict[users] = {}
        self.accounts.loadAccounts(self.accounts)

    def register(self):
        registry.register(self.users)
        # registry.py의 register 함수를 호출하여 회원가입을 처리합니다. accounts 딕셔너리를 전달하여 새로운 계좌 정보를 저장할 수 있도록 합니다.
        registry.loadData(self.users)

    def login(self):
        userId = registry.login(self.users)
        return userId
        # registry.py의 login 함수를 호출하여 로그인 처리를 합니다.

    def mainMenu(self):
        while True:
            if self.currentUser:
                userSelectedNumber = input('3. 회원탈퇴   4. 회원정보 수정   5. 로그아웃   ' \
                                        '6. 계좌 메뉴   7. 투두 리스트 메뉴   8. 시계 표시   99. 종료 : ')
            else:
                userSelectedNumber = input('1. 로그인   2. 회원가입   ' \
                                        '8. 시계 표시   99. 종료 : ')
            
            if isinstance(userSelectedNumber, str) and userSelectedNumber.isdigit():
                userSelectedNumber = int(userSelectedNumber)
            else:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

            if userSelectedNumber == 1 and not self.currentUser:
                userId = self.login()
                self.currentUser = userId
            elif userSelectedNumber == 2 and not self.currentUser:
                self.register()
            elif userSelectedNumber == 3 and self.currentUser:
                self.deleteUser()
            elif userSelectedNumber == 4 and self.currentUser:
                self.modifyUser()
            elif userSelectedNumber == 5 and self.currentUser:
                self.logout()
            elif userSelectedNumber == 6 and self.currentUser:
                self.accountsMenu()
            elif userSelectedNumber == 7 and self.currentUser:
                self.todoMenu()
            elif userSelectedNumber == 8:
                self.clock()
            elif userSelectedNumber == 99:
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")

    def accountsMenu(self):
        while True:
            userSelectedNumber = int(input('1. 계좌 추가, 2. 계좌 삭제, 3. 계좌 조회, 4. 송금하기, 99. 처음으로 돌아가기 : '))
            print(70*'-')
            if userSelectedNumber == 1:
                self.addAccount()
            elif userSelectedNumber == 2:
                self.deleteAccount()
            elif userSelectedNumber == 3:
                self.viewAccount()
            elif userSelectedNumber == 4:
                self.sendMoney()
            elif userSelectedNumber == 99:
                print('종료하겠습니다.')
                print(70*'-')
                break

    def addAccount(self):
        self.accounts.addAccount(self.accounts, self.currentUser)
        self.accounts.saveAccounts(self.accounts)

    def modifyAccount(self):
         self.accounts.modifyAccount(self.accounts, self.currentUser)
         self.accounts.saveAccounts(self.accounts)
         # accounts.py의 modifyAccount 함수를 호출하여 계좌 정보를 수정합니다. accounts 딕셔너리를 전달하여 계좌 정보를 업데이트할 수 있도록 합니다.

    def deleteAccount(self):
        self.accounts.deleteAccount(self.accounts, self.currentUser)
        self.accounts.saveAccounts(self.accounts)
        # accounts.py의 deleteAccount 함수를 호출하여 계좌를 삭제합니다. accounts

    def viewAccount(self):
        self.accounts.viewAccount(self.accounts, self.currentUser)
        self.accounts.saveAccounts(self.accounts)
        # accounts.py의 viewAccount 함수를 호출하여 계좌 정보를 조회합니다. accounts

    def sendMoney(self):
        self.accounts.sendMoney(self.accounts, self.currentUser)
        self.accounts.saveAccounts(self.accounts)
        # accounts.py의 sendMoney 함수를 호출하여 송금 기능을 처리합니다. accounts 딕셔너리를 전달하여 송금 기능을 구현할 수 있도록 합니다. 

    def deleteUser(self):
        registry.deleteUser(self.users)
        # accounts.py의 deleteUser 함수를 호출하여 회원을 삭제합니다. accounts 딕셔너리를 전달하여 회원 정보를 삭제할 수 있도록 합니다.

    def modifyUser(self):
        registry.modifyUser(self.users)
        # accounts.py의 modifyUser 함수를 호출하여 회원 정보를 수정합니다. accounts 딕셔너리를 전달하여 회원 정보를 업데이트할 수 있도록 합니다.

    def logout(self):
        self.currentUser = registry.logout()
        # registry.py의 logout 함수를 호출하여 로그아웃 처리를 합니다.

    def todoMenu(self):
        while True:
            todoNumber = int(input('1. 일정 작성하기    2. 일정 수정하기    3. 처음으로 돌아가기 : '))
            if todoNumber == 1:
                self.todolists.askNextStep()
            elif todoNumber == 2:
                self.todolists.showTodoList()
            elif todoNumber == 3:
                print('처음으로 돌아갑니다.')
                break
            else:
                print('잘못된 입력입니다. 다시 입력해주세요.')

        # todolistnumber.py의 todoMenu 함수를 호출하여 투두 리스트 메뉴를 처리합니다. accounts 딕셔너리와 todos 딕셔너리를 전달하여 투두 리스트 기능을 구현할 수 있도록 합니다.

    def clock(self):
        print(f"\n {self.todolists.gotDay()} | {self.todolists.getTime()} \n")
        # addOn.py의 clock 함수를 호출하여 시계를 표시합니다.


if __name__ == "__main__":
    userSystem = UserSystem()
    userSystem.mainMenu()