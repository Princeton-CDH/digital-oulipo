# -*- coding: utf-8 -*-

from datetime import date
from datetime import time
from datetime import datetime

import uuid
import math
import subprocess

class Corpus:
    
    poems = [   
     
[u'From fairest creatures we desire increase,',  # Sonnet 1: http://www.nosweatshakespeare.com/sonnets/1/
u'That thereby beauty’s rose might never die,',
u'But as the riper should by time decrease,',
u'His tender heir mught bear his memeory:',
u'But thou, contracted to thine own bright eyes,',
u'Feed’st thy light’st flame with self-substantial fuel,',
u'Making a famine where abundance lies,',
u'Thyself thy foe, to thy sweet self too cruel.',
u'Thou that art now the world’s fresh ornament',
u'And only herald to the gaudy spring,',
u'Within thine own bud buriest thy content',
u'And, tender churl, makest waste in niggarding.',
u'Pity the world, or else this glutton be,',
u'To eat the world’s due, by the grave and thee.'],
     
[u'Lo! in the orient when the gracious light', # Sonnet 7: http://www.nosweatshakespeare.com/sonnets/7/
u'Lifts up his burning head, each under eye',
u'Doth homage to his new-appearing sight,',
u'Serving with looks his sacred majesty;',
u'And having climb’d the steep-up heavenly hill,',
u'Resembling strong youth in his middle age,',
u'yet mortal looks adore his beauty still,',
u'Attending on his golden pilgrimage;',
u'But when from highmost pitch, with weary car,',
u'Like feeble age, he reeleth from the day,',
u'The eyes, ‘fore duteous, now converted are',
u'From his low tract and look another way:',
u'So thou, thyself out-going in thy noon,',
u'Unlook’d on diest, unless thou get a son.'],

[u'For shame deny that thou bear’st love to any,', # Sonnet 10: http://www.nosweatshakespeare.com/sonnets/10/
u'Who for thy self art so unprovident.',
u'Grant, if thou wilt, thou art beloved of many,',
u'But that thou none lov’st is most evident:',
u'For thou art so possessed with murderous hate,',
u'That ‘gainst thy self thou stick’st not to conspire,',
u'Seeking that beauteous roof to ruinate',
u'Which to repair should be thy chief desire.',
u'O! change thy thought, that I may change my mind:',
u'Shall hate be fairer lodged than gentle love?',
u'Be, as thy presence is, gracious and kind,',
u'Or to thyself at least kind-hearted prove:',
u'Make thee another self for love of me,',
u'That beauty still may live in thine or thee.'],

[u'Where art thou Muse that thou forget’st so long,', # Sonnet 100: http://www.nosweatshakespeare.com/sonnets/100/
u'To speak of that which gives thee all thy might?',
u'Spend’st thou thy fury on some worthless song,',
u'Darkening thy power to lend base subjects light?',
u'Return forgetful Muse, and straight redeem,',
u'In gentle numbers time so idly spent;',
u'Sing to the ear that doth thy lays esteem',
u'And gives thy pen both skill and argument.',
u'Rise, resty Muse, my love’s sweet face survey,',
u'If Time have any wrinkle graven there;',
u'If any, be a satire to decay,',
u'And make time’s spoils despised every where.',
u'Give my love fame faster than Time wastes life,',
u'So thou prevent’st his scythe and crooked knife.'],

[u'O truant Muse what shall be thy amends', # Sonnet 101: http://www.nosweatshakespeare.com/sonnets/101/
u'For thy neglect of truth in beauty dyed?',
u'Both truth and beauty on my love depends;',
u'So dost thou too, and therein dignified.',
u'Make answer Muse: wilt thou not haply say,',
u'Truth needs no colour, with his colour fixed;',
u'Beauty no pencil, beauty’s truth to lay;',
u'But best is best, if never intermixed?',
u'Because he needs no praise, wilt thou be dumb?',
u'Excuse not silence so, for’t lies in thee',
u'To make him much outlive a gilded tomb',
u'And to be praised of ages yet to be.',
u'Then do thy office, Muse; I teach thee how', 
u'To make him seem, long hence, as he shows now.'],
     
[u'My love is strengthened, though more weak in seeming;', # Sonnet 102: http://www.nosweatshakespeare.com/sonnets/102/
u'I love not less, though less the show appear;',
u'That love is merchandized, whose rich esteeming,',
u'The owner’s tongue doth publish every where.',
u'Our love was new, and then but in the spring,',
u'When I was wont to greet it with my lays;',
u'As Philomel in summer’s front doth sing,',
u'And stops his pipe in growth of riper days:',
u'Not that the summer is less pleasant now',
u'Than when her mournful hymns did hush the night,',
u'But that wild music burthens every bough,',
u'And sweets grown common lose their dear delight.',
u'Therefore like her, I sometime hold my tongue:',
u'Because I would not dull you with my song.'],

[u'Alack! what poverty my Muse brings forth,', # Sonnet 103: http://www.nosweatshakespeare.com/sonnets/103/
u'That having such a scope to show her pride,',
u'The argument all bare is of more worth',
u'Than when it hath my added praise beside!',
u'O! blame me not, if I no more can write!',
u'Look in your glass, and there appears a face',
u'That over-goes my blunt invention quite,',
u'Dulling my lines, and doing me disgrace.',
u'Were it not sinful then, striving to mend,',
u'To mar the subject that before was well?',
u'For to no other pass my verses tend',
u'Than of your graces and your gifts to tell;',
u'And more, much more, than in my verse can sit,',
u'Your own glass shows you when you look in it.'],
     
[u'To me, fair friend, you never can be old,', # Sonnet 104: http://www.nosweatshakespeare.com/sonnets/104/
u'For as you were when first your eye I ey’d,',
u'Such seems your beauty still. Three winters cold,'
u'Have from the forests shook three summers’ pride,'
u'Three beauteous springs to yellow autumn turn’d,',
u'In process of the seasons have I seen,',
u'Three April perfumes in three hot Junes burn’d,',
u'Since first I saw you fresh, which yet are green.',
u'Ah! yet doth beauty like a dial-hand,',
u'Steal from his figure, and no pace perceiv’d;',
u'So your sweet hue, which methinks still doth stand,',
u'Hath motion, and mine eye may be deceiv’d:',
u'For fear of which, hear this thou age unbred:',
u'Ere you were born was beauty’s summer dead.'],
     
[u'Let not my love be called idolatry,', # Sonnet 105: http://www.nosweatshakespeare.com/sonnets/105/
u'Nor my beloved as an idol show,',
u'Since all alike my songs and praises be',
u'To one, of one, still such, and ever so.', 
u'Kind is my love to-day, to-morrow kind,',
u'Still constant in a wondrous excellence;',
u'Therefore my verse to constancy confined,',
u'One thing expressing, leaves out difference.',
u'Fair, kind, and true, is all my argument,',
u'Fair, kind, and true, varying to other words;',
u'And in this change is my invention spent,',
u'Three themes in one, which wondrous scope affords.',
u'Fair, kind, and true, have often lived alone,',
u'Which three till now, never kept seat in one.'],
     
[u'When in the chronicle of wasted time', # Sonnet 106: http://www.nosweatshakespeare.com/sonnets/106/
u'I see descriptions of the fairest wights,',
u'And beauty making beautiful old rhyme,',
u'In praise of ladies dead and lovely knights,',
u'Then, in the blazon of sweet beauty’s best,',
u'Of hand, of foot, of lip, of eye, of brow,',
u'I see their antique pen would have express’d',
u'Even such a beauty as you master now.',
u'So all their praises are but prophecies',
u'Of this our time, all you prefiguring;',
u'And for they looked but with divining eyes,',
u'They had not skill enough your worth to sing:',
u'For we, which now behold these present days,',
u'Have eyes to wonder, but lack tongues to praise.']     
]

    def begin(self): 
		print "Would you like to read one of Shakespeare's original sonnets? If yes, type 1."
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