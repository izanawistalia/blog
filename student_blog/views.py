from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import botany
from .models import commerce
from .models import cs
from .models import geography
from .models import history
from .models import math
from .models import physics
from .models import yoga
from .models import zoology

@login_required
def botanycreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Botany = botany()
            Botany.title = request.POST['title']
            Botany.body = request.POST['body']
            Botany.image = request.FILES['image']
            Botany.pub_date = timezone.datetime.now()
            Botany.hunter = request.user
            Botany.save()
            return redirect('/student_blog/'+ str(Botany.id)+'/botanydetail')
            
        else:
            return render(request, 'student_blog/botanycreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/botanycreate.html')

@login_required
def commercecreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Commerce = commerce()
            Commerce.title = request.POST['title']
            Commerce.body = request.POST['body']
            Commerce.image = request.FILES['image']
            Commerce.pub_date = timezone.datetime.now()
            Commerce.hunter = request.user
            Commerce.save()
            return redirect('/student_blog/'+ str(Commerce.id)+'/commercedetail')
            
        else:
            return render(request, 'student_blog/commercecreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/commercecreate.html')

@login_required
def cscreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Cs = cs()
            Cs.title = request.POST['title']
            Cs.body = request.POST['body']
            Cs.image = request.FILES['image']
            Cs.pub_date = timezone.datetime.now()
            Cs.hunter = request.user
            Cs.save()
            return redirect('/student_blog/'+ str(Cs.id)+'/csdetail')
            
        else:
            return render(request, 'student_blog/cscreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/cscreate.html')

@login_required
def geographycreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Geography = geography()
            Geography.title = request.POST['title']
            Geography.body = request.POST['body']
            Geography.image = request.FILES['image']
            Geography.pub_date = timezone.datetime.now()
            Geography.hunter = request.user
            Geography.save()
            return redirect('/student_blog/'+ str(Geography.id)+'/geographydetail')
            
        else:
            return render(request, 'student_blog/geographycreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/geographycreate.html')

@login_required
def historycreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            History = history()
            History.title = request.POST['title']
            History.body = request.POST['body']
            History.image = request.FILES['image']
            History.pub_date = timezone.datetime.now()
            History.hunter = request.user
            History.save()
            return redirect('/student_blog/'+ str(History.id)+'/historydetail')
            
        else:
            return render(request, 'student_blog/historycreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/historycreate.html')

@login_required
def mathcreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Math = math()
            Math.title = request.POST['title']
            Math.body = request.POST['body']
            Math.image = request.FILES['image']
            Math.pub_date = timezone.datetime.now()
            Math.hunter = request.user
            Math.save()
            return redirect('/student_blog/'+ str(Math.id)+'/mathdetail')
            
        else:
            return render(request, 'student_blog/mathcreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/mathcreate.html')

@login_required
def physicscreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Physics = physics()
            Physics.title = request.POST['title']
            Physics.body = request.POST['body']
            Physics.image = request.FILES['image']
            Physics.pub_date = timezone.datetime.now()
            Physics.hunter = request.user
            Physics.save()
            return redirect('/student_blog/'+ str(Physics.id)+'/physicsdetail')
            
        else:
            return render(request, 'student_blog/physicscreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/physicscreate.html')

@login_required
def yogacreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Yoga = yoga()
            Yoga.title = request.POST['title']
            Yoga.body = request.POST['body']
            Yoga.image = request.FILES['image']
            Yoga.pub_date = timezone.datetime.now()
            Yoga.hunter = request.user
            Yoga.save()
            return redirect('/student_blog/'+ str(Yoga.id)+'/yogadetail')
            
        else:
            return render(request, 'student_blog/yogacreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/yogacreate.html')

@login_required
def zoologycreate(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image']:
            Zoology = zoology()
            Zoology.title = request.POST['title']
            Zoology.body = request.POST['body']
            Zoology.image = request.FILES['image']
            Zoology.pub_date = timezone.datetime.now()
            Zoology.hunter = request.user
            Zoology.save()
            return redirect('/student_blog/'+ str(Zoology.id)+'/zoologydetail')
            
        else:
            return render(request, 'student_blog/zoologycreate.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'student_blog/zoologycreate.html')


def botanydetail(request, botany_id):
    Product = get_object_or_404(botany, pk=botany_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def commercedetail(request, commerce_id):
    Product = get_object_or_404(commerce, pk=commerce_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def csdetail(request, cs_id):
    Product = get_object_or_404(cs, pk=cs_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def geographydetail(request, geography_id):
    Product = get_object_or_404(geography, pk=geography_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def historydetail(request, history_id):
    Product = get_object_or_404(history, pk=history_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def mathdetail(request, math_id):
    Product = get_object_or_404(math, pk=math_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def physicsdetail(request, physics_id):
    Product = get_object_or_404(physics, pk=physics_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def yogadetail(request, yoga_id):
    Product = get_object_or_404(yoga, pk=yoga_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})

def zoologydetail(request, zoology_id):
    Product = get_object_or_404(zoology, pk=zoology_id)
    return render(request, 'student_blog/detail.html', {'Product':Product})



@login_required
def botanyupvote(request, botany_id):
    if request.method == 'POST':
        Product = get_object_or_404(botany, pk=botany_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/botanydetail')

@login_required
def commerceupvote(request, commerce_id):
    if request.method == 'POST':
        Product = get_object_or_404(commerce, pk=commerce_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/commercedetail')

@login_required
def csupvote(request, cs_id):
    if request.method == 'POST':
        Product = get_object_or_404(cs, pk=cs_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/csdetail')

@login_required
def geographyupvote(request, geography_id):
    if request.method == 'POST':
        Product = get_object_or_404(geography, pk=geography_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/geographydetail')

@login_required
def historyupvote(request, history_id):
    if request.method == 'POST':
        Product = get_object_or_404(history, pk=history_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/historydetail')

@login_required
def mathupvote(request, math_id):
    if request.method == 'POST':
        Product = get_object_or_404(math, pk=math_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/mathdetail')

@login_required
def physicsupvote(request, physics_id):
    if request.method == 'POST':
        Product = get_object_or_404(physics, pk=physics_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/physicsdetail')

@login_required
def yogaupvote(request, yoga_id):
    if request.method == 'POST':
        Product = get_object_or_404(yoga, pk=yoga_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/yogadetail')

@login_required
def zoologyupvote(request, zoology_id):
    if request.method == 'POST':
        Product = get_object_or_404(zoology, pk=zoology_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/student_blog/'+ str(Product.id) + '/zoologydetail')





def botanyhome(request):
    Product = botany.objects
    return render(request, 'student_blog/botanyhome.html', {'Product':Product })


def commercehome(request):
    Product = commerce.objects
    return render(request, 'student_blog/commercehome.html', {'Product':Product })

def cshome(request):
    Product = cs.objects
    return render(request, 'student_blog/cshome.html', {'Product':Product })

def geographyhome(request):
    Product = geography.objects
    return render(request, 'student_blog/geographyhome.html', {'Product':Product })

def historyhome(request):
    Product = history.objects
    return render(request, 'student_blog/historyhome.html', {'Product':Product })

def mathhome(request):
    Product = math.objects
    return render(request, 'student_blog/mathhome.html', {'Product':Product })

def physicshome(request):
    Product = physics.objects
    return render(request, 'student_blog/physicshome.html', {'Product':Product })

def yogahome(request):
    Product = yoga.objects
    return render(request, 'student_blog/yogahome.html', {'Product':Product })

def zoologyhome(request):
    Product = zoology.objects
    return render(request, 'student_blog/zoologyhome.html', {'Product':Product })





























