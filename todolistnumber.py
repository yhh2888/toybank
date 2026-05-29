TODO_WRITE  = 1
TODO_READ   = 2
TODO_UPDATE = 3
TODO_DELETE = 4
TODO_STATUS = 5
TODO_END    = 0

import time
import os

class TodoManager:
    def __init__(self):
        self.filePath = os.getcwd() + '/todolist.txt'
  
    def gotDay(self):
        return time.strftime('%Y년%m월%d일')
    
    def getTime(self):
        return time.strftime('%H시%M분')
   
    def addNewTodo(self):
        userInput = input('일정 입력: ')
        while True:
            deadline = input('마감일을 입력하세요: ')
            if len(deadline) == 8:
                deadline = f'{deadline[:4]}-{deadline[4:6]}-{deadline[6:]}'
                break
            else:
                print('잘못입력하셨습니다. 다시 입력해주세요.')

        with open(self.filePath, 'a') as file:
            file.write(f'[{self.gotDay()}|{self.getTime()}] [미완료] 마감일[{deadline}] {userInput}\n')
            print(f'{userInput}등록이 완료 되었습니다.')
            return userInput
                
    def askNextStep(self):
        while True:
            choice = int(input('1. 일정 추가 등록    2.  처음으로'))
            if choice == 1:
                print('추가 등록할 일정을 추가해주세요.')
                self.addNewTodo()

            elif choice == 2:
                print('처음으로 돌아갑니다.')
                return

            else:
                print('번호를 잘못 입력했습니다. 다시 입력 해주세요.')
    
    def showTodoIist(self):
        todoIist = []
        file = open(self.filePath,'r')
        readResult =  file.read()
        todoIist = readResult.splitlines()
        isRunning = True
        while isRunning:
            for i, todo in enumerate(todoIist, start=1):
                if todo[:10] < self.gotDay():
                    continue
                print(f'{i}. {todo}')
            editOrDelete = int(input('3.일지 수정   4.일지 삭제  5.일지 완료 체크  0.처음메뉴로'))

            if editOrDelete == TODO_UPDATE:
                targetNumber = int(input('수정할 일정의 번호 입력해주세요: '))
                print('수정할 내용을 입력해주세요')
                newContent = input('입력:')
                todoIist[targetNumber - 1] = f'[{self.gotDay()}|{self.getTime()}] {newContent}'

                with open(self.filePath, 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')

            elif editOrDelete == TODO_DELETE:
                targetNumber = int(input('삭제할 일지 번호 입력해주세요: '))
                del todoIist[targetNumber - 1]
                print('삭제완료되었습니다.')

                with open(self.filePath, 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')


            elif editOrDelete == TODO_STATUS:
                targetNumber = int(input('완료할 일정의 번호 입력해주세요: '))
                todoIist[targetNumber - 1] = todoIist[targetNumber - 1].replace('[미완료]', '[완료]')
                with open(self.filePath, 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')


            elif editOrDelete == TODO_END:
                print('다시 돌아갑니다.')
                isRunning = False

            else:
                print('입력 번호를 다시 확인해주세요.')
