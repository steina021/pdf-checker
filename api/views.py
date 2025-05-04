from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoggerSerializer
from api.pdf_checker.check_accessibility import check_accessibility
import tempfile
import os

@api_view(['POST'])
def check_pdf(request):
    # Case 1: Check by URL
    pdf_url = request.data.get("pdf_url")
    
    # Case 2: Check by File Upload
    pdf_file = request.FILES.get("pdf_file")

    password = request.data.get("password", "")

    # If neither URL nor file is provided, return an error
    if not pdf_url and not pdf_file:
        return Response({"error": "Either pdf_url or pdf_file is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # If pdf_url is provided, use it to perform the check
        if pdf_url:
            accessibility_report = check_accessibility(pdf_url, password=password)
        
        # If pdf_file is provided, save it to a temporary file for checking
        elif pdf_file:
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(pdf_file.read())
                tmp_file_path = tmp_file.name

            # Perform the check using the file's path
            accessibility_report = check_accessibility(tmp_file_path, password=password)

            # Delete the temporary file after processing
            os.remove(tmp_file_path)

        # Save the result using the LoggerSerializer (optional)
        serializer = LoggerSerializer(data={
            "pdf_url": pdf_url if pdf_url else "Uploaded file",
            "accessibility_report": accessibility_report
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
