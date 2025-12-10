from django.shortcuts import render

def formula(request):
    power = None

    if request.method == "POST":
        I = float(request.POST.get("INTENSITY"))
        R = float(request.POST.get("RESISTANCE"))
        power = I * I * R  # Formula P = I²R

    return render(request, "mathapp/science.html", {"power": power})