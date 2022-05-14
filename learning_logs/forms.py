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
        fields = ['text', 'key_days', 'last_retention', 'rating_5', 'rating_4', 'rating_3', 'rating_2', 'rating_1',
                  'rating_average',
                  'positive_percent']
        labels = {'text': '请输入日期等相关文本信息：',
                  'key_days': '月初：',
                  'last_retention': '请输入前一天的真实用户留存率：（0～1） 如0.381',
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


class EntryMiddleForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'key_days_middle', 'retention_1_middle', 'retention_2_middle', 'retention_3_middle', 'retention_4_middle', 'retention_5_middle',
                  'retention_6_middle', 'retention_7_middle']
        labels = {'text': '请输入日期等相关文本信息：',
                  'key_days_middle': '月中：',
                  'retention_1_middle': '请输入第一天的真实用户留存率：（0～1） 如0.381',
                  'retention_2_middle': '请输入第二天的真实用户留存率：（0～1） 如0.381',
                  'retention_3_middle': '请输入第三天的真实用户留存率：（0～1） 如0.381',
                  'retention_4_middle': '请输入第四天的真实用户留存率：（0～1） 如0.381',
                  'retention_5_middle': '请输入第五天的真实用户留存率：（0～1） 如0.381',
                  'retention_6_middle': '请输入第六天的真实用户留存率：（0～1） 如0.381',
                  'retention_7_middle': '请输入第七天的真实用户留存率：（0～1） 如0.381',

                  }


class EntryEndForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'key_days_end', 'retention_1_end', 'retention_2_end', 'retention_3_end', 'retention_4_end', 'retention_5_end',
                  'retention_6_end', 'retention_7_end', 'retention_8_end']
        labels = {'text': '请输入日期等相关文本信息：',
                  'key_days_end': '月末：',
                  'retention_1_end': '请输入第一天的真实用户留存率：（0～1） 如0.381',
                  'retention_2_end': '请输入第二天的真实用户留存率：（0～1） 如0.381',
                  'retention_3_end': '请输入第三天的真实用户留存率：（0～1） 如0.381',
                  'retention_4_end': '请输入第四天的真实用户留存率：（0～1） 如0.381',
                  'retention_5_end': '请输入第五天的真实用户留存率：（0～1） 如0.381',
                  'retention_6_end': '请输入第六天的真实用户留存率：（0～1） 如0.381',
                  'retention_7_end': '请输入第七天的真实用户留存率：（0～1） 如0.381',
                  'retention_8_end': '请输入第十四天的真实用户留存率：（0～1） 如0.381',
                  }