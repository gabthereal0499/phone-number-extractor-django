from django.urls import path
from . import views


urlpatterns = [

    # =====================================
    # Upload files for OCR processing
    # Final API URL → /api/upload/
    # =====================================
    path(
        'upload/',
        views.upload_files,
        name='upload_files'
    ),


    # =====================================
    # Download extracted phone numbers
    # Final API URL → /api/download/
    # =====================================
    path(
        'download/',
        views.download_file,
        name='download_file'
    ),


    # =====================================
    # Send WhatsApp messages
    # Final API URL → /api/send-messages/
    # =====================================
    path(
        'send-messages/',
        views.send_whatsapp_messages,
        name='send_whatsapp_messages'
    ),

]