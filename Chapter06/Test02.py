# 创建字典
cleese={}
# 创建字典
palin = dict()

print(type(cleese))
print(type(palin))

cleese['Name']='John Cleese'
cleese['Occupations']=['actor', 'comedian', 'writer', 'film producer']
palin={'Name':'Michael Palin', 'Occupations':['comedin', 'actor', 'writer', 'tv']}
print(palin['Name'])
print(cleese['Occupations'][-1])

# 动态扩展字典项 新增出身地
cleese['Birthplace']='Broomhill, Sheffield, England'
palin['Birthplace']='Weston-super-Mare, North Somerset, England'

print(palin)
print(cleese)
