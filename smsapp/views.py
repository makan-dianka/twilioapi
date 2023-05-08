from django.shortcuts import render

def sendsms(request):
    if request.method=='POST':
        print(request.POST)
    return render(request, 'smsapp/smspage.html')
