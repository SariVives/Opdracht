import sys, csv, sqlite3

script, input, database, output = sys.argv
#een inputbestand dat enkele titels van foto's bevat
Fotos[]

try:
	with open( input, 'r') as inputbestand:
		Fotos = inputbestand.readlines()
	except:
		print("Fout bij inlezen inputbestand")
		sys.exit(-1)

query = """
select Foto.Titel, Locatie.Depot/Sectie/Doos from Foto join Locatie using(FotoID) where Foto.Titel like ?;
"""
try:
	dbconnectie = sqlite3.connect("testdatabase.db")
except:
	print("geen connectie met database mogelijk")
	sys.exit(-1)


mijncursor = dbconnectie.cursor()
mijnquery = "SELECT titel FROM "
#het wegschrijven naar een CSV bestand
try:
	with open('export.csv' , 'w') as export_file:
		my_writer = csv.writer(export_file)
		for foto in Fotos:
			pass
except Exception as e:
	print("Fout bij wegschrijven: ", e)
	sys.exit(1)

