day_number = int(input('오늘 날짜를 입력하세요'))
print('오늘날짜는', day_number, '일 입니다')

car_number = input('차량번호 입력하세요(ex: 1234)')

if day_number >31 or day_number ==0 :
    print('잘못된 날짜입니다.')
    exit()
if not car_number.isdigit() or len(car_number) !=4 :
    print('잘못된 차량번호 입니다.')