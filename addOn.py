from todolistnumber import *

todo = True
manager =TodoManager()

while todo:
    print('------원하는 메뉴를 선택하세요.-------')
    listSelection = int(input('1.일정 등록    2. 일정조회    0.종료'))

    if listSelection == TODO_WRITE:
        print('----등록할 일정을 적어주세요----.')
        todoContent = manager.add_new_todo()
        print(f'[{manager.gotDay()}|{manager.getTime()}] {todoContent}')
        manager.ask_next_step()

    elif listSelection == TODO_READ:
        print('----전체 일정 조회----')
        manager.showTodoIist()

    elif listSelection == TODO_END:
        print('시스템을 종료합니다.')
        todo = False

    else:
        print('입력 번호를 다시 확인해주세요.')