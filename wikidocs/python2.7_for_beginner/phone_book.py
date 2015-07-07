"""전화번호부

요구사항
 - 입력/목록/삭제/정렬 기능 제공
 - 파일에 저장하고 프로그램 실행시에 다시 읽어온다.

"""

phone_book_list = []
phone_book_file = open("phone_book.txt", 'r')
total_phone_num = int(phone_book_file.readline())

phone_book_file.close()



# name = phone_book_file.readline()
# phone = phone_book_file.readline()
