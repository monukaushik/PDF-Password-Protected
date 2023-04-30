from django.shortcuts import render
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
import PyPDF2
  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response,encrypt="password", bottomup=True)  
    p.setFont("Times-Roman", 20)  
    p.drawString(100,700, "Hello, welcome.")  
    p.showPage()  
    p.save()  
    return response
