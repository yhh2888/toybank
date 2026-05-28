TODO_WRITE  = 1
TODO_READ   = 2
TODO_UPDATE = 3
TODO_DELETE = 4
TODO_STATUS = 5
TODO_END    = 0

import time

class TodoManager:
    def __init__(self):
        self.filePath = 'C:/lge/ToyBank/toybank/todolist.txt', 'a'
  
    def gotDay(self):
        return time.strftime('%Y년%m월%d일')
    
    def getTime(self):
        return time.strftime('%H:%M')
   
    def add_new_todo(self):
        userInput = input('입력: ')
        with open('C:/lge/ToyBank/toybank/todolist.txt', 'a') as file:
            file.write(f'[{self.gotDay()}|{self.getTime()}] [미완료] {userInput}\n')

            return userInput
        
    def ask_next_step(self):
        while True:
            choice = int(input('1. 일정 추가 등록    2.  처음으로'))
            if choice == 1:
                print('추가 등록할 일정을 추가해주세요.')
                self.add_new_todo()

            elif choice == 2:
                print('처음으로 돌아갑니다.')
                return

            else:
                print('번호를 잘못 입력했습니다. 다시 입력 해주세요.')
    
    def showTodoIist(self):
        todoIist = []
        file = open('C:/lge/ToyBank/toybank/todolist.txt', 'r')
        readResult =  file.read()
        todoIist = readResult.splitlines()
        isRunning = True
        while isRunning:
            for i, todo in enumerate(todoIist, start=1):
                print(f'{i}. {todo}')

            editOrDelete = int(input('3.일지 수정   4.일지 삭제  5.일지 완료 체크  0.처음메뉴로'))

            if editOrDelete == TODO_UPDATE:
                targetNumber = int(input('수정할 일정의 번호 입력해주세요: '))
                print('수정할 내용을 입력해주세요')
                newContent = input('입력:')
                todoIist[targetNumber - 1] = f'[{self.gotDay()}|{self.getTime()}] {newContent}'

                with open('C:/lge/ToyBank/toybank/todolist.txt', 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')

            elif editOrDelete == TODO_DELETE:
                targetNumber = int(input('삭제할 일지 번호 입력해주세요: '))
                del todoIist[targetNumber - 1]
                print('삭제완료되었습니다.')

                with open('C:/lge/ToyBank/toybank/todolist.txt', 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')


            elif editOrDelete == TODO_STATUS:
                targetNumber = int(input('완료할 일정의 번호 입력해주세요: '))
                todoIist[targetNumber - 1] = todoIist[targetNumber - 1].replace('[미완료]', '[완료]')
                with open('C:/lge/ToyBank/toybank/todolist.txt', 'w') as file:
                    for todo in todoIist:
                        file.write(f'{todo}\n')


            elif editOrDelete == TODO_END:
                print('다시 돌아갑니다.')
                isRunning = False

            else:
                print('입력 번호를 다시 확인해주세요.')