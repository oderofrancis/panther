from datetime import datetime

from panther.app import API
from panther.configs import config
from panther import version, status
from panther.request import Request
from panther.response import Response
from app.throttling import InfoThrottling


@API()
async def hello_world_api():
    
    data = 'Hello World coming soon!'
    
    context = {
        'detail': data,
        'API': 'Data'
        }
    return context


@API(cache=True, throttling=InfoThrottling)
async def info_api(request: Request):
    data = {
        'version': version(),
        'datetime_now': datetime.now().isoformat(),
        'user_agent': request.headers.user_agent,
        'db_engine': config['db_engine'],
    }
    return Response(data=data, status_code=status.HTTP_202_ACCEPTED)
