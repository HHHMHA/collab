from django import forms

from comment.models import Comment
from task.models import Task


class TaskUpdateForm(forms.ModelForm):
    comment = forms.CharField(max_length=255, required=False,
                              widget=forms.Textarea(
                                  attrs={"class": "form-control", "placeholder": "Your Comment"}

                              ),
                              )

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update(
            {
                'placeholder': 'Your Comment',
            }
        )

    class Meta:
        model = Task
        fields = ['status', 'upload', 'comment']

    def save(self, commit=True):
        task = super(TaskUpdateForm, self).save(commit=False)
        if self.cleaned_data['comment'] != "" and commit:
            Comment.objects.create(task=self.instance, comment=self.cleaned_data['comment'])
        if commit:
            task.save()
        return task
