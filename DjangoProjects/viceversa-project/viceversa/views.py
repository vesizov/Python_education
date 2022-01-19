from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def reverse(request):
	user_text = request.GET['user_text']
	reversed_text = user_text[::-1]
	words_amount = len(user_text.split())
	return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text, 'words_amount': words_amount})


# its getting hard