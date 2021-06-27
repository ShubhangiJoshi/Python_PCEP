email = {}

assert email == {}


print (email)

email = {'shubh':"sh@hrgfd.com",'prd':'snd@sds.com','awss':'qwqw@asa.com','aqw':'kotk'}

email['ash'] = 'ash@example.com'
email ['craig'] = 'craig@example.com'

print(email)

email['dalton'] = 'qwq@example.com'

print(email)
del email['craig']

print(email )

user_list = list(email .keys())

#assert user_list == []

print(user_list)

email_list = list(email.values())

print(list(sorted(reversed(email_list))))

pair = email.items()

print(pair)

modified_dict = {}