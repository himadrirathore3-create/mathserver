# Ex.05 Design a Website for Server Side Processing
# Date:28/11/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
    <title>power formula </title>
    <style>
        body {
            background :linear-gradient(rgb(111, 190, 219),rgb(168, 120, 190));
            background-size: cover;
            background-repeat: top left;
            background-attachment: fixed;
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            display: inline-block;
            width: 150px;
        }
        input {
            margin-bottom: 10px;
        }
        button {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h2>Power of Lamp Filament</h2>

    <label>Intensity (I): </label>
    <input type="number" id="INTENSITY"><br><br>

    <label>Resistance (R): </label>
    <input type="number" id="RESISTANCE"><br><br>

    <button onclick="calculatePower()">Calculate Power</button>

    <h3 id="result"></h3>

    <script>
        function calculatePower() {
            let I = Number(document.getElementById("INTENSITY").value);
            let R = Number(document.getElementById("RESISTANCE").value);

            let P = I * I * R; 

            document.getElementById("result").innerHTML = "Power = " + P + " watts";
        }
    </script>
    
</body>
</html>
```
```
urls.py

from django.urls import path
from mathapp import views

urlpatterns= [path('admin/', admin.site.urls),
path('',views.formula,name='formula'),]
```
```
views.py

from django.shortcuts import render

def formula(request):
    power = None

    if request.method == "POST":
        I = float(request.POST.get("INTENSITY"))
        R = float(request.POST.get("RESISTANCE"))
        power = I * I * R  # Formula P = I²R

    return render(request, "mathapp/science.html", {"power": power})
```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-12-10 210042.png>)
# HOMEPAGE:
![alt text](<Screenshot 2025-12-10 205824.png>)
# RESULT:
The program for performing server side processing is completed successfully.
