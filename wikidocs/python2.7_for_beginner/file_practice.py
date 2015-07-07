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

## 문서 줄단위로 길이 출력

oz_book = open("THE_WONDERFUL_WIZARD_OF_OZ.txt", 'r')
text = oz_book.readlines()
oz_book.close()

print("*** Analyzing ***")
print("Total %d Line(s)" % (len(text)))
for line in text:
	print(len(line))

## 파일 읽어 가수 + 노래 출력하기
songs_file = open('songs.txt', 'r')
num_of_songs = int(songs_file.readline())
print('total songs : %d' % (num_of_songs))

for num in range(num_of_songs):
	singer = songs_file.readline()
	song = songs_file.readline()

	print("singer : %s" % singer)
	print("song : %s" % song)



## 파일읽어 사람 + 전화번호

## 줄변 글자수, 전체 글자수 출력 