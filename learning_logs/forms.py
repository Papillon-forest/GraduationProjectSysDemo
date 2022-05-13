from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'key_days', 'rating_5', 'rating_4', 'rating_3', 'rating_2', 'rating_1', 'rating_average',
                  'positive_percent']
        labels = {'text': '请输入日期等相关文本信息：',
                  'key_days': '请输入第几天（1，2，3，4，5，6，7，14，30）：',
                  'rating_5': '请输入当天五星级占比：（0～1） 如0.53333',
                  'rating_4': '请输入当天四星级占比：（0～1） 如0.53333',
                  'rating_3': '请输入当天三星级占比：（0～1） 如0.53333',
                  'rating_2': '请输入当天二星级占比：（0～1） 如0.53333',
                  'rating_1': '请输入当天一星级占比：（0～1） 如0.53333',
                  'rating_average': '请输入当天星级平均得分：（0～5） 如4.35',
                  'positive_percent': '请输入当天用户评论积极程度占比：（0～1） 如0.53333',
                  }
        # widgets = {'text': forms.Textarea(attrs={'cols': 80}),
        #            'key_days': forms.IntegerField(max_value=30,min_value=1),
        #            'rating_5': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'rating_4': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'rating_3': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'rating_2': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'rating_1': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'rating_average': forms.DecimalField(max_digits=11,decimal_places=10),
        #            'positive_percent': forms.DecimalField(max_digits=11,decimal_places=10),
        #            }
