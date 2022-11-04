'''
text = ' azat   Disk1         for     kivanoparser  lesson5  lesson8  module.py     parserbot       snap     telegrwmbot  var   wather_bot  Документы  Изображения  Общедоступные
cdrom  dosmartov.py  github  lesson10      lesson7  lesson9  my_module.py  python_lessons  ssh-key  tmp          venv  Видео       Загрузки   Музыка       Шаблоны  '
with open('directories.txt', 'w') as file:
	file.write(text)

with open('directories.txt', 'r') as f:
	content = f.read()
	print(content)
'''
'''
f = open('directories.txt', 'r')
a = f.read()
print(a)
f.close()
'''
'''
login =input('username: ')
password =input ('password:')


with open('users.txt' ,'w') as file:
	file.write(login)
	file.write(password)
'''

'''
1. Допустим у нас есть список языков программирования. lang1 = 'Rust'
 languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
 Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
 Если этого языка нет в списке, ничего не нужно выводить.
'''
'''
lang1 = 'php'
languages =['go','java','php','python','javascript','rudy']
text = 'this languages is in list '
for i in languages:
	if lang1 == i:
		print(text)
'''


a = int(input('chislo: '))
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 111,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,]

if  a in ls:
	print('yes') 
else:
	print('no')
	
