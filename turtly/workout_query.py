from datetime import datetime, timedelta
from .models import Workout
from django.db.models import Count

def aver(obju):
	DIA = ''
	first_enter = True
	my_context= []
	print(obju)
	print('este es el 1')
	for objeto in obju:
		dia= str(objeto)
		if first_enter== True:
			DIA= dia
		#if dia ==! DIA:


		print(me[:10])

def workout_to_calendar(day, month, year):
	datik = datetime.date(datetime(year, month, day))
	#item= Workout.objects.extra(select={'day': 'date(date)'}).values('day').annotate(available=Count('date'))
	item = Workout.objects.extra(select={'day': 'date(date)'}).values('day').annotate(available=Count('date'))
	for items in item:
		if str((items['day'])) == str(datik):
			#print(items['day'] + 'is equal to ' + str(datik))
			return(True)


def workout_get_dates():
	Values= {}
	context_proto= []
	list_empty = True
	posts_combined= Workout.objects.extra(select={'day': 'date(date)'}).values('day').annotate(available=Count('date'))

	for post in posts_combined:
		first = ' '
		if list_empty:
			first= str(post['day'])[:10]
			Values['date']= first
			context_proto.append(Values.copy())
			list_empty = False
			Values= {}
		else:
			if str(post['day'])[:10] != first:
				Values['date']= str(post['day'])[:10]
				context_proto.append(Values.copy())
	Values.clear()
	return workout_to_post(context_proto)

def workout_to_post(context_proto):
	Values= {}
	context_novo = []
	posts= Workout.objects.all()

	for context in context_proto:
		Values['date']= context['date']
		#print('this is the context: ' + str(context))
		for post in posts:
			print(str(context['date']))
			if str(post.date)[:10] == str(context['date']):
				print(str(post.date)[:10] == str(context['date']))
				#print(post + 'time is not eqaul to ' + str(context['date'])
				if str(post.BACK_EX) != '':
					Values[str(post.BACK_EX)]= str(post.AMOUNT)
				if str(post.CHEST_EX) != '':
					Values[str(post.CHEST_EX)]= str(post.AMOUNT)
				if str(post.ARM_EX) != '':
					Values[str(post.ARM_EX)]= str(post.AMOUNT)
				if str(post.LEG_EX) != '':
					Values[str(post.LEG_EX)]= str(post.AMOUNT)

		context_novo.append(Values)
		Values = {}
	print(context_novo)
	return(context_novo)







	