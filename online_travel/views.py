from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 방구석 세계여행에 오신 것을 환영합니다")

