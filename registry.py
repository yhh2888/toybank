from dumy import *
import os
import json

# 📂 요청하신 경로로 파일 저장 위치를 변경했습니다.
# 뒤에 실제 파일명과 확장자(예: data.txt)를 붙여주어야 정상적으로 파일이 생성됩니다.

class MemberService:
    def __init__(self):
        self.FILE_PATH = os.getcwd() + '\\data.txt'
        
        def signIn(self): # 로그인
            sign = True
            while sign:
               menuChoice = int(input('1. 로그인    2.로그아웃    3.회원탈퇴'))
               if menuChoice == 1:
                        uId = input('아이디:')
                        uPw = input('비밀번호:')
                        if uId in userdumy:
                            if uPw == userdumy[uId]['pw']:
                                print('로그인성공!')
                                signInedMemberId = uId
                                print(f'{signInedMemberId}님 어서오세요!')
                        else:
                            print('아이디를 다시 확인해주세요.')

               elif menuChoice == 2:
                    signInedMemberId = ''
                    print('로그아웃이 정상적으로 되었습니다.')

               elif menuChoice == 3:
                    currentSignInedMemberID = signInedMemberId
                    del userdumy[currentSignInedMemberID]

                    print('Member info deleted!!')
                    signInedMemberId = ''

               else:
                   print('번호를 잘못 입력했습니다 다시 확인해주세요.')
                    

        def createAccount(self): # 회원가입
            userId = input('아이디를 입력하세요: ')
            userPw = input('비밀번호를 입력하세요: ')
            userEmail = input('이메일를 입력하세요: ')
            userPhone = input('전화번호를 입력하세요: ')

            userdumy[userId] = {
                'id':userId,
                'pw':userPw,
                'email':userEmail,
                'phone':userPhone
            }

            with open(self.filePath, 'w', encoding='utf-8') as file:
                json.dump()
                print(f'{userdumy[id]}님! 회원가입을 축하드립니다.')

            return userdumy
        
        def run(self):
            userInputData = int(input('1. 회원가입   2.로그인'))
            member = True
            while member:
                if userInputData == 1:
                    self.createAccount()

                elif userInputData == 2:
                    self.signIn()

                else:
                    print('번호를 잘못 입력했습니다. 다시 입력해주세요.')