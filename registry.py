import json
import os

# 📂 요청하신 경로로 파일 저장 위치를 변경했습니다.
# 뒤에 실제 파일명과 확장자(예: data.txt)를 붙여주어야 정상적으로 파일이 생성됩니다.
FILE_PATH = 'C:/nggm/python_prct/project0528ex/toybank/data.txt'

def save_data(accounts):
    """[쓰기/수정/삭제] 딕셔너리 데이터를 텍스트 파일에 저장하는 함수"""
    # 폴더가 존재하지 않으면 자동으로 경로를 끝까지 다 생성해줍니다.
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    # 1. 파일을 쓰기('w') 모드로 open
    file = open(FILE_PATH, 'w', encoding='utf-8')
    # 2. 딕셔너리를 문자열(JSON)로 변환하여 파일에 쓰기
    json.dump(accounts, file, ensure_ascii=False, indent=4)
    # 3. 파일 닫기
    file.close()


def load_data(accounts):
    """[조회] 텍스트 파일에서 데이터를 읽어와서 메인 딕셔너리에 동기화하는 함수"""
    if not os.path.exists(FILE_PATH):
        return  # 파일이 아직 없으면 무시하고 리턴

    # 1. 파일을 읽기('r') 모드로 open
    file = open(FILE_PATH, 'r', encoding='utf-8')
    # 2. 파일 안의 글자를 다시 딕셔너리로 읽어오기
    data = json.load(file)
    file.close()
    
    # 3. 메인 프로그램의 accounts 딕셔너리에 데이터 채우기
    accounts.clear()
    accounts.update(data)


def register(accounts):
    """회원가입 (C: 데이터 쓰기)"""
    # 항상 최신 데이터 상태에서 조회/비교하기 위해 로드 먼저 실행
    load_data(accounts)
    
    print("\n--- [회원가입] ---")
    user_id = input("사용할 ID를 입력하세요: ").strip()
    
    if user_id in accounts:
        print("❌ 이미 존재하는 ID입니다.")
        return

    password = input("사용할 비밀번호를 입력하세요: ").strip()
    name = input("이름을 입력하세요: ").strip()
    email = input("이메일을 입력하세요: ").strip()

    # 데이터 저장 구조 정의
    accounts[user_id] = {
        "pw": password,
        "name": name,
        "email": email,
        "account_list": []
    }
    
    # 변경된 데이터 파일에 쓰기
    save_data(accounts)
    print(f"🎉 회원가입 완료! 정보가 {FILE_PATH}에 저장되었습니다.")


def login(users):
    """로그인 및 회원 관리 (R: 조회, U: 수정, D: 삭제)"""
    # 항상 최신 데이터 상태에서 로그인하기 위해 로드 먼저 실행
    load_data(users)
    
    print("\n--- [로그인] ---")
    user_id = input("ID: ").strip()
    password = input("PW: ").strip()

    if user_id not in users or users[user_id]["pw"] != password:
        print("❌ ID 또는 비밀번호가 일치하지 않습니다.")
        return

    print(f"✅ 로그인 성공! 반갑습니다, {users[user_id]['name']}님.")
    
    while True:
        print(f"\n================ [로그인 상태: {user_id}] ================")
        print(" 1. 정보 수정 | 2. 회원 탈퇴(삭제) | 3. 로그아웃")
        print("=========================================================")
        choice = input("메뉴 선택: ").strip()

        # [회원 정보 수정 (Update)]
        if choice == '1':
            print("\n--- [회원 정보 수정] ---")
            cpw = input("보안을 위해 현재 비밀번호를 입력하세요: ").strip()
            if users[user_id]["pw"] != cpw:
                print("❌ 비밀번호가 일치하지 않습니다.")
                continue

            print("\n새로운 정보를 입력하세요 (변경하지 않으려면 엔터)")
            npw = input("새 비밀번호: ").strip()
            nname = input("새 이름: ").strip()
            nemail = input("새 이메일: ").strip()

            if npw:   users[user_id]["pw"] = npw
            if nname: users[user_id]["name"] = nname
            if nemail: users[user_id]["email"] = nemail
            
            # 수정 후 파일 덮어쓰기
            save_data(users)
            print("✨ 회원 정보가 수정되어 파일에 갱신되었습니다!")

        # [회원 탈퇴 / 삭제 (Delete)]
        elif choice == '2':
            print("\n--- [회원 탈퇴] ---")
            cpw = input("보안을 위해 현재 비밀번호를 입력하세요: ").strip()
            if users[user_id]["pw"] != cpw:
                print("❌ 비밀번호가 일치하지 않습니다.")
                continue

            print("\n⚠️ [현재 저장된 회원 정보] ⚠️")
            print(f"- 아이디: {user_id}")
            print(f"- 이 름: {users[user_id]['name']}")
            print(f"- 이메일: {users[user_id]['email']}")
            print("-" * 30)
            
            final_check = input("❗ 정말로 이 정보를 모두 삭제하고 탈퇴하시겠습니까? (yes/no): ").strip().lower()
            if final_check == 'yes':
                del users[user_id]  # 데이터 삭제
                
                # 삭제 후 파일 덮어쓰기
                save_data(users)
                print("👋 회원 정보가 파일에서 완전히 삭제되었습니다.")
                break
            else:
                print("🛡️ 탈퇴가 취소되었습니다.")

        elif choice == '3':
            print("로그아웃 되었습니다.")
            break
        else:
            print("잘못된 입력입니다.")