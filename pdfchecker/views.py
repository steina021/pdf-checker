import os
from pypdf import PdfReader
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')

def scan_pdf(request):

    if request.method == 'POST' and request.FILES.get('pdf_file'):
        # Get the uploaded PDF file from the request
        uploaded_file = request.FILES['pdf_file']

        try:
            # Create an instance of FileSystemStorage, specifying the location
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)

            # Save the uploaded file to the filesystem and get the saved filename
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)

            # Ensure the file is a PDF by checking the extension
            if file_path.endswith('.pdf'):
                # Open the PDF using PyPDF2
                reader = PdfReader(file_path)

                # Initialize extracted_text as an empty string
                extracted_text = ""

                # Loop through all pages and extract text from each one
                for page_number, page in enumerate(reader.pages):
                    # Extract text from the current page
                    page_text = page.extract_text()

                    if page_text:
                        # If text is found, append it to extracted_text with page number
                        extracted_text += f"Page {page_number + 1}:\n{page_text}\n\n"
                    else:
                        # If no text is extracted from a page, indicate it
                        extracted_text += f"Page {page_number + 1}: No text extracted.\n\n"

                # Delete the file after processing
                os.remove(file_path)

                # Return extracted text in the response
                return JsonResponse({
                    "number_of_pages": len(reader.pages),
                    "extracted_text": extracted_text,
                })
            else:
                # Log the error if the file is not a PDF
                print(f"Error: File {file_path} is not a valid PDF.")  # Debug: Log when file is not a PDF
                return JsonResponse({"error": "Invalid file format, please upload a PDF."}, status=400)

        except Exception as e:
            # Handle any exceptions that may arise and log the error
            print(f"Exception during PDF processing: {str(e)}")  # Debug: Log the exception message
            return JsonResponse({"error": f"Error processing PDF: {str(e)}"}, status=500)

    # If no file is uploaded, log the error
    print("Error: No file uploaded.")  # Debug: Log if no file is uploaded
    return JsonResponse({"error": "No file uploaded."}, status=400)
