from django.shortcuts import render,redirect
from .models import Question,ExamTime	
import datetime

def exam(request):
	time = ExamTime.objects.all()[0]
	print(time.time)
	print(datetime.datetime.now())
	response = {}
	questions = Question.objects.all()
	response["questions"] = questions	
	if request.method == "POST":
		score = 0
		answer = []
		for qes in questions:
			r = {}
			r['correct'] = False
			r['ans'] = request.POST[str(qes.pk)]
			if qes.answer == request.POST[str(qes.pk)]:
				r['correct'] = True
				score+=1
			answer.append(r)
		response["answer"] = answer
		response["zipped"] = zip(questions,answer)
	return render(request, "quiz/exam.html", response)
