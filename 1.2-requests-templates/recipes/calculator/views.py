
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`

    pages = {
        'Рецепт омлета': reverse('omlet'),
        'Рецепт пасты': reverse('pasta'),
        'Рецепт бутера': reverse('buter')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def servings(dicts, n):
    result = {}
    for a, b in dicts.items():
        result[a] = b * n
    return result


def omlet(request):
    amount = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    if amount == 1:
        recipe = DATA['omlet']
    else:
        recipe = servings(DATA['omlet'],amount)
    context = {
         'recipe':  recipe
    }
    return render(request, template_name, context)


def pasta(request):
    amount = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    if amount == 1:
        recipe = DATA['pasta']
    else:
        recipe = servings(DATA['pasta'], amount)
    context = {
         'recipe':  recipe
    }
    return render(request, template_name, context)


def buter(request):
    amount = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    if amount == 1:
        recipe = DATA['buter']
    else:
        recipe = servings(DATA['buter'], amount)
    context = {
         'recipe':  recipe
    }
    return render(request, template_name, context)

