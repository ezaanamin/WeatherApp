from django.shortcuts import render
def home(request):
    import json
    import requests
    if request.method=='POST':
      name=request.POST.get('name',False)
    a=requests.get('http://api.openweathermap.org/data/2.5/find?q='+str(name)+'&units=metric&appid=568f8ba2f7979b2c271e1197f38dce73')

    try:
        api = json.loads(a.content)
    except Exception as e:
        api = "Error...."

    return render(request,'weatherapp/home.html',{'api':api})


def about(request):
    return render(request,'weatherapp/about.html')

