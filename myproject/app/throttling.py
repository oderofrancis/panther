from datetime import timedelta
from panther.throttling import Throttling


InfoThrottling = Throttling(rate=5, duration=timedelta(minutes=1))
