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

 - 함수의 인자로 받던 것을 매개변수 없이 전역변수로 처리한다.
   모든 함수가 동일한 변수를 가르키는 것이므로..

"""

def sort_list(unsorted_keys):
	sorted_keys = sorted(list(unsorted_keys.keys()))
	return sorted_keys

def display_menu():
	print('')
	print('### MENU ###')
	print('')
	print('1. Display list')
	print('2. Input phone number')
	print('3. Delete phone number')
	print('4. Save list')
	print('5. Load list')
	print('6. Quit')
	print('')

	choice = input('Your choice : ')

	return choice

def display_list():
	print('')
	print('DISPLAY LIST')
	print("NAME\tPHONE NUMBER")
	print('====\t============')
	for name, phone_num in phone_book.items():
		print("%s\t%s" % (name, phone_num))

	print('==== Sorted list ====\n')
	sorted_list = sort_list(phone_book)
	for name in sorted_list:
		print("%s\t%s" % (name, phone_book[name]))

def input_list():
	print('')
	print('INPUT PHONE NUMBER')
	name = input('What is name? : ')
	phone_num = input('What is phone number? : ')
	phone_book[name] = phone_num

def del_list():
	print('')
	print('DELETE PHONE NUMBER')
	name = input('What is name? : ')
	del phone_book[name]

def save_list():
	print('')
	print('SAVE PHONE NUMBER')
	f = open('phone_data.txt', 'w')
	f.write("%d\n" % len(phone_book))
	for name, phone_num in phone_book.items():
		f.write("%s\n" % name)
		f.write("%s\n" % phone_num)

	f.close()

def load_list():
	print('')
	print('LOAD PHONE NUMBER')
	f = open('phone_data.txt', 'r')
	count = int(f.readline())

	global phone_book # global을 명시하지 않으면, 여기의 phone_book은 지역변수로 취급된다.

	phone_book = {}  # 기존 데이터 초기화

	for i in range(count):
		name = f.readline().rstrip()
		phone_num = f.readline().rstrip() 
		# 문장 끝의 '\n'을 rstrip()을 이용해서 잘라낸다.

		phone_book[name] = phone_num

	f.close()

phone_book = {}

while True:
	choice = display_menu()

	if choice == '1':
		display_list()
	elif choice == '2':
		input_list()
	elif choice == '3':
		del_list()
	elif choice == '4':
		save_list()
	elif choice == '5':
		load_list()
	elif choice == '6':
		break
	else:
		pass



