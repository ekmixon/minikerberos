

class KerberosSPN:
	def __init__(self):
		self.username = None
		self.service  = None #the service we are trying to get a ticket for (eg. cifs/mssql...)
		self.domain   = None #the kerberos realm
		
	# https://docs.microsoft.com/en-us/windows/desktop/ad/name-formats-for-unique-spns
	#def from_spn(self):

	@staticmethod
	def from_user_email(s):
		#not actually email, but whatever
		kt = KerberosSPN()
		if s.find('@') == -1:
			raise Exception('Incorrect format, @ sign is missing!')
		kt.username, kt.domain = s.split('@')
		return kt
	
	@staticmethod
	def from_target_string(s):
		"""
		service/host@domain
		or
		host@domain
		"""
		kt = KerberosSPN()

		if s.find('/') != -1:
			t, kt.domain = s.rsplit('@',1)
			kt.service, kt.username = t.split('/')
		else:
			kt.domain, kt.username = s.split('@')
		return kt

	def get_principalname(self):
		return [self.service, self.username] if self.service else [self.username]

	def get_formatted_pname(self):
		if self.service:
			return f'{self.service}/{self.username}@{self.domain}'
		return f'{self.username}@{self.domain}'
	
	def __str__(self):
		return self.get_formatted_pname()