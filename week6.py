

class Posting:
    def post_write(self):
        self.board = list()
        post_number = input('저장할 게시글의 수 : ')
        for i in range(0, int(post_number)):
            id_number = i + 1
            input_title = input('게시글 제목 : ') 
            input_text = input('게시글 내용 : ')
            self.board.append(Posting().post_create(id_number, input_title, input_text))
        Posting().post_search(self.board)

    def post_create(self, id, title, text):
        dictionary = {
            'id' : id,
            'title' : title,
            'text' : text  
        }
        print('저장되었습니다.')
        return dictionary
    
    def post_search(self, board):
        search_id = input('게시물을 검색해주세요 : ')
        print(board)
        #print(board[1].val ues()) # 2, 2, 2
        #print(board[1].[key = "id"].values()) #  #
        for i in range(0, len(board)):
            if search_id in board[i]["id"].values():
                print('find')

# 깃헙 브런치 바꾸는 법
Posting().post_write()