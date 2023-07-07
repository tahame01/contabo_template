from django.shortcuts import render


def main(request):
    return render(request,"main.html")

def test(request):
    return render(request,"test.html")

def afra(request):
    return render(request,"afra.html")

def dessert(request):
    return render(request,"dessert.html")

def ba_properties(request):
    return render(request,"ba_properties.html")
