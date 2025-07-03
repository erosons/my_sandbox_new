from datetime import datetime,timedelta,timezone
import pytz    
utc_time = datetime.now(timezone.utc)
tz = pytz.timezone('CST6CDT')

utc_time =utc_time.replace(tzinfo=pytz.utc).astimezone(tz)