"""
    _summary_
    
    Module use to operate the Dashoboard Operations,
    include: Create project, Save project, Delete project, REST APIS
    Low Level: DB Operations
    
    Read Code 1 for more information.


"""


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def engine(request):
    """_summary_
    Code 1

    Args:
        request (Http): Recieve a http/https respose and return a page

    Returns:
        HttpResponse: Returning a Dashboard page
    """
    return render(request, 'core/index.html')