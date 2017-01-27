from django import forms

class ReviewForm(forms.Form):

    is_favorite = forms.BooleanField(
        label='Favorite?',
        help_text='In your top 100 books of all time?',
        required=False,
    )

    review = forms.CharField(
        widget=forms.Textarea,
        min_length=300,
        error_messages={
            'required': 'Please enter your review',
            'min_length': 'Please write at least 300 characters (you have written %(show_value)s)'
        }
    )