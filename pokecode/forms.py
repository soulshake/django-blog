from django import forms
from .models import Pannel, Card

choices_pk = [1,2,3]
true = Pannel.objects.get(pk=choices_pk[0])
false1 = Pannel.objects.get(pk=choices_pk[2])
false2 = Pannel.objects.get(pk=choices_pk[1])


Card_QnA= {
	('true', true.name),
	('false1', false1.name),
	('false2', false2.name),
}

class CardForm(forms.Form):
	field = forms.ChoiceField(widget=forms.RadioSelect, choices=Card_QnA)
	choices = Card_QnA

	def get_true(self):
		for answer in self.choices:
			if answer[0]=='true':
				return Pannel.objects.get(name=answer[1]) #retourne un panneau