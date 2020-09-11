import re

pattern=re.compile(r'[a-zA-Z].(X)')

cadena='ADXFAVX'


a=pattern.search(cadena)

print(a.group(2))


