import random


capitals = {'Alabama':'Montgomery', 
			'vAlabama':'Montgomery',
			'Alaska':'Juneau',
			'Arizona':'Phoenix',
			'Arkansas':'Little rock',
			'California':'Sacramento',
			'Colorado':'Denver',
			'Connecticut':'Hartford',
			'Delaware':'Dover',
			'Florida':'Tallahassee',
			'Georgia':'Atlanta',
			'Hawaii':'Honolulu',
			'Idaho':'Boise',
			'Illinois':'Springfield',
			'Indiana':'Indianapolis',
			'Iowa':'Des Moines',
			'Kansas':'Topeka',
			'Kentucky':'Frankfort',
			'Louisiana':'Baton Rouge',
			'Maine':'Augusta',
			'Maryland':'Annapolis',
			'Massachusetts':'Boston',
			'Michigan':'Lansing',
			'Minnesota':'St. Paul',
			'Mississippi':'Jackson',
			'Missouri':'Jefferson City',
			'Montana':'Helena',
			'Nebraska':'Lincoln',
			'Nevada':'Carson City',
			'New hampshire':'Concord',
			'New jersey':'Trenton',
			'New mexico':'Santa Fe',
			'New York':'Albany',
			'North Carolina':'Raleigh',
			'North Dakota':'Bismarck',
			'Ohio':'Columbus',
			'Oklahoma':'Oklahoma City',
			'Oregon':'Salem',
			'Pennsylvania':'Harrisburg',
			'Rhode island':'Providence',
			'South carolina':'Columbia',
			'South dakota':'Pierre',
			'Tennessee':'Nashville',
			'Texas':'Austin',
			'Utah':'Salt Lake City',
			'Vermont':'Montpelier',
			'Virginia':'Richmond',
			'Washington':'Olympia',
			'West Virginia':'Charleston',
			'Wisconsin':'Madison',
			'Wyoming':'Cheyenne'}
			
for quizNum in range(35):
	quizFile = open('capitalsquiz%s.txt' % (quizNum +1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' '*20) + 'State Capitals Quiz (From %s)' % (quizNum + 1))
	quizFile.write('\n\n')
	states = list(capitals.keys())
	random.shuffle(states)
	
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		
		quizFile.write('%s. What is the capital of %s? \n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
