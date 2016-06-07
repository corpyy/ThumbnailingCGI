#!/usr/bin/env python
# -*- coding: utf-8 -*-

html_body= '''
<html>
<head>
</head>
<body>
test test
%s
</body>
</html>'''

import cgi
form = cgi.FieldStorage()

print 'Content-type: text/html\n'
print html_body % form['img'].value

