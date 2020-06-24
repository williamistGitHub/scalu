


import math


class universe():

	def __init__(self):
		self.computations = list()
		self.known_aliases = list()
		self.picker = picker()
		self.constructs = dict()
		#initialize universal aliases
		true_alias = self.picker.new_alias()
		false_alias = self.picker.new_alias()
		self.true = alias(true_alias, "true")
		self.false = alias(false_alias, "false")
		self.known_aliases.append(self.true)
		self.known_aliases.append(self.false)

	def add_computation(self, alias_type):
		alias_string = self.picker.new_alias()
		new_alias = alias(alias_string, alias_type)
		new_computation = computation(new_alias, list())
		self.known_aliases.append(new_alias)
		self.computations.append(new_computation)
		return new_computation

	def add_alias(self, alias_type):
		alias_string = self.picker.new_alias()
		new_alias = alias(alias_string, alias_type)
		self.known_aliases.append(new_alias)
		return new_alias


class computation():

	def __init__(self, alias_object, command_list):
		self.alias = alias_object
		self.commands = list()

	def extend(self, command):
		self.commands.append(command)

class alias():

	def __init__(self, string, compile_type):
		self.string = string
		self.type = compile_type

class bind():

	def __init__(self, key, computation):
		self.key = key
		self.computation = computation

class source_command():

	def __init__(self, string):
		self.string = string

class picker():

	def __init__(self):

		self.symbols = list()
		self.current_use = 1
		lower_case_letters = range(97,123)
		numbers = range(48,58)
		for x in numbers:
			self.symbols.append(chr(x))
		for x in lower_case_letters:
			self.symbols.append(chr(x))

	def new_alias_list(self, count):
		alias_list = list()
		for alias in range(count):
			alias_list.append(self.new_alias())
		return alias_list


	def new_alias(self):
		revolutions = int(math.log(self.current_use, len(self.symbols))) + 1
		new_alias = list()
		for x in range(0, revolutions):
			selected = int((self.current_use / int((len(self.symbols) ** x)) % len(self.symbols)))
			new_alias = [self.symbols[selected]] + new_alias
		new_alias = ''.join(new_alias)
		new_alias = '%' + new_alias  #using π here causes strange behavior
		self.current_use += 1
		return new_alias
