# list는 인덱스 번호로 데이터에 접근한다.

korea = ['daum-kakao', 'naver']
print(korea[0])
print(korea[1])

# 변수보다 나은 점은
# 반복문을 이용하여 쉽게 데이터 처리가 가능하다.
for i in korea:
	print(i)

# 사전은 key를 통해 데이터 접근 가능하다.
test_dic = { 'key1':'room1', 'key2':'room2'}
print(test_dic['key1'])
print(test_dic['key2'])

price = { "2015-02-04" : 30100, "2015-02-05" : 31000 }
print(price["2015-02-04"])
print(price["2015-02-05"])


