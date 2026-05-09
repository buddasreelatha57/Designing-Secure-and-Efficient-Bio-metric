from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import os
import base64


# ================= GLOBAL VARIABLES ================= #

username = ""
password = ""
contact = ""
gender = ""
email = ""
address = ""
finger = ""


# ================= HOME PAGES ================= #

def index(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, 'UserLogin.html')


def Signup(request):
    return render(request, 'Signup.html')


def Upload(request):
    return render(request, 'Upload.html')


def ValidateFace(request):
    return render(request, 'ValidateFace.html')


# ================= FILE DOWNLOAD ================= #

def DownloadFileAction(request):

    img = request.GET.get('fname')

    if not img:
        return HttpResponse("No filename provided")

    filepath = os.path.join(
        "SecureBiometricApp/static/files",
        img
    )

    if os.path.exists(filepath):

        with open(filepath, 'rb') as infile:
            data = infile.read()

        response = HttpResponse(
            data,
            content_type='application/octet-stream'
        )

        response[
            'Content-Disposition'
        ] = f'attachment; filename="{img}"'

        return response

    return HttpResponse("File not found")


def Download(request):

    output = """
    <table border="1" align="center" width="100%">
    <tr>
    <th>Filename</th>
    <th>Download</th>
    </tr>
    """

    folder = "SecureBiometricApp/static/files"

    os.makedirs(folder, exist_ok=True)

    for file in os.listdir(folder):

        output += f"""
        <tr>
        <td>{file}</td>
        <td>
        <a href='/DownloadFileAction?fname={file}'>
        Download
        </a>
        </td>
        </tr>
        """

    output += "</table>"

    context = {'data': output}

    return render(request, "Download.html", context)


# ================= FILE UPLOAD ================= #

def UploadAction(request):

    if request.method == 'POST':

        try:

            file = request.FILES['t1']

            filename = file.name

            save_path = 'SecureBiometricApp/static/files/'

            os.makedirs(save_path, exist_ok=True)

            fs = FileSystemStorage(location=save_path)

            fs.save(filename, file)

            context = {
                'data': f'{filename} uploaded successfully'
            }

            return render(request, 'Upload.html', context)

        except Exception as e:

            context = {
                'data': 'Upload Error: ' + str(e)
            }

            return render(request, 'Upload.html', context)

    return render(request, 'Upload.html')


# ================= LOGIN ================= #

def UserLoginAction(request):

    global username

    if request.method == 'POST':

        username = request.POST.get('t1')
        password = request.POST.get('t2')

        # Demo Login
        if username == "admin" and password == "admin":

            context = {
                'data': 'Login successful'
            }

            return render(request, 'UserScreen.html', context)

        else:

            context = {
                'data': 'Login failed'
            }

            return render(request, 'UserLogin.html', context)

    return render(request, 'UserLogin.html')


# ================= SIGNUP ================= #

def SignupAction(request):

    global username
    global password
    global contact
    global gender
    global email
    global address
    global finger

    if request.method == 'POST':

        username = request.POST.get('t1')
        password = request.POST.get('t2')
        contact = request.POST.get('t3')
        gender = request.POST.get('t4')
        email = request.POST.get('t5')
        address = request.POST.get('t6')
        finger = request.POST.get('t7')

        context = {
            'data': f'{username} signup successful'
        }

        return render(request, 'Signup.html', context)

    return render(request, 'Signup.html')


# ================= FACE VALIDATION ================= #

def ValidateFaceAction(request):

    context = {
        'data': 'Face validation temporarily disabled on Vercel'
    }

    return render(
        request,
        'UserScreen.html',
        context
    )


# ================= WEBCAM SAVE ================= #

def WebCam(request):

    try:

        data = str(request.body)

        if ';base64,' not in data:
            return HttpResponse("Invalid image")

        formats, imgstr = data.split(';base64,')

        imgstr = imgstr[:-1]

        image_data = base64.b64decode(imgstr)

        save_dir = "SecureBiometricApp/static/photo"

        os.makedirs(save_dir, exist_ok=True)

        save_path = os.path.join(save_dir, "test.png")

        with open(save_path, 'wb') as f:
            f.write(image_data)

        return HttpResponse("Image saved")

    except Exception as e:

        return HttpResponse("Webcam Error: " + str(e))


# ================= FACE CAPTURE ================= #

def CaptureFaceAction(request):

    context = {
        'data': 'Face capture saved successfully'
    }

    return render(request, 'Signup.html', context)