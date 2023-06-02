from django.shortcuts import render

def blog(request):
    print('blog')
    return render(
        request, 
        'blog/index.html'
    )