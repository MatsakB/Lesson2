list_of_scores = [{'school_class':'4a', 'scores':[3, 4, 4, 5, 2]},
{'school_class':'4b', 'scores':[5, 5, 3, 5, 4]},
{'school_class':'4c', 'scores':[2, 3, 3, 5, 5]},]


for avg_scores in list_of_scores:
	print(
		sum (avg_scores['scores'])/len(avg_scores['scores'])
		)