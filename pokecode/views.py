from django.shortcuts import render, get_object_or_404
from .models import Pannel, Card
from .forms import CardForm

# Create your views here.

wins=0

def quiz(request): #------ NO DJANGO FORMS
	if request=="POST":
		message="POST = sent"
		return render(request,'/', {'choices':choices,'Card':newCard,'message':message})
	else:
		pannels = Pannel.objects.all() #crée l'objet liste de posts à partir du modèle Post

		choices_pk = [1,2,3]
		true = Pannel.objects.get(pk=choices_pk[0])
		false1 = Pannel.objects.get(pk=choices_pk[2])
		false2 = Pannel.objects.get(pk=choices_pk[1]) #picks up 3 Pannels into a newCard
		"""newCard = Card(true=true)
		newCard.save()
		newCard.falsees.add(false1,false2)
		choices = [newCard.true.name]
		for false in newCard.falsees.all():
			choices.append(false.name)"""
		choices = [true.name, false1.name, false2.name]
		return render(request,'pokecode/quiz_sans_form.html', {'choices':choices, 'true':true})
			#'Card':newCard}

"""def quiz(request): #------ USING DJANGO FORMS
	if request=='POST':
		form = CardForm(request.POST)
		truePannel = form.get_true() #right answer
		if form.is_valid():
			data = form.cleaned_data() #genre pour avoir la première réponse donnée
			inputPannel = Pannel.objects.get(name=data)
			if inputPannel == truePannel:
				wins+=1
				context = {
				#'Card': newCard, 'choices': choices,
				'form':form, 'truePannel':truePannel,
				'data':data}
				return render(request,'pokecode/quiz.html', context)
	else:
		form = CardForm()
		truePannel = form.get_true()
		context = {
		#'Card': newCard, 'choices': choices,
		'form':form, 'truePannel':truePannel}
		return render(request,'pokecode/quiz.html', context)"""
