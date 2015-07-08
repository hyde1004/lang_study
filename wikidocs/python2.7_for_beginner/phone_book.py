"""전화번호부

요구사항
 - 입력/목록/삭제/정렬 기능 제공
 - 파일에 저장하고 프로그램 실행시에 다시 읽어온다.

개발순서
1. 파일 저장없는 입력/목록/삭제/정렬 기능을 구현
2. 파일에 결과 저장하기
3. 파일에서 결과 읽어오기

"""

def display(a_phone_book):
	print("NAME\tPHONE NUMBER")
	for phone_info in a_phone_book:
		for name, phone_num in phone_info.items():
			print("%s\t%s" % (name, phone_num))

phone_book = []

phone_info1 = {'Jack' : '010-1234-1234'}
phone_info2 = {'Hyde' : '02-111-1212'}

phone_book.append(phone_info1)
phone_book.append(phone_info2)

display(phone_book)

