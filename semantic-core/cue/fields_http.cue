package schema

Fields: HTTP: {
	"http.status_code": {
		"description": "\nThe HTTP response status code.\nWhen span.kind: client the response status code received.\nWhen span.kind: server the response status code sent.\nNote: Although this is an integer, it must be sent as a string."
		"examples": [
			"200",
			"404",
			"500",
		]
		"pattern": "^[12345]\\d\\d$"
		"title":   "HTTP Status Code"
		"type":    "string"
	}
	"http.url": {
		"description": "\nThe URL of the HTTP request, including the obfuscated query string."
		"examples": [
			"https://example.com:443/search?q=datadog",
		]
		"is_sensitive": true
		"minLength":    1
		"title":        "HTTP URL"
		"type":         "string"
	}
	"http.method": {
		"description": "\nThe HTTP method used for the connection. Required for both client and server spans."
		"examples": [
			"GET",
			"POST",
			"PUT",
			"DELETE",
			"PATCH",
		]
		"pattern": "^(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)$"
		"title":   "HTTP Method"
		"type":    "string"
	}
	"http.version": {
		"description": "\nThe version of HTTP used for the request."
		"examples": [
			"1.0",
			"1.1",
			"2.0",
		]
		"pattern": "^1\\.[01]$|^2\\.0$"
		"title":   "HTTP Version"
		"type":    "string"
	}
	"http.route": {
		"default":     null
		"description": "\nThe matched route (path template).\nOnly when span.kind: server."
		"examples": [
			"/users/:userID",
		]
		"minLength": 1
		"title":     "HTTP Route"
		"type":      "string"
	}
	"http.client_ip": {
		"default":     null
		"description": "\nThe IP address of the original client behind all proxies, if known (discovered from headers such as X-Forwarded-For)."
		"examples": [
			"192.168.123.132",
		]
		"is_sensitive": true
		"pattern":      "^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}|(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
		"title":        "HTTP Client IP"
		"type":         "string"
	}
	"http.useragent": {
		"default":     null
		"description": "\nThe user agent header received with the request.\nOnly when span.kind: server."
		"examples": [
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
		]
		"is_sensitive": true
		"minLength":    1
		"title":        "HTTP User Agent"
		"type":         "string"
	}
	"http.request.content_length": {
		"default":     null
		"description": "\nThe size of the request body.\nThe size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.\nFor requests using transport encoding, this should be compressed size."
		"examples": [
			1234,
		]
		"exclusiveMinimum": 0
		"is_sensitive":     true
		"title":            "HTTP Request Content Length"
		"type":             "integer"
	}
	"http.response.content_length": {
		"default":     null
		"description": "\nThe size of the response payload body in bytes.\nThe size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.\nFor requests using transport encoding, this should be compressed size."
		"examples": [
			1234,
		]
		"exclusiveMinimum": 0
		"is_sensitive":     true
		"title":            "HTTP Response Content Length"
		"type":             "integer"
	}
	"http.request.content_length_uncompressed": {
		"default":     null
		"description": "\nThe size of the request payload body after transport decoding. Not set if transport encoding not used."
		"examples": [
			1234,
		]
		"exclusiveMinimum": 0
		"is_sensitive":     true
		"title":            "HTTP Request Content Length Uncompressed"
		"type":             "integer"
	}
	"http.response.content_length_uncompressed": {
		"default":     null
		"description": "\nThe size of the response payload body after transport decoding. Not set if transport encoding not used."
		"examples": [
			1234,
		]
		"exclusiveMinimum": 0
		"is_sensitive":     true
		"title":            "HTTP Response Content Length Uncompressed"
		"type":             "integer"
	}
}
