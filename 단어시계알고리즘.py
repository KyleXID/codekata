import sys


hour = int(sys.stdin.readline())
minute = int(sys.stdin.readline())

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number_strs = '''one two three four five six seven eight nine ten eleven twelve thirteen fourteen quarter sixteen seventeen eighteen nineteen twenty'''
number_dict=dict(zip(numbers, number_strs.split()))

def check_minute(minute):
    # 분을 확인하여 30분을 기준으로 past인지 to인지 구분한다.
    # to인 경우 남은 분을 확인하기 위해 60분에서 빼준다.
    if minute <= 30:
        connect = 'past'
        target_minute = minute
    elif minute > 30:
        connect = 'to'
        target_minute = 60 - minute

    # 변환하고자 하는 분을 dictionary를 통해 변환해준다. 20이상은 일의자리를 분리해서 변환한다.
    if target_minute <= 20:
        minute_str = number_dict[target_minute]
    elif target_minute > 20 and target_minute < 30:
        units = int(str(target_minute)[1])
        minute_str = 'twenty' + ' ' + number_dict[units]
    elif target_minute == 30:
        minute_str = 'half'

    return connect, minute_str

# 시간을 영어로 표현하는 함수
def change_clock(hour, minute):
    # 30분 이상인 경우 시간에 +1을 해준다. 12시인경우 1시로 만들어준다.
    if minute > 30:
        if hour == 12:
            hour = 1
        else:
            hour = hour + 1

    # 시간을 영어로 변환한다.
    str_hour = number_dict[hour]

    if minute == 0:
        str_clock = f'{str_hour} o\' clock'
    else:
        # past와 to을 정하고 분을 영어로 변환한다.
        connect, str_minute = check_minute(minute)
        if str_minute in ('quarter', 'half'):
            # quater, half 인 경우 minute 문자를 제외하고 표현해준다.
            str_clock = f'{str_minute} {connect} {str_hour}'
        else:
            # 1분 일때는 단수형으로 출력한다
            if str_minute == 'one':
                m = 'minute'
            else:
                m = 'minutes'

            str_clock = f'{str_minute} {m} {connect} {str_hour}'

    return str_clock

print(change_clock(hour, minute))