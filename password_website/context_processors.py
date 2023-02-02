def users_proc(request):
    PORTAL_URL = request.get_host()
    return {'PORTAL_URL': f'http://{PORTAL_URL}'}
