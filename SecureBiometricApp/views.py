from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import os
import base64

# ================= GLOBAL VARIABLES ================= #

username = ""

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

    try:

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

    except Exception as e:

        return HttpResponse("Download Error : " + str(e))


def Download(request):

    try:

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

    except Exception as e:

        return HttpResponse("Download Page Error : " + str(e))


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
                'data': 'Upload Error : ' + str(e)
            }

            return render(request, 'Upload.html', context)

    return render(request, 'Upload.html')


# ================= LOGIN ================= #

def UserLoginAction(request):

    global username

    try:

        if request.method == 'POST':

            username = request.POST.get('t1')
            password = request.POST.get('t2')

            # DEMO LOGIN

            if username == "admin" and password == "admin":

                context = {
                    'data': 'Login successful'
                }

                return render(request, 'VerifyFinger.html', context)

            else:

                context = {
                    'data': 'Login failed'
                }

                return render(request, 'UserLogin.html', context)

        return render(request, 'UserLogin.html')

    except Exception as e:

        return HttpResponse("Login Error : " + str(e))


# ================= SIGNUP ================= #

def SignupAction(request):

    global username

    try:

        if request.method == 'POST':

            username = request.POST.get('t1')

            context = {
                'data': f'{username}, signup completed successfully'
            }

            return render(request, 'Signup.html', context)

        return render(request, 'Signup.html')

    except Exception as e:

        return HttpResponse("Signup Error : " + str(e))


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

        return HttpResponse("Image saved successfully")

    except Exception as e:

        return HttpResponse("Webcam Error : " + str(e))


# ================= FACE VALIDATION ================= #

def ValidateFaceAction(request):

    context = {
        'data': 'Face validation temporarily disabled for Vercel deployment'
    }

    return render(request, 'ValidateFace.html', context)


# ================= FACE CAPTURE ================= #

def CaptureFaceAction(request):

    context = {
        'data': 'Face capture temporarily disabled for Vercel deployment'
    }

    return render(request, 'Signup.html', context)