

class Posting:
    def post_write(self):
        self.board = list()
        post_number = input('저장할 게시글의 수 : ')
        for i in range(0, int(post_number)):
            id_number = i + 1
            input_title = input('게시글 제목 : ') 
            input_text = input('게시글 내용 : ')
            self.board.append(Posting().post_create(id_number, input_title, input_text))
        Posting().post_search()

    def post_create(self, id, title, text):
        test = {
            'id' : id,
            'title' : title,
            'text' : text  
        }
        print('저장되었습니다.')
        return test
    
    def post_search(self):
        search_id = input('게시물을 검색해주세요 : ')
        if int(search_id) in self.board:
            print('find')
        else :
            print('no result')

Posting().post_write()