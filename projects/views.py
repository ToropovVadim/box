from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, "project/index.html")


publications_data = [
    {
        'name': 'статья круть!',
        'date': datetime.now(),
        'text': '''Hello! This is a generator for text fonts of the "cool" variety. I noticed people were trying to find a generator like fancy letters, but were ending up on actual font sites rather than generators of copy-paste text like this one. So currently this is basically a duplicate of the above, but I think I'll try to collect a few more "cool" text fonts, like the old enlgish one, and specialise this a bit.
               <br> <br> If you're wondering how one produces cool text fonts like you see above, it's fairly simple (but maybe not what you'd expect). Basically, the text that gets generated isn't actually a font - it's a bunch of symbols that are in the unicode standard. You're reading symbols that are in the unicode standard right now - the alphabet is a part of it, as are all the regular symbols on your keyboard: !@#$%^&*() etc.'''

    },
    {
        'name': 'статья вторая вооще круть!',
        'date': datetime.now(),
        'text': '''Hello! This is a generator for text fonts of the "cool" variety. I noticed people were trying to find a generator like fancy letters, but were ending up on actual font sites rather than generators of copy-paste text like this one. So currently this is basically a duplicate of the above, but I think I'll try to collect a few more "cool" text fonts, like the old enlgish one, and specialise this a bit.
               <br> <br> If you're wondering how one produces cool text fonts like you see above, it's fairly simple (but maybe not what you'd expect). Basically, the text that gets generated isn't actually a font - it's a bunch of symbols that are in the unicode standard. You're reading symbols that are in the unicode standard right now - the alphabet is a part of it, as are all the regular symbols on your keyboard: !@#$%^&*() etc.'''
    }
]


def index_tests(request):
    return render(request, 'index_tests.html', publications_data[0])


def index_test(request):
    return render(request, 'index_test.html', publications_data[1])
