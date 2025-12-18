Capitals = {'USA':'Washington DC',
            'India' : 'New Delhi',
            'Russia' : 'Moscow',
            'China' : 'Beijing'}
print(Capitals['Russia'])
print(Capitals.get('Germany'))
print(Capitals.keys())
print(Capitals.values())
print(Capitals.items())

Capitals.update({'Germany':'Berlin'})
Capitals.update({'USA' : 'Las Vagas'})
Capitals.pop('China')
Capitals.clear()

for key,value in Capitals.items():
    print(key,value)
    