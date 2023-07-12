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


def gt(request):
    return render(request,"gt.html")

def robtech(request):
    return render(request,"robtech.html")

def demo1(request):
    return render(request,"demo1.html")

def demo2(request):
    return render(request,"demo2.html")