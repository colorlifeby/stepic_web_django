CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/ask',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=3',
        '--timeout=60',
	'--log-file=/home/box/guni_wsgi.log',
        'wsgi',
    ),
}
