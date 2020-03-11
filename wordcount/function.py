# from django.http import HttpResponse
from django.shortcuts import render

# 获取用户请求，传达index.html
def home(request):
    return render(request, 'index.html')

def count(request):
    # get方式获取文本
    user_text = request.GET['text']     # 文本
    total_count = len(request.GET['text'])  # 字数
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)
    return render(request, 'count.html',
        {'count': total_count,
        'text': user_text,
        'worddict': word_dict,
        'sorteddict': sorted_dict})

def about(request):
    return render(request, 'about.html')