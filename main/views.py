from django.shortcuts import render

# db_temp = [
#     ('plushie1', 'Hitagi Plushie', '400000', 'Koyo koyooo'),
#     ('plushie2', 'Suruga Plushie', '400000', 'I love my senpai'),
#     ('plushie3', 'Karen Plushie', '500000', 'Asta la vistaaa'),
#     ('plushie4', 'Hanekawa Plushie', '550000', 'i don\'t know everything i just know what i know'),
#     ('plushie5', 'Shinobu Plushie', '450000', 'ka..ka.. >_<'),
#     ('plushie6', 'Nadeko Plushie', '400000', 'Koyomi-onichan'),
#     ('plushie7', 'Mayoi Plushie', '450000', 'Sorry I stuttered, Arararagi-san'),
# ]

def show_main(request):
    context = {
        'npm' : '2306216636',
        'name': 'Muhammad Raihan Maulana',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
