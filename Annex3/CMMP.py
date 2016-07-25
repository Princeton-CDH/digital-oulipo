# -*- coding: utf-8 -*-
# The poetry contained within this program is taken from Cent mille milliards de poèmes, 
# a 1961 collection of poetry that is currently under copyright and owned by Gallimard.
# The reason that I have chosen to include the poems in the code itself is so the data 
# structure of Queneau's original volume is visible. See Readme for more information.

from datetime import date
from datetime import time
from datetime import datetime

import uuid
import math
import subprocess

class Corpus:
    
    poems = [   
     
[u'Le roi de la pampa retourne sa chemise', 
u'pour la mettre à sécher aux cornes des taureaux',
u'le cornédbîf en boîte empeste la remise',
u'et fermentent de même et les cuirs et les peaux',
u'Je me souviens encor de cette heure exeuquise ',
u'les gauchos dans la plaine agitaient leurs drapaux',
u'nous avions aussi froid que nus sur la banquise',
u'lorsque pour nous distraire y plantions nos tréteaux',
u'Du pôle à Rosario fait une belle trotte',
u'aventures on eut qui s\'y pique s\'y frotte',
u'lorsqu\' on boit du maté l\'on devient argentin',
u'L\'Amérique du Sud séduit les équivoques ',
u'exaltent l\'espagnol les oreilles baroques',
u'si la cloche se tait et son terlintintin'],
     
[u'Le cheval Parthénon s\'énerve sur sa frise',
u'depuis que le lord Elgin négligea ses naseaux',
u'le Turc de ce temps-là pataugeait dans sa crise',
u'il chantait tout de même oui mais il chantait faux',
u'Le cheval Parthénon frissonnait sous la bise',
u'du client londonien où s\'ébattent les beaux',
u'il grelottait le pauvre aux bords de la Tamise',
u'quand les grêlons fin mars mitraillent les bateaux',
u'La Grèce de Platon à coup sûr n\'est point sotte',
u'on comptait les esprits acérés à la hotte',
u'lorsque Socrate mort passait pour un lutin',
u'Sa sculpture est illustre et dans le fond des coques',
u'on transporte et le marbre et débris et défroques',
u'si l\'Europe le veut l\'Europe ou son destin'],

[u'Le vieux marin breton de tabac prit sa prise',
u'pour du fin fond du nez exciter les arceaux',
u'sur l\'antique bahut il choisit sa cerise',
u'il n\'avait droit qu\'à une et le jour des Rameaux',
u'Souvenez-vous amis de ces îles de Frise',
u'où venaient par milliers s\'échouer les harenceaux',
u'nous regrettions un peu ce tas de marchandise',
u'lorsqu\'on voyait au loin flamber les arbrisseaux',
u'On sèche le poisson dorade ou molve lotte',
u'on sale le requin on fume à l\'échalotte',
u'lorsqu\'on revient au port en essuyant un grain',
u'Enfin on vend le tout homards et salicoques',
u'on s\'excuse il n\'y a ni baleines ni phoques',
u'le mammifère est roi nous sommes son cousin'],

[u'C\'était à cinq o\'clock que sortait la marquise',
u'pour consommer un thé puis des petits gâteaux',
u'le chauffeur indigène attendait dans la brise',
u'elle soufflait bien fort par dessus les côteaux',
u'On était bien surpris par cette plaine grise',
u'quand se carbonisait la fureur des châteaux',
u'un audacieux baron empoche toute accise',
u'lorsque vient le pompier avec ses grandes eaux',
u'Du Gange au Malabar le lord anglais zozotte',
u'comme à Chandernagor le manant sent la crotte',
u'le colonel s\'éponge un blason dans la main',
u'Ne fallait pas si loin agiter ses breloques',
u'les Indes ont assez sans ça de pendeloques',
u'l\'écu de vair ou d\'or ne dure qu\'un matin'],

[u'Du jeune avantageux la nymphe était éprise',
u'snob un peu sur les bords des bords fondamentaux',
u'une toge il portait qui n\'était pas de mise',
u'des narcisses on cueille ou bien on est des veaux',
u'Quand on prend des photos de cette tour de Pise',
u'd\'où Galilée jadis jeta ses petits pots',
u'd\'une étrusque inscription la pierre était incise',
u'les Grecs et les Romains en vain cherchent leurs mots',
u'L\'esprit souffle et resouffle au-dessus de la botte',
u'le touriste à Florence ignoble charibotte',
u'l\'autocar écrabouille un peu d\'esprit latin',
u'Les rapports transalpins sont-ils biunivoques ?',
u'les banquiers d\'Avignon changent-ils les baïoques ?', 
u'le Beaune et le Chianti sont-ils le même vin ?'],
     
[u'Il se penche il voudrait attraper sa valise',
u'que convoitait c\'est sûr une horde d\'escrocs',
u'il se penche et alors à sa grande surprise',
u'il ne trouve aussi sec qu\'un sac de vieux fayots',
u'Il déplore il déplore une telle mainmise',
u'qui se plaît à flouer de pauvres provinciaux',
u'aller à la grand ville est bien une entreprise',
u'elle effraie le Berry comme les Morvandiaux',
u'Devant la boue urbaine on retrousse sa cotte',
u'on gifle le marmot qui plonge sa menotte',
u'lorsqu\'il voit la gadoue il cherche le purin',
u'On regrette à la fin les agrestes bicoques',
u'on mettait sans façon ses plus infectes loques',
u'mais on n\'aurait pas vu le métropolitain'],

[u'Quand l\'un avecque l\'autre aussitôt sympathise',
u'se faire il pourrait bien que ce soit des jumeaux',
u'la découverte alors voilà qui traumatise',
u'on espère toujours être de vrais normaux',
u'Et pourtant c\'était lui le frère de feintise',
u'qui clochard devenant jetait ses oripeaux',
u'un frère même bas est la part indécise',
u'que les parents féconds offrent aux purs berceaux',
u'Le généalogiste observe leur bouillotte',
u'gratter le parchemin deviendra sa marotte',
u'il voudra retrouver le germe adultérin',
u'Frère je te comprends si parfois tu débloques',
u'frère je t\'absoudrai si tu m\'emberlucoques',
u'la gémellité vraie accuse son destin'],
     
[u'Lorsqu\'un jour exalté l\'aède prosaïse',
u'pour déplaire au profane aussi bien qu\'aux idiots',
u'la critique lucide aperçoit ce qu\'il vise'
u'il donne à la tribu des cris aux sens nouveaux'
u'L\'un et l\'autre a raison non la foule insoumise',
u'le vulgaire s\'entête à vouloir des vers beaux',
u'l\'un et l\'autre ont raison non la foule imprécise',
u'à tous n\'est pas donné d\'aimer les chocs verbaux',
u'Le poète inspiré n\'est point un polyglotte',
u'une langue suffit pour emplir sa cagnotte',
u'même s\'il prend son sel au celte c\'est son bien',
u'Barde que tu me plais toujours tu soliloques',
u'tu me stupéfies plus que tous les ventriloques',
u'le métromane à force incarne le devin'],
     
[u'Le marbre pour l\'acide est une friandise',
u'd\'aucuns par dessus tout prisent les escargots',
u'sur la place un forain de feu se gargarise',
u'qui sait si le requin boulotte les turbots ?', 
u'Du voisin le Papou suçote l\'apophyse',
u'que n\'a pas dévoré la horde des mulots ?',
u'le gourmet en salade avale la cytise',
u'l\'enfant pur aux yeux bleus aime les berlingots',
u'Le loup est amateur de coq et de cocotte',
u'le chat fait un festin de têtes de linotte',
u'le chemin vicinal se nourrit de crottin',
u'On a bu du pinard à toutes les époques',
u'grignoter des bretzels distrait bien des colloques',
u'mais rien ne vaut grillé le morceau de boudin'],
     
[u'Lorsque tout est fini lorsque l\'on agonise',
u'lorsque le marbrier astique nos tombeaux',
u'des êtres indécis vous parlent sans franchise',
u'et tout vient signifier la fin des haricots',
u'On vous fait devenir une orde marchandise',
u'on prépare la route aux pensers sépulcraux',
u'de la mort on vous greffe une orde bâtardise',
u'la mite a grignoté tissus os et rideaux',
u'Le brave a beau crier ah cré nom saperlotte',
u'le lâche peut arguer de sa mine pâlotte',
u'les croque-morts sont là pour se mettre au turbin',
u'Cela considérant ô lecteur tu suffoques',
u'comptant tes abattis lecteur tu te disloques',
u'toute chose pourtant doit avoir une fin']     
]

    def begin(self): 
		print "Would you like to read one of Queneau's original sonnets? If yes, type 1."
		print "Would you like to generate a pseudo-random sonnet based on your age? If yes, type 2."
		print "Would you like to generate a pseudo-random sonnet based on your position? If yes, type 3."
		print "Would you like to generate a pseudo-random sonnet based on your computer? If yes, type 4." 
		choice = 0 
		while choice ==0: 
			choice = int(raw_input())
			if choice == 1: 
				return self.pick_sonnet() 
			elif choice == 2: 
				return self.age_sonnet()
			elif choice == 3: 
				return self.location_sonnet()
			elif choice == 4:
				return self.computer_sonnet()
			else: 
				print "That is not a valid choice."  
				choice = 0
    
    def print_sonnet(self, sonnet):
		for line in sonnet: 
			print line
			print "\n"
    
    def get_sonnet(self, index):
        return self.poems[index]
    
    def get_line(self, sonnet, verse):
        return self.poems[sonnet][verse]
    
    def generate_sonnet(self, key):
        sonnet = []
        for i in range(0, len(key)):
            sonnet.append(self.get_line(int(key[i]), i))
        return sonnet
    
    def get_all_verses(self, verse_number):
        result = []
        for i in range(0,9):
            result.append(self.get_line(i, verse_number))
        return result
    
    def pick_sonnet(self): 
    	print "Which of Queneau's original 10 sonnets would you like to read?"
    	key = int(raw_input())
    	self.print_sonnet(self.get_sonnet(key - 1))
    	
    def computer_sonnet(self):
		number = uuid.uuid1().int
		key = str(number)[0:14]
		self.print_sonnet(self.generate_sonnet(key))
    	
    def location_sonnet(self):
		print "Go to <http://ctrlq.org/maps/where/>."
		print "What is your latitude? (no negatives, to the nearest thousandth)" 
		latitude = float(raw_input())
		print "What is your longitude? (no negatives, to the nearest thousandth)"
		longitude = float(raw_input())
		key = "{:14.0f}".format(latitude*longitude*100987654321)
		self.print_sonnet(self.generate_sonnet(key))	

    def age_sonnet(self):
		print "What is your birthday? mmddyyyy?"
		birthday = int(raw_input())
		key = str(birthday*birthday)[0:14] 
		self.print_sonnet(self.generate_sonnet(key))
		

if __name__ == "__main__":
	c = Corpus()
	c.begin()