ages = {'shubh':12,'kevin':'34','bob':'11',('joshi','prasad'):'22'}

print(ages[('joshi','prasad')])


print(ages['shubh'])

del ages['shubh']

ages['newkey']= 13
print(ages['newkey'])

new_dict=dict(kevin=160,bob=100,kayla=333)
print(new_dict)

newer_dict = dict([(1,2),(3,4),(5,6)])
print(newer_dict)

print(1 in newer_dict)

print(newer_dict.fromkeys())

print(ages.values())

print(new_dict.items())