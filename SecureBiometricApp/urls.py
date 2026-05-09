from django.urls import path
from . import views

urlpatterns = [

    # HOME PAGE
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),

    # LOGIN
    path("Login.html", views.Login, name="Login"),
    path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),

    # SIGNUP
    path("Signup.html", views.Signup, name="Signup"),
    path("SignupAction", views.SignupAction, name="SignupAction"),

    # FACE
    path("CaptureFaceAction", views.CaptureFaceAction, name="CaptureFaceAction"),
    path("ValidateFace.html", views.ValidateFace, name="ValidateFace"),
    path("ValidateFaceAction", views.ValidateFaceAction, name="ValidateFaceAction"),
    path("WebCam", views.WebCam, name="WebCam"),

    # FILES
    path("Upload.html", views.Upload, name="Upload"),
    path("UploadAction", views.UploadAction, name="UploadAction"),
    path("Download", views.Download, name="Download"),
    path("DownloadFileAction", views.DownloadFileAction, name="DownloadFileAction"),
]