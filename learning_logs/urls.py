"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 显示特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
    #用于添加middle条目的页面
    path('new_entry_middle/<int:topic_id>/',views.new_entry_middle,name='new_entry_middle'),
    #用于添加end条目的页面
    path('new_entry_end/<int:topic_id>/',views.new_entry_end,name='new_entry_end'),
    # 用于编辑middle条目的页面
    path('edit_entry_middle/<int:entry_id>/', views.edit_entry_middle, name='edit_entry_middle'),
    # 用于编辑end条目的页面
    path('edit_entry_end/<int:entry_id>/', views.edit_entry_end, name='edit_entry_end'),
]

