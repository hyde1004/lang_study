# file practice

# 파일 전체를 한번에 작업하기

oz_book = open('THE_WONDERFUL_WIZARD_OF_OZ.txt', 'r')
text = oz_book.read()
oz_book.close()

print("*** Text ***")
print()
print(text)
print()
print("TOTAL LENGTH : %d" % (len(text)))


# 줄 단위로 작업하기
oz_book = open("THE_WONDERFUL_WIZARD_OF_OZ.txt", 'r')
text = oz_book.readlines()
oz_book.close()

print("*** Analyzing ***")
print("Total %d Line(s)" % (len(text)))
for line in text:
	print(len(line))

