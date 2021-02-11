"""
Andrew Newton
Jan. Winter 2021
Appointments
Week 1
"""

from datetime import datetime


class Agenda:
	"""An Agenda is a collection of appointments,
	    similar to a list.

	    Usage:
	    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
	    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")

	    agenda = Agenda()
	    agenda.append(appt1)
	    agenda.append(appt2)
	    ag_conflicts = agenda.conflicts()

	    if len(ag_conflicts) == 0:
	        print(f"Agenda has no conflicts")
	    else:
	        print(f"In agenda:\n{agenda.text()}")
	        print(f"Conflicts:\n {ag_conflicts}")

	    Expected output:
	    In agenda:
	    2018-03-15 13:30 15:30 | Early afternoon nap
	    2018-03-15 15:00 16:00 | Coffee break
	    Conflicts:
	    2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
	    """

	def __init__(self):
		self.elements = [ ]

	def __eq__(self, other: 'Agenda') -> bool:
		"""Delegate to __eq__ (==) of wrapped lists"""
		return self.elements == other.elements

	def __str__(self):
		'''String representation of an Agenda'''
		lines = [str(e) for e in self.elements]
		return "\n".join(lines)

	def __len__(self):
		'''Length of an Agenda'''
		return len(self.elements)

	def append(self, var):
		self.elements.append(var)

	def sort(self):
		self.elements.sort(key=lambda appt: appt.start)

	def conflicts(self) -> "Agenda":
		'''Searches through an Agenda comparing Appts'''
		self.sort() #SORT TO MAKE IT EASIER TO COMPARE TIMES OF APPTS
		conflicts_agenda = Agenda()

		for i in range(0, len(self)): #FIRST APPT I COMPARED TO NEXT APPT X

			for x in range(i+1, len(self)): #COMPARE TO APPT I

				if self.elements[i].overlaps(self.elements[x]): #USE OVERLAPS FROM APPT CLASS

					conflict_appt = self.elements[i].intersect(self.elements[x]) #INTERSECT GIVES US THE APPT WE WANT

					conflicts_agenda.append(conflict_appt)
				else:
					break

		return conflicts_agenda


class Appt:
	"""
	An appointment has a start time, an end time, and a title.
	The start and end time should be on the same day.
	Usage example:
	appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
	appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
	if appt2 > appt1:
		print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
	elif appt1.overlaps(appt2):
		print("Oh no, a conflict in the schedule!")
		print(appt1.intersect(appt2))
	Should print:
		Oh no, a conflict in the schedule!
		2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
	"""
	def __init__(self, start: datetime, finish: datetime, desc: str):
		"""An appointment from start time to finish time, with description desc.
		Start and finish should be the same day.
		"""
		assert finish > start, f"Period finish ({finish}) must be after start ({start})"
		self.start = start
		self.finish = finish
		self.desc = desc 

	def __lt__(self, other: 'Appt') -> bool:
		'''APPT1 IS BEFORE APPT2 IF APPT1 ENDS BEFORE APPT2 STARTS '''
		return self.finish <= other.start
		
	def __gt__(self, other: 'Appt') -> bool:
		'''APPT1 IS AFTER APPT2 IF APPT1 STARTS AFTER APPT2 ENDS '''
		return self.start >= other.finish

	def __eq__(self, other: 'Appt') -> bool:
		return (self.start == other.start) and (self.finish == other.finish)

	def __str__(self) -> str:
		"""The textual format of an appointment is
		yyyy-mm-dd hh:mm hh:mm  | description
		Note that this is accurate only if start and finish
		are on the same day.
		"""

		date_iso = self.start.date().isoformat()
		start_iso = self.start.time().isoformat(timespec='minutes')
		finish_iso = self.finish.time().isoformat(timespec='minutes')
		return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

	def __repr__(self) -> str:
		return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"


	def overlaps(self, other: 'Appt') -> bool:
		"""Is there a non-zero overlap between these periods?"""
		if ((self < other) or (self > other)) and (self != other):
			return False #IF APPT1 IS BEFORE OR AFTER APPT2 AND THEY'RE NOT EQUAL THEN THEY DO NOT OVERLAP
		else:
			return True


	def intersect(self, other: 'Appt') -> 'Appt':
		"""The overlapping portion of two Appt objects"""
		assert self.overlaps(other)

		intersect_start = max(self.start, other.start)

		intersect_finish = min(self.finish, other.finish)

		intersect_desc = ("| " + self.desc + " and " + other.desc)

		ap = Appt(intersect_start, intersect_finish, intersect_desc)

		return ap


if __name__ == '__main__':
	print("Running usage examples")

	appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
	appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")

	if appt2 > appt1:
		print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")

	elif appt1.overlaps(appt2):
		print("Oh no, a conflict in the schedule!")
		print(appt1.intersect(appt2))

	agenda = Agenda()
	agenda.append(appt1)
	agenda.append(appt2)
	ag_conflicts = agenda.conflicts()

	if len(ag_conflicts) == 0:
		print(f"Agenda has no conflicts")
	else:
		print(f"In agenda:\n{agenda}")
		print(f"Conflicts:\n {ag_conflicts}")