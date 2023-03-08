import sqlite3

class create:
	def __init__(self, adself):
		self.connect = sqlite3.connect(adself.filename)
		self.cursor = self.connect.cursor()

	def table(self, *args):
		vars = ''
		vars_arg = args[2]
		vars_list = vars_arg.split(', ')
		for i in vars_list:
			if i.startswith('&&'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} TEXT PRIMARY KEY'
				else:
					vars += f'{var} TEXT PRIMARY KEY, '
			elif i.startswith('&'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} TEXT'
				else:
					vars += f'{var} TEXT, '
			elif i.startswith('**'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} INTEGER PRIMARY KEY'
				else:
					vars += f'{var} INTEGER PRIMARY KEY, '
			elif i.startswith('*'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} INT'
				else:
					vars += f'{var} INT, '
			elif i.startswith('##'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} FLOAT PRIMARY KEY'
				else:
					vars += f'{var} FLOAT PRIMARY KEY, '
			elif i.startswith('#'):
				var = i.split('-')[1]
				if (i == vars_list[len(vars_list)-1]):
					vars += f'{var} FLOAT'
				else:
					vars += f'{var} FLOAT, '
		if args[1]:
			self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {args[0]} ({vars})')
		else:
			self.cursor.execute(f'CREATE TABLE {args[0]} ({vars})')


class sqlite:
	def __init__(self, filename):
		self.filename = filename

	def create(self):
		return create(self)