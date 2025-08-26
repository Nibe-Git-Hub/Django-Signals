from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import TweetForm

# Create your views here.

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(reverse('create_tweet'))  # Change to a URL of your choice
    else:
        form = TweetForm()

    return render(request, 'Tweets/create_tweet.html', {'form': form})