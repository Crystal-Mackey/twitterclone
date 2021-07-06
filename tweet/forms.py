from django import forms
from tweet.models import Tweet


class TweetForm(forms.ModelForm):
    tweet = forms.CharField(widget=forms.Textarea, max_length=140) #max length dictated by rubric

    class Meta:
        model = Tweet
        fields = ['tweet']
        exclude = ['time', 'user']