# -*- coding: utf-8 -*-
# The text contained within this program is taken from Un conte à votre façon, 
# a 1967 choose your own adventure tale that is currently under copyright and owned by Gallimard.
# The reason that I have chosen to include the story in the code itself is so the data 
# structure of Queneau's original tale is visible. See Readme for more information.

from graphviz import Digraph

class Node: 
	def __init__(self, description):
		self.description = description

	def describe(self):
		print self.description
		
class Edge:
	def __init__(self, number, description):
		self.number = number
		self.description = description
	
	def describe(self):
		print self.description 

class Graph: 
	def __init__(self):
		
		self.nodelist = {
			
        '1': Node("1. Désirez-vous connaître l'histoire des trois alertes petits pois?"),
        '2': Node("2. Préférez-vous celle des trois minces grands échalas?"),
        '3': Node("3. Préférez-vous celle des trois moyens médiocres arbustes?"),
        '4': Node("4. Il y avait une fois trois petits pois vêtus de vert qui dormaient gentiment dans leur cosse.\nLeur visage bien rond respirait par les trous de leurs narines et l'on entendait leur ronflement doux et harmonieux."),
        '5': Node("5. Ils ne rêvaient pas. Ces petits êtres en effet ne rêvent jamais."),
        '6': Node("6. Ils rêvaient. Ces petits êtres en effet rêvent toujours et leurs\nnuits sécrètent des songes charmants."),
        '7': Node("7. Leurs pieds mignons trempaient dans de chaudes chaussettes et ils portaient au lit des gants de velours noir."),
        '8': Node("8. Ils portaient au lit des gants de velours bleu."),
        '9': Node("9. Il y avait une fois trois petits pois qui roulaient leur bosse sur les grands chemins.\nLe soir venu, fatigués et las, ils s'endormaient très rapidement."),
        '10': Node("10. Tous les trois faisaient le même rêve, ils s'aimaient en effet tendrement et,\nen bons fiers trumeaux, songeaient toujours semblement."),
        '11': Node("11. Ils rêvaient qu'ils allaient chercher leur soupe à la cantine populaire\net qu'en ouvrant leur gamelle ils découvraient que c'était de la soupe d'ers.\nD'horreur, ils s'éveillent."),
        '12': Node("12. Opopoï! s'écrient-ils en ouvrant les yeux. Opopoï! quel songe avons-nous enfanté là!\nMauvais présage, dit le premier. Oui-da, dit le second, c'est bien vrai,\nme voilà triste. Ne vous troublez pas ainsi, dit le troisième qui était le plus futé,\nil ne s'agit pas de s'émouvoir, mais de comprendre, bref, je m'en vais vous analyser ça."),
        '13': Node("13. Tu nous la bailles belle, dit le premier. Depuis quand sais-tu analyser les songes?\nOui, depuis quand? ajouta le second."),
        '14': Node("14. Depuis quand? s'écria le troisième. Est-ce que je sais moi!\nLe fait est que je pratique la chose. Vous allez voir!"),
        '15': Node("15. Eh bien voyons, dirent ses frères. Votre ironie ne me plaît pas,\nrépliqua l'autre et vous ne saurez rien. D'ailleurs, au cours de cette conversation d'un ton assez vif,\nvotre sentiment d'horreur ne s'est-il pas estompé? effacé même?\nAlors à quoi bon remuer le bourbier de votre inconscient de papilionacées?\nAllons plutôt nous laver à la fontaine et saluer ce gai matin dans l'hygiène et la sainte euphorie!\nAussitôt dit, aussitôt fait: les voilà qui se glissent hors de leur cosse,\nse laissent doucement rouler sur le sol et puis au petit trot gagnent joyeusement le théâtre de leurs ablutions."),
        '16': Node("16. Trois grands échalas les regardaient faire."),
        '17': Node("17. Trois moyens médiocres arbustes les regardaient faire."),
        '18': Node("18. Se voyant ainsi zyeutés, les trois alertes petits pois qui\nétaient fort pudiques s'ensauvèrent."),
        '19': Node("19. Ils coururent bien fort pour regagner leur cosse et,\nrefermant celle-ci derrière eux, s'y endormirent de nouveau."),
        '20': Node("20. Il n'y a pas de suite, le conte est terminé."),
        '21': Node("21. Dans ce cas, le conte est également terminé.")
    }

		self.edgelist = {
		
		'1': [Edge('4', "Si oui, passez à 4."), Edge('2', "Si non, passez à 2.")],
		'2': [Edge('16', "Si oui, passez à 16."), Edge('3', "Si non, passez à 3.")],
		'3': [Edge('17', "Si oui, passez à 17."), Edge('21', "Si non, passez à 21.")],
		'4': [Edge('9', "Si vous préférez une autre description, passez à 9."), Edge('5', "Si celle-ci vous convient, passez à 5.")],
		'5': [Edge('6', "Si vous préférez qu'ils rêvent, passez à 6."), Edge('7', "Sinon, passez à 7.")],
		'6': [Edge('11', "Si vous désirez connaître ces songes, passez à 11."), Edge('7', "Si vous n'y tenez pas, passez à 7.")],
		'7': [Edge('8', "Si vous préférez des gants d'une autre couleur, passez à 8."), Edge('10', "Si cette couleur vous convient, passez à 10.")],
		'8': [Edge('7', "Si vous préférez des gants d'une autre couleur, passez à 7."), Edge('10', "Si cette couleur vous convient, passez à 10.")],
		'9': [Edge('5', "Si vous désirez connaître la suite, passez à 5."), Edge('21', "Si non, passez à 21.")],
		'10': [Edge('11', "Si vous désirez connaître leur rêve, passez à 11."), Edge('12', "Si non, passez à 12.")],
		'11': [Edge('11',"Si vous voulez savoir pourquoi ils s'éveillent d'horreur,\nconsultez le dictionnaire Larousse au mot 'ers' et n'en parlons plus."), Edge('12', "Si vous jugez inutile d'approfondir la question, passez à 12.")],
		'12': [Edge('15', "Si vous désirez connaître tout de suite l'interprétation de ce songe, passez à 15."), Edge('13', "Si vous souhaitez au contraire connaître les réactions des deux autres, passez à 13.")],
		'13': [Edge('14', "Si vous désirez aussi savoir depuis quand, passez à 14."), Edge('14', "Si non, passez à 14 tout de même, car vous ne le saurez pas plus.")],
		'14': [Edge('15', "Si vous voulez aussi voir, passez à 15."), Edge('15', "Si non, passez également à 15, car vous ne verrez rien.")],
		'15': [Edge('16', "Si vous désirez savoir ce qui se passe sur le théâtre de leurs ablutions, passez à 16."), Edge('21', "Si vous ne le désirez pas, vous passez à 21.")],
		'16': [Edge('21', "Si les trois grands échalas vous déplaisent, passez à 21."), Edge('18', "S'ils vous conviennent, passez à 18.")],
		'17': [Edge('21', "Si les trois moyens médiocres arbustes vous déplaisent, passez à 21."), Edge('18', "S'ils vous conviennent, passez à 18.")],
		'18': [Edge('19', "Si vous désirez savoir ce qu'ils firent ensuite, passez à 19."), Edge('21', "Si vous ne le désirez pas, vous passez à 21.")],
		'19': [Edge('20', "Si vous désirez connaître la suite, passez à 20."), Edge('21', "Si vous ne le désirez pas, vous passez à 21.")]
	}
		
		self.path = ['1']
	
		
	def enter(self, nodeid):
		current_node = self.nodelist[nodeid]
		current_node.describe()
		return self.get_choice(nodeid)
		
	def get_choice(self, nodeid):
		if nodeid in self.edgelist.keys():
			current_edges = self.edgelist[nodeid]
			for edge in current_edges:
				edge.describe()
			choice = 0
			while choice == 0:
				choice = raw_input()
				if choice in [e.number for e in current_edges]: 
					self.path.append(choice)
					self.enter(choice)
				else: 
					print "Ceci n'est pas un choix." 
					choice = 0
				
		else: 
			print "Voulez-vous lire un 'autre' conte, oui ou non ?"
			choice = raw_input()
			if choice == "oui":
				self.enter('1')
			else: 
				print "En ce cas, le conte est définitivement terminé."
				print self.path 
				
	def print_graph(self):
		dot = Digraph()
		dot.attr('node', shape='circle')
		dot.attr('node', style='filled')
		dot.attr('node', fillcolor='white')
		for key in self.nodelist.keys():
			if key in self.path:
				dot.attr('node', fillcolor='green')
			node = dot.node(key)
			dot.attr('node', fillcolor='white')
				
		for key in self.edgelist.keys():
			edges = self.edgelist[key]
			dot.edge(key, edges[0].number)
			dot.edge(key, edges[1].number)
	
		print dot.source
		dot.render('test-output/g.gv', view=True)
		
if __name__ == "__main__":
	g = Graph()
	g.enter('1')
	g.print_graph()