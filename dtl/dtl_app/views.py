from django.shortcuts import render

# Create your views here.
def practice_dt1(request):
    context = {
        'name':'Habib',
        'no_of_messages':5,
        'messages':['hello','free to chat','when can we talk'],
        'is_logged_in':True
    }
    return render(request,'dtl_app/practice_dtl.html',context=context)