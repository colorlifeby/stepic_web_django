def application(environ, start_response):
	args = environ["QUERY_STRING"]
	args = args.split('&')
	body = '\n'.join(args)
	status = "200 OK"
	headers = [("Content-Type", "text/plain")]
	start_response(status, headers)
	return [body]
