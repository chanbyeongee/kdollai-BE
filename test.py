from datetime import datetime
from pytz import timezone


now = datetime.now(timezone('Asia/Seoul'))
YMDHMS= now.strftime("%Y%m%d%H%M%S")
print(YMDHMS)
ampm = now.strftime('%p')
ampm_kr = '오전' if ampm == 'AM' else '오후'
real_time = now.strftime("%#H")
print(now.strftime('%#H:%M'))