# 테스트 해보는 프로젝트
# 게시글을 입력하고 저장할 수 있는 프로젝트를 구현해보도록 한다.

class board:

    def __init__(self):
        self.number = input("원하는 수의 포스팅 : ")


    def write(self):
        board = list()
        for i in range(0, int(self.number)):
            print(f"\n{i + 1}번째 게시글")
            write_post_title = input("제목 : ")
            write_post_text = input("내용 : ")
            post = { write_post_title : write_post_text }
            board.append(post)
        return board

def output_posts(board):
    board_value = board.keys()
    for i in range(0, len(board)):
        for x in board_value:
            print(f"\n{i + 1}번째 게시글\n제목 : {x}\n내용 : {board[x]}")


board = board().write()
output_posts(board)