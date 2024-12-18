class Foto:

	def __init__(self, titel):
		self.titel = titel

	def print(self):
		print(self.titel)

foto1 = Foto("Manneke Pis")
foto2 = Foto("Guido Gezelle")

for foto in [foto1,foto2]:
	foto.print()