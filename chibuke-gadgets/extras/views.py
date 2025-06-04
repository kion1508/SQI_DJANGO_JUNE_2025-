from django.shortcuts import render, HttpResponse

# Create your views here.
def extras(request):
    return HttpResponse('''<div>Phone (Fonu): Your daily driver for calls, chats, internet,and snapping pictures.<br>
Television (TV): Where we dey watch film, news, and football.<br>
Computer (Kompúta): For work, school, games, and research.<br>
Fridge (Friji): Keeps your food and drinks cold and fresh.<br>
Fan: Gives you sweet breeze when the weather hot.<br>
Charger & Power Bank: Essential for keeping your phone on.</div>''')