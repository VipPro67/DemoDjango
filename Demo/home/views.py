from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>DemoDjango</h1>")
    response.writelines("<h2>Nhóm 5</h2>")
    response.writelines("<p>19521358	Vương Đức Đạt</p>")
    response.writelines("<p>20521867	Huỳnh Thiện Tâm</p>")
    response.writelines("<p>20522103	Triệu Tuấn Tú</p>")
    response.writelines("<p>20522165	Nguyễn Phước An Vũ</p>")
    response.writelines("<p>20521526	Phan Nguyên Lịch</p>")
    response.writelines("<p>20521947	Lê Văn Thiện</p>")
    response.writelines("<p>18520439	Tô Thành An</p>")
    response.writelines("<p>20522157	Hồng Trường Vinh</p>")
    return response