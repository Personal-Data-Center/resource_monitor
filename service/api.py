from django.http import JsonResponse
from django.conf import settings

import os
import psutil

def getResources(request):
    if request.method == 'GET':
        if request.user.admin != True and request.isApi is True:
            node = {
            'nodeId' : os.environ.get('NODE_ID'),
            'cpuUsage': psutil.cpu_percent(),
            'cpuCount': psutil.cpu_count(),
            'cpuFreq': psutil.cpu_freq(),
            'ramTotal': (psutil.virtual_memory().total/ (2**30)),
            'ramUsed': psutil.virtual_memory().percent,
            'diskTotal': (psutil.disk_usage('/').total / (2**30)),
            'diskUsed': (psutil.disk_usage('/').used / (2**30)),
            'diskFree': (psutil.disk_usage('/').free / (2**30)),
            }
            content ={ **{'Success' : True}, 'node': node}
        else:
            content = {'Success' : False, 'error' : 'only admin user allowed'}
    else:
        content = {'Success' : False, 'Error' : 'not GET method'}
    return JsonResponse(content)
