from django.http import HttpResponse

def calion(request):
    return HttpResponse("Hi ,welcome to the first page of my project")
def coursedetails(request,courseid):
    return HttpResponse(courseid)