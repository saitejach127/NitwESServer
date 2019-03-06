from django.shortcuts import render
from .models import Question

# Create your views here.

def exam(request):
	response = {}
	response["questions"] = Question.objects.all()
	return render(request, "quiz/exam.html", response)

def evaluate(request):
	response = {}
	if request.method == "POST":
		score = 0
		questions = Question.objects.all()
		for qes in questions:
			if qes.answer == request.POST[str(qes.pk)]:
				score+=1
		print(score)
	return render(request, "quiz/evaluate.html")
