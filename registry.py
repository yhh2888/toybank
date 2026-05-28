import json
import os

FILE_PATH = os.getcwd() + '/data.json'

def saveData(accounts):
    """[쓰기/수정/삭제] 딕셔너리 데이터를 텍스트 파일에 저장하는 함수"""
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    file = open(FILE_PATH, 'w', encoding='utf-8')
    json.dump(accounts, file, ensure_ascii=False, indent=4)
    file.close()


def loadData(accounts):
    """[조회] 텍스트 파일에서 데이터를 읽어와서 메인 딕셔너리에 동기화하는 함수"""
    if not os.path.exists(FILE_PATH):
        return
    file = open(FILE_PATH, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    accounts.clear()
    accounts.update(data)


def register(accounts):
    """회원가입 (C: 데이터 쓰기)"""
    # 항상 최신 데이터 상태에서 조회/비교하기 위해 로드 먼저 실행
    loadData(accounts)
    
    print("\n--- [회원가입] ---")
    userId = input("사용할 ID를 입력하세요: ").strip()
    
    if userId in accounts:
        print("이미 존재하는 ID입니다.")
        return

    password = input("사용할 비밀번호를 입력하세요: ").strip()
    name = input("이름을 입력하세요: ").strip()
    email = input("이메일을 입력하세요: ").strip()

    # 데이터 저장 구조 정의
    accounts[userId] = {
        "pw": password,
        "name": name,
        "email": email,
        "account_list": []
    }
    
    # 변경된 데이터 파일에 쓰기
    saveData(accounts)
    print(f"회원가입 완료! 정보가 {FILE_PATH}에 저장되었습니다.")


def login(users):
    """로그인 및 회원 관리 (R: 조회, U: 수정, D: 삭제)"""
    # 항상 최신 데이터 상태에서 로그인하기 위해 로드 먼저 실행
    loadData(users)
    
    print("\n--- [로그인] ---")
    userId = input("ID: ").strip()
    password = input("PW: ").strip()

    if userId not in users or users[userId]["pw"] != password:
        print("ID 또는 비밀번호가 일치하지 않습니다.")
        return 
    else: 
        print(f"로그인 성공! 반갑습니다, {users[userId]['name']}님.")
        return userId
    
def deleteUser(accounts):
    loadData(accounts)
    
    print("\n--- [회원 탈퇴] ---")
    userId = input("탈퇴할 ID: ").strip()
    password = input("비밀번호: ").strip()

    if userId not in accounts or accounts[userId]["pw"] != password:
        print("ID 또는 비밀번호가 일치하지 않습니다.")
        return

    del accounts[userId]
    saveData(accounts)
    print(f"회원 정보가 {FILE_PATH}에서 완전히 삭제되었습니다.")

def logout():
    print("로그아웃 되었습니다.")
    return None

def modifyUser(accounts):
    loadData(accounts)
    print("\n--- [회원 정보 수정] ---")
    userId = input("수정할 ID: ").strip()
    password = input("현재 비밀번호: ").strip()

    if userId not in accounts or accounts[userId]["pw"] != password:
        print("ID 또는 비밀번호가 일치하지 않습니다.")
        return
    
    modifyTarget = input("수정할 항목 선택 (1. 비밀번호, 2. 이름, 3. 이메일): ").strip()
    if modifyTarget not in ['1', '2', '3']:
        print("잘못된 선택입니다.")
        return
    elif modifyTarget == '1':
        newPassword = input("새 비밀번호: ").strip()
        newPasswordConfirm = input("새 비밀번호 확인: ").strip()
        if newPassword != newPasswordConfirm:
            print("비밀번호 확인이 일치하지 않습니다.")
        else:
            accounts[userId]["pw"] = newPassword
    elif modifyTarget == '2':
        newName = input("새 이름: ").strip()
        newNameConfirm = input("새 이름 확인: ").strip()
        if newName != newNameConfirm:
            print("이름 확인이 일치하지 않습니다.")
        elif len(newName) < 2:
            print("이름은 최소 2자 이상이어야 합니다.") 
        else:
            accounts[userId]["name"] = newName
    
    elif modifyTarget == '3':
        newEmail = input("새 이메일: ").strip()
        newEmailConfirm = input("새 이메일 확인: ").strip()
        if newEmail != newEmailConfirm:
            print("이메일 확인이 일치하지 않습니다.")
        elif "@" not in newEmail or "." not in newEmail:
            print("유효한 이메일 형식이 아닙니다.")
        else:
            accounts[userId]["email"] = newEmail
    
    saveData(accounts)
    print("회원 정보가 수정되었습니다.")

    if newPassword:
        accounts[userId]["pw"] = newPassword
    if newName:
        accounts[userId]["name"] = newName