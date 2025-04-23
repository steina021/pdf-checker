from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoggerSerializer
from api.pdf_checker.check_accessibility import check_accessibility

@api_view(['POST'])
def check_pdf(request):
    
    # Expecting: 
    # { 
    #   "pdf_url": "<some URL or path>", 
    #   "password": "optional" 
    # }

    pdf_url = request.data.get("pdf_url")
    password = request.data.get("password", "")

    if not pdf_url:
        return Response({"error": "pdf_url is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        accessibility_report = check_accessibility(pdf_url, password=password)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Save it via serializer if needed
    serializer = LoggerSerializer(data={
        "pdf_url": pdf_url,
        "accessibility_report": accessibility_report
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
