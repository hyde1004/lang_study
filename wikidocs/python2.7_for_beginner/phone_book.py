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

def display_menu():
	print('')
	print('### MENU ###')
	print('')
	print('1. Display list')
	print('2. Input phone number')
	print('3. Delete phone number')
	print('4. Save list')
	print('5. Quit')
	print('')

	choice = input('Your choice : ')

	return choice

def display_list(a_phone_book):
	print('')
	print('DISPLAY LIST')
	print("NAME\tPHONE NUMBER")
	print('====\t============')
	for name, phone_num in a_phone_book.items():
		print("%s\t%s" % (name, phone_num))

def input_list(a_phone_book):
	print('')
	print('INPUT PHONE NUMBER')
	name = input('What is name? : ')
	phone_num = input('What is phone number? : ')
	a_phone_book[name] = phone_num

phone_book = {}



while True:
	choice = display_menu()

	if choice == '1':
		display_list(phone_book)
	elif choice == '2':
		input_list(phone_book)
	elif choice == '5':
		break
	else:
		pass



