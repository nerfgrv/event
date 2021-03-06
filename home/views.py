from django.shortcuts import render
from .models import Company, Trading, Share
from users.models import User
from .forms import BidForm

def coming(request):
	return render(request, 'home/comingsoon.html')
	
def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)


def trading(request):
	# if request.method == 'POST':
	# 	form = BidForm(request.POST)
	# 	if form.is_valid():
	# 		Trading = form.save()

			# messages.success(request, f'Your account has been created! You can login now.')
	# 		return redirect('trading')

	# else:
	# form = BidForm()
	context = {
		'Tradings': Trading.objects.all(),
		'Companys': Company.objects.all()	
	}
	# print(context[trading])
	return render(request, 'home/trading.html', context)


def bidding(request):
	return render(request, 'home/letsbid.html')

def mycompanies(request):
	context = {
		'Shares': Share.objects.all(),
	}
	return render(request, 'home/mycompanies.html', context)

