from django.shortcuts import render,redirect
from .models import Question

# Create your views here.

def exam(request):
	response = {}
	response["questions"] = Question.objects.all()
	if request.method == "POST":
		score = 0
		answer = {}
		questions = Question.objects.all()
		for qes in questions:
			answer[str(qes.pk)] =  request.POST[str(qes.pk)]
			if qes.answer == request.POST[str(qes.pk)]:
				score+=1
			response["answer"] = answer
		print(score)
	return render(request, "quiz/exam.html", response)
