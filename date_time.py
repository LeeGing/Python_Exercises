#Current Date and Time

from datetime import datetime
current = datetime.now()
print '[Date: %s/%s/%s]' % (current.month, current.day, current.year)
print '[Time: %s:%s:%s]' % (current.hour, current.minute, current.second)
