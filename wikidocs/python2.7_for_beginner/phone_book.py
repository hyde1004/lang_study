"""전화번호부

요구사항
 - 입력/목록/삭제/정렬 기능 제공
 - 파일에 저장하고 프로그램 실행시에 다시 읽어온다.

개발순서
1. 파일 저장없는 입력/목록/삭제/정렬 기능을 구현
2. 파일에 결과 저장하기
3. 파일에서 결과 읽어오기

history
 - 굳이 list를 사용해서 순서를 정할 필요가 있을까?
   정렬을 해서 출력하면 되기 때문에 dict로 저장하는게 더 나아보인다.
   구조도 더 단순해진다.

"""

def display(a_phone_book):
	print("NAME\tPHONE NUMBER")
	for name, phone_num in a_phone_book.items():
		print("%s\t%s" % (name, phone_num))

phone_book = {}

phone_book['Jack'] = '010-1234-1234'
phone_book['Hyde'] = '02-111-1212'

display(phone_book)

