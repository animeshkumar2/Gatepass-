from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import User
from .models import SourceLocation
from .models import DestinationLocation
from .models import Approval
from .models import MMaterial
from .models import Gatepass
from .models import Session
from .models import ApproverReg

# Create your views here.


def register(request):
        return render(request,'register.html')
def login(request):
        return render(request,'login.html')


def add1(request):
        if request.method == 'POST':
                name1 = request.POST['name']
                # request.session['name1'] = name1
                email1 = request.POST['email']
                request.session['email'] = email1
                password1 = request.POST['password']
                pno = request.POST['pno']
                phonenumber = request.POST['phonenumber']
                peronal_details = User(name=name1,email=email1,password=password1,pno=pno,phonenumber=phonenumber)
                peronal_details.save()
                return render(request,'login.html')                  
        else:
                return render(request,'register.html')


def log1(request):
        if request.method == 'POST':
                email1 = request.POST['email']
                password1 = request.POST['password']
                if User.objects.filter(email=email1,password=password1):
                        return render(request,'gatepass_choice.html')
                else:
                        return render(request,'login.html') 

def create1(request):
        source=SourceLocation.objects.all()
        dest=DestinationLocation.objects.all()
        context= {'source' :source , 'dest' :dest}
        return render(request,'location.html', context) 
         
        

def manage1(request):
        return render(request,'manage.html')

def approver_reg1(request):
        if request.method == 'POST':
                per = request.POST['personal_no']
                apr = Approval.objects.filter(pers_number=per)
                return render(request,'app_reg.html',{'apr' :apr}) 

def app_log1(request):
        if request.method == 'POST':
                app_name = request.POST['app_name']
                email1 = request.POST['email']
                password1 = request.POST['password']
                pno = request.POST['pno']
                peronal_details = ApproverReg(app_name=app_name,app_email=email1,app_password=password1,personal_no=pno)
                peronal_details.save()
                return render(request,'app_login.html',{'app_name' :app_name})                  
        else:
                return render(request,'app_reg.html') 

def app_login1(request):
        return render(request,'app_login.html')

def approval_log1(request):
        if request.method == 'POST':
                ap = request.POST['approver']
                email1 = request.POST['email']
                password1 = request.POST['password']
                customers = Gatepass.objects.filter(approval=ap)
                if ApproverReg.objects.filter(app_email=email1,app_password=password1):
                        return render(request,'approval_admin.html',{'customers' :customers})
                else:
                        return render(request,'login.html')
                   

def approval1(request):
        if request.method == 'POST':
                source = request.POST['source']
                dest = request.POST['dest']
                appr = Approval.objects.filter(source__s_name=source)
                mat = MMaterial.objects.all()
                return render(request,'approval.html',{'appr' :appr,'mat':mat, 'source':source, 'dest': dest })                     

def vehicle1(request):
        if request.method == 'POST':
                source = request.POST['source']
                request.session['source'] = source
                dest = request.POST['dest']
                request.session['dest'] = dest
                quantity = request.POST['quant']
                request.session['quant'] = quantity
                app = request.POST['app']
                request.session['app'] = app
                mat = request.POST['mat']
                
                material = MMaterial.objects.filter(m_material_id=mat)
                
                request.session['mat'] = mat

                selection = request.POST['selection']
                if selection == 'Employee':
                        return render(request,'new.html')
                else:
                        return render(request,'courier.html')
                

def gatepass1(request):
        if request.method == 'POST':
                print(request.POST['courier'])
                cour=request.POST['courier']
                email = request.session.get('email', None)
                user = User.objects.filter(email=email)
                source = request.session.get('source', None)
                dest = request.session.get('dest', None)
                quant = request.session.get('quant', None)
                app = request.session.get('app', None)
                mat = request.session.get('mat', None)

                selected_details = Gatepass(userid = user[0],source = source,quantity = quant,destination = dest,approval = app,courierservice=cour,material_id=mat)
                selected_details.save()

                matr = MMaterial.objects.filter(m_material_id=mat)

                return render(request,'gatepass.html',{'user':user,'matr':matr,'source':source,'dest': dest,'quant':quant,'app':app,'cour':cour})

       

                