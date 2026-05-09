from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import os
import cv2
import base64
import numpy as np
from PIL import Image

# ================= GLOBAL VARIABLES ================= #

username = ""
password = ""
contact = ""
gender = ""
email = ""
address = ""
finger = ""

# ================= LOAD FACE DETECTOR ================= #

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face_detection = cv2.CascadeClassifier(cascade_path)

# IMPORTANT:
# Do NOT initialize recognizer globally on Vercel
recognizer = None


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


# ================= FACE IMAGE HELPERS ================= #

def getUserImages():

    names = []
    ids = []
    faces = []

    dataset = "SecureBiometricApp/static/profile"

    os.makedirs(dataset, exist_ok=True)

    count = 0

    for root, dirs, files in os.walk(dataset):

        for file in files:

            try:

                path = os.path.join(root, file)

                pilImage = Image.open(path).convert('L')

                imageNp = np.array(pilImage, 'uint8')

                name = os.path.splitext(file)[0]

                names.append(name)

                faces.append(imageNp)

                ids.append(count)

                count += 1

            except:
                pass

    return names, ids, faces


def getName(predict, ids, names):

    for i in range(len(ids)):

        if ids[i] == predict:
            return names[i]

    return "Unknown"


# ================= FACE VALIDATION ================= #

def ValidateFaceAction(request):

    global username

    try:

        img_path = 'SecureBiometricApp/static/photo/test.png'

        if not os.path.exists(img_path):

            context = {
                'data': 'Test image not found'
            }

            return render(request, 'ValidateFace.html', context)

        img = cv2.imread(img_path)

        if img is None:

            context = {
                'data': 'Unable to read image'
            }

            return render(request, 'ValidateFace.html', context)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = face_detection.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        if len(detected_faces) == 0:

            context = {
                'data': 'Face not detected'
            }

            return render(request, 'ValidateFace.html', context)

        (x, y, w, h) = detected_faces[0]

        face_component = gray[y:y+h, x:x+w]

        names, ids, faces = getUserImages()

        if len(faces) == 0:

            context = {
                'data': 'No trained faces found'
            }

            return render(request, 'ValidateFace.html', context)

        # SAFE INITIALIZATION
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        recognizer.train(faces, np.asarray(ids))

        predict, conf = recognizer.predict(face_component)

        validate_user = getName(predict, ids, names)

        if conf < 80 and validate_user == username:

            context = {
                'data': f'Welcome {username}, face matched successfully'
            }

            return render(request, 'UserScreen.html', context)

        context = {
            'data': 'Face validation failed'
        }

        return render(request, 'ValidateFace.html', context)

    except Exception as e:

        context = {
            'data': 'Face Recognition Error: ' + str(e)
        }

        return render(request, 'ValidateFace.html', context)


# ================= LOGIN ================= #

def UserLoginAction(request):

    global username

    if request.method == 'POST':

        username = request.POST.get('t1')
        password = request.POST.get('t2')

        # Demo login
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
            'data': f'{username}, please capture your face'
        }

        return render(request, 'CaptureFace.html', context)

    return render(request, 'Signup.html')


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

    global username

    try:

        img_path = 'SecureBiometricApp/static/photo/test.png'

        if not os.path.exists(img_path):

            context = {
                'data': 'Test image not found'
            }

            return render(request, 'CaptureFace.html', context)

        img = cv2.imread(img_path)

        if img is None:

            context = {
                'data': 'Unable to read image'
            }

            return render(request, 'CaptureFace.html', context)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = face_detection.detectMultiScale(
            gray,
            1.3,
            5
        )

        if len(detected_faces) == 0:

            context = {
                'data': 'Unable to detect face'
            }

            return render(request, 'CaptureFace.html', context)

        (x, y, w, h) = detected_faces[0]

        face_component = img[y:y+h, x:x+w]

        profile_dir = 'SecureBiometricApp/static/profile'

        os.makedirs(profile_dir, exist_ok=True)

        save_path = os.path.join(
            profile_dir,
            username + '.png'
        )

        cv2.imwrite(save_path, face_component)

        context = {
            'data': 'Signup process completed successfully'
        }

        return render(request, 'Signup.html', context)

    except Exception as e:

        context = {
            'data': 'Capture Face Error: ' + str(e)
        }

        return render(request, 'CaptureFace.html', context)

