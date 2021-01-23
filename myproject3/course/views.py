from django.shortcuts import render
# Create your views here.
def learn_django(request):
    data = {'stu1': {'Name': 'Vivek', 'Id': 101},
           'stu2': {'Name': 'Aneel', 'Id': 102},
           'stu3': {'Name': 'Rajesh', 'Id': 103},
           'stu4': {'Name': 'Santosh', 'Id': 104},
           }
    
    return render(request, 'course/courseone.html', {'data': data})

def learn_python(request):
    return render(request, 'course/coursetwo.html')