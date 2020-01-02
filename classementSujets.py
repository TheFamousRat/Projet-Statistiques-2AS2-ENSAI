#Output actuel : '27;32;38;29;28;17;16;18;14;34;15;21;31;13;30;33;23;36;40;24;10;39;35;11;26;37;20;9;7;42;6;8;5;3;2;12;22;25;19;1;41;4;43'
NOMBRE_SUJETS = 43

classements = {}
classements['Alexandre'] = '38;33;34;27;14;15;13;39;23;32;28;24;16;29;17;9;20;8;7;21;30;31;18;10;11;12;19;26;25;37;35;40;41;42;3;1;2;22;5;6;4;36;43'
classements['Aurélien'] = '16;17;40;27;5;29;37;6;18;34;28;22;32;21;36;35;2;3;7;14;15;19;41;20;1;33;38;31;30;10;11;4;26;25;23;9;24;8;42;39;13;12;43'
classements['Guillaume'] = '38;31;32;30;13;42;36;27;29;28;26;18;10;11;12;17;21;24;23;14;15;39;35;8;9;25;3;2;16;33;6;40;34;20;1;5;22;37;4;7;19;41;43'

classementSujets = {}
for i in range(1,NOMBRE_SUJETS+1):
  classementSujets[i] = 0
for personne in classements:
  classementPersonnel = classements[personne].split(';')
  for i in range(1, NOMBRE_SUJETS+1):
    classementSujets[i] += NOMBRE_SUJETS - classementPersonnel.index(str(i))

finalClassementStr = ''
classementTrie = sorted(classementSujets.items(), key = lambda kv:(kv[1], kv[0]))
for i in range(len(classementTrie)-1, -1, -1):
  finalClassementStr += str(classementTrie[i][0]) +';'

print(finalClassementStr)
