from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Entry
from django.contrib.auth.models import User
from .workout_query import aver, workout_to_calendar


class Calendario(HTMLCalendar):
	def __init__(self, user, year=None, month=None):
		self.year = year
		self.month = month
		self.user= user
		super(Calendario, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(date__day=day)

		d = ''
		if day == 0: 
			pass

		else :
			if workout_to_calendar(day, self.month, self.year):
				#print('received true for ' + str(day) + str(self.month) + str(self.year))
				
				if self.month < 10: 
					month = str('0')+ str(self.month)
				else: 
					month = self.month
				if day < 10: day_string = str('0')+ str(day) 

				d += f'<a href=" workout/{self.year}-{month}-{day} "> workout day</a><br>'
				for event in events_per_day:
					if str(event.get_username) == self.user:
						d += f' {event.get_html_url}<br>'
			else: 
				for event in events_per_day:
					if str(event.get_username) == self.user:
						d += f' {event.get_html_url}<br>' 
			#elif (Workout.objects.extra(select={'day': 'date( date )'}).values('day').annotate(available=Count('date'))):
			#	d += f' Workout <br>' 
			#d += ' {event.language} + {event.id} '
		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Entry.objects.filter(date__year=self.year, date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal