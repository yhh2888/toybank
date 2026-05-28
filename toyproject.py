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
import accounts

def tempFunction():
    print(f'tempFunction() CALLED!!')

class UserSystem:
    def __init__(self):
        self.users = {
            "administrator": "1234",
            "userexample": "p@ssword"
        }
        self.currentUser = None
        self.accounts = {}
        self.memos = {}
        self.todos = {}
    
    def register(self):
        registry.register(self.accounts)
        # registry.py의 register 함수를 호출하여 회원가입을 처리합니다. accounts 딕셔너리를 전달하여 새로운 계좌 정보를 저장할 수 있도록 합니다.

    def login(self):
        registry.login(self.users)
        # registry.py의 login 함수를 호출하여 로그인 처리를 합니다.

    def mainMenu(self):
        registry.mainMenu()
        # registry.py의 mainMenu 함수를 호출하여 메인 메뉴를 처리합니다.

    def modifyAccount(self):
        accounts.modifyAccount(self.accounts)
        # accounts.py의 modifyAccount 함수를 호출하여 계좌 정보를 수정합니다. accounts 딕셔너리를 전달하여 계좌 정보를 업데이트할 수 있도록 합니다.

    def deleteAccount(self):
        accounts.deleteAccount(self.accounts)
        # accounts.py의 deleteAccount 함수를 호출하여 계좌를 삭제합니다. accounts

    def viewAccount(self):
        accounts.viewAccount(self.accounts)
        # accounts.py의 viewAccount 함수를 호출하여 계좌 정보를 조회합니다. accounts

    def sendMoney(self):
        accounts.sendMoney(self.accounts)
        # accounts.py의 sendMoney 함수를 호출하여 송금 기능을 처리합니다. accounts 딕셔너리를 전달하여 송금 기능을 구현할 수 있도록 합니다.

    def deleteUser(self):
        accounts.deleteUser(self.accounts)
        # accounts.py의 deleteUser 함수를 호출하여 회원을 삭제합니다. accounts 딕셔너리를 전달하여 회원 정보를 삭제할 수 있도록 합니다.

    def modifyUser(self):
        pass

    def logout(self):
        pass

    def memoMenu(self):
        pass

    def todoMenu(self):
        addOn.todoMenu(self.accounts, self.todos)
        # addOn.py의 todoMenu 함수를 호출하여 투두 리스트 메뉴를 처리합니다. accounts 딕셔너리와 todos 딕셔너리를 전달하여 투두 리스트 기능을 구현할 수 있도록 합니다.

    def clock(self):
        pass

    def save(self):
        pass

    def load(self):
        pass



