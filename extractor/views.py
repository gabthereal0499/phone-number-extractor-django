from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os
import uuid

from .send_whatsapp import send_messages

from .ocr_utils import (
    extract_text,
    extract_text_from_pdf,
    extract_text_from_ppt
)

from .number_extractor import extract_phone_numbers
from .excel_writer import save_to_excel


# ==============================
# REACT FRONTEND VIEW
# ==============================

def react_app(request):
    """
    This view serves the React build index.html
    so Django can run frontend + backend together.
    """
    return render(request, "index.html")


# ==============================
# REACT API ENDPOINT
# ==============================

@csrf_exempt
def upload_files(request):

    if request.method == "POST":

        files = request.FILES.getlist('files')
        all_numbers = set()

        upload_folder = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(upload_folder, exist_ok=True)

        for file in files:

            ext = os.path.splitext(file.name)[1].lower()

            allowed_extensions = [
                '.jpg', '.jpeg', '.png',
                '.pdf',
                '.pptx'
            ]

            if ext not in allowed_extensions:
                continue

            filename = f"{uuid.uuid4().hex}{ext}"
            filepath = os.path.join(upload_folder, filename)

            # Save uploaded file
            with open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            try:

                # IMAGE OCR
                if ext in ['.jpg', '.jpeg', '.png']:
                    text = extract_text(filepath)

                # PDF OCR
                elif ext == '.pdf':
                    text = extract_text_from_pdf(filepath)

                # PPT OCR
                elif ext == '.pptx':
                    text = extract_text_from_ppt(filepath)

                else:
                    continue

                numbers = extract_phone_numbers(text)

                all_numbers.update(numbers)

            except Exception as e:

                print(f"OCR ERROR while processing {file.name}: {e}")
                continue

        numbers_list = sorted(all_numbers)

        # Save Excel file
        output_file = os.path.join(settings.MEDIA_ROOT, "phone_numbers.xlsx")

        if numbers_list:
            save_to_excel(numbers_list, output_file)

        return JsonResponse({
            "status": "success",
            "numbers": numbers_list
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


# ==============================
# DOWNLOAD EXCEL
# ==============================

def download_file(request):

    output_file = os.path.join(settings.MEDIA_ROOT, "phone_numbers.xlsx")

    if os.path.exists(output_file):
        return FileResponse(
            open(output_file, 'rb'),
            as_attachment=True,
            filename="phone_numbers.xlsx"
        )

    return JsonResponse({"error": "File not found"}, status=404)


# ==============================
# SEND WHATSAPP MESSAGE
# ==============================

@csrf_exempt
def send_whatsapp_messages(request):

    if request.method == "POST":

        try:

            numbers = request.POST.getlist("numbers")

            if not numbers:
                return JsonResponse({
                    "status": "error",
                    "message": "No numbers provided"
                })

            # Clean numbers (remove spaces and non-digits)
            cleaned_numbers = []

            for num in numbers:

                num = str(num).strip()

                if num.isdigit() and len(num) >= 10:
                    cleaned_numbers.append(num)

            if not cleaned_numbers:
                return JsonResponse({
                    "status": "error",
                    "message": "No valid phone numbers"
                })

            message = request.POST.get(
                "message",
                "Hello! This message was sent from the Phone Number Extraction System."
            )

            print("Sending messages to:", cleaned_numbers)
            print("Message:", message)

            # Send WhatsApp messages
            send_messages(cleaned_numbers, message)

            return JsonResponse({
                "status": "success",
                "message": "Messages sent successfully"
            })

        except Exception as e:

            print("WHATSAPP SENDING ERROR:", e)

            return JsonResponse({
                "status": "error",
                "message": str(e)
            })

    return JsonResponse({"error": "Invalid request"}, status=400)