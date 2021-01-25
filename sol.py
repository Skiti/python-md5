import hashlib

password_length = 10
#il set di caratteri che possono comporre la password
characters = "abcdefghilmnopqrstuvzxykjw"
#characters = "abcde"
password = ""
# 0 = a, 1 = b etc. quindi itero così
# 0 0 0 0 0 0 0 0 0 0 = a a a a a a a a a a
# 0 0 0 0 0 0 0 0 0 1 = a a a a a a a a a b
# ...
# 0 0 0 25 0 0 0 0 2 1 = a a a w a a a a c b
# ...
# 25 25 25 25 25 25 25 25 25 25  = w w w w w w w w w w
indexes = [ 0,0,0,0,0,0,0,0,0,0 ]

#"lorislento", la soluzione corretta
correct_md5 = "8bd4df69ed228fc6dea0e6d3012f478e" 
#"aaaaaaaaab", una soluzione alternativa, giusto per dimostrazione veloce
#correct_md5 = "ba05a43d3b98a72379fdc90a1e28ecaf"

#ciclo infinito, termina solo in caso di:
#break 1 -> trova la soluzione corretta
#break 2 -> esaurito tutte le possibile stringhe che si possono creare
while True:
	#reset del tentativo scorso di password
	password = ""
	#ciclo per 10 volte perchè voglio inserire 10 caratteri nella password a lunghezza 10
	for j in range(len(indexes)):
		#recupera l'indice in cui siamo attualmente, tipo il 3° indice di 0000000100 sarebbe 1 
		chara_index = indexes[j]
		#converti il valore dell'indice in una lettera es. 1 = b
		single_chara = characters[chara_index]
		#print("I'm going to append character: " + single_chara)
		password = password + single_chara
	#stampa il nuovo tentativo di indovinare la password
	print("Password guess: " + password)
	
	#ottieni la password crittografata in md5
	#copiato uguale dal codice originale, non serve capire come funziona
	password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
	#controllare se l'md5 del nuovo tentativo corrisponde ad md5 "hardcodato" che trovate nel codice
	if password_md5 == correct_md5:
		print("Found correct md5")
		break
	
	#gestione degli indici, sarebbe estremamente più semplcie con funzioni ma ve lo metto il più terra terra possibile
	#ho appena cercato di indovinare 0000000000 cioè aaaaaaaaaa
	#ora voglio indovinare 0000000001 cioè aaaaaaaaab
	indexes[9] = indexes[9] + 1
	#la mia ultima lettera è la w con valore 25, se passo a 26, allora torno indietro a 0 
	if indexes[9] == len(characters):
		indexes[9] = 0
		indexes[8] = indexes[8] + 1
	#stessa cosa per tutti gli altri indici, appena raggiungo il massimo, scalo al prossimo ed azzero il currente
	if indexes[8] == len(characters):
		indexes[8] = 0
		indexes[7] = indexes[7] + 1
	if indexes[7] == len(characters):
		indexes[7] = 0
		indexes[6] = indexes[6] + 1
	if indexes[6] == len(characters):
		indexes[6] = 0
		indexes[5] = indexes[5] + 1
	if indexes[5] == len(characters):
		indexes[5] = 0
		indexes[4] = indexes[4] + 1
	if indexes[4] == len(characters):
		indexes[4] = 0
		indexes[3] = indexes[3] + 1
	if indexes[3] == len(characters):
		indexes[3] = 0
		indexes[2] = indexes[2] + 1
	if indexes[2] == len(characters):
		indexes[2] = 0
		indexes[1] = indexes[1] + 1
	if indexes[1] == len(characters):
		indexes[1] = 0
		indexes[0] = indexes[0] + 1
	#se arrivo qui vuol dire che ho iterato attraverso ogni possibile stringa
	#in questo caso specifico arrivo a 25 25 25 25 25 25 25 25 25 25 cioè w w w w w w w w w w 
	if indexes[0] == len(characters) and indexes[1] == len(characters) and indexes[2] == len(characters) and indexes[3] == len(characters) and indexes[4] == len(characters) and indexes[5] == len(characters) and indexes[6] == len(characters) and indexes[7] == len(characters) and indexes[8] == len(characters) and indexes[9] == len(characters):
		print("All possible iterations done")
		break

