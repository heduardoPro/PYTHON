from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog'
    }

    return render(
        request,
        'blog/index.html',
        context,
    )
