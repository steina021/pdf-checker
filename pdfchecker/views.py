import os
from pypdf import PdfReader
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO

def index(request):
    return render(request, 'index.html')

def scan_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        uploaded_file = request.FILES['pdf_file']

        try:
            # Read PDF content directly into memory
            pdf_content = uploaded_file.read()
            pdf_file_obj = BytesIO(pdf_content)

            # Open the PDF using pypdf from in-memory content
            reader = PdfReader(pdf_file_obj)

            extracted_text = ""
            for page_number, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_text += f"Page {page_number + 1}:\n{page_text}\n\n"
                else:
                    extracted_text += f"Page {page_number + 1}: No text extracted.\n\n"

            return JsonResponse({
                "number_of_pages": len(reader.pages),
                "extracted_text": extracted_text,
            })

        except Exception as e:
            print(f"Exception during PDF processing: {str(e)}")
            return JsonResponse({"error": f"Error processing PDF: {str(e)}"}, status=500)

    print("Error: No file uploaded.")
    return JsonResponse({"error": "No file uploaded."}, status=400)