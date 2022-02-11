from __future__ import unicode_literals

from os.path import dirname, realpath
from subprocess import CalledProcessError, check_output

from django.http import JsonResponse

import eox_rate

def info_view(request):

    try:
        working_dir = dirname(realpath(__file__))
        git_data = check_output(['git', 'rev-parse', 'HEAD'], cwd=working_dir)
        git_data = git_data.decode().rstrip('\r\n')
    except CalledProcessError:
        git_data = ''

    return JsonResponse(
        {
            'version': eox_rate.__version__,
            'name': 'eox-rate',
            'git': git_data,
        },
    )
