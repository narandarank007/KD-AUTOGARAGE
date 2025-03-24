from django.shortcuts import render,redirect
from django.contrib import messages

 #--------home-------
def home(request):
    return render(request,'open.html')
#-----------------redirect------
def rhome(request):
    return redirect('home')

def relogin(request):
   return redirect('servicelogin')
    
#---------- register login--------
#from django.contrib.auth.forms import UserCreationForm
from cl.forms import UserCreationForm
from.models import login
from django.contrib.auth.models import User
def registerlogin(request):
   
   if request.method == "POST":
    email=request.POST["email"]
    usname=request.POST["username"]
    password=request.POST["password1"]
    p1=request.POST["password2"]


    if password == p1:
       user=User.objects.create_user(username=usname,email=email,password=password)
       obj=login()
       obj.Email=email
       obj.Username=usname
       obj.Password=password
       obj.save()  
       user.save()
       messages.success(request, "register successfully !")
       return redirect('servicelogin')
    else:
         messages.error(request, "Passwords do not match.")
         return redirect('register')
   else:
     form=UserCreationForm()
     return render(request,'registerlogin.html',{'form':form})
   
#----------------------------



#---------profiles---
from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    return render(request,'profile.html') 

@login_required
def detailing(request):
   return render(request,'servicedetailing.html')

@login_required
def painting(request):
   return render(request,'servicepainting.html')
@login_required 
def acservice(request):
   return render(request,'serviceacservice.html')
@login_required
def custom(request):
   return render(request,'servicecustom.html')
@login_required
def insurance(request):
   return render(request,'serviceinsurance.html')
#-----------------------------------booking op



#----------------------------------------------
def error404(request,exception):
     return render(request,'error404.html')




#contact detail---------
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import enquiry

def contact(request):
    return render(request, "contact.html")
     
def contact(request):
    if request.method == "POST":
        # Get form data
        NAME = request.POST.get('name', '').strip()
        EMAIL = request.POST.get('email', '').strip()
        MESSAGE = request.POST.get('message', '').strip()

        # Check if any field is empty
        if not NAME or not EMAIL or not MESSAGE:
            return HttpResponse("All fields are required.", status=400)

        # Save the enquiry to the database
        obj = enquiry()
        obj.EName = NAME
        obj.Mail = EMAIL
        obj.YourMessage = MESSAGE
        obj.save()

        # Send success message to the user
        messages.success(request, "Your message has been successfully submitted.")

        # Prepare context for emails
        context = {
            "name": NAME,
            "email": EMAIL,
            "body": MESSAGE
        }

        # Admin email content
        admin_html_message = render_to_string("companyemail.html", context)
        admin_plain_message = strip_tags(admin_html_message)

        # Send email to admin
        send_mail(
            subject=f"New Message from {NAME}",
            message=admin_plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["kdautogarageservice@gmail.com"],  # Assuming there's a setting for the admin email
            html_message=admin_html_message
        )

        # Prepare and send confirmation email to the user
        user_context = {"name": NAME}
        user_html_message = render_to_string("contactconfirm.html", user_context)
        user_plain_message = strip_tags(user_html_message)

        # Send email to the user
        send_mail(
            subject="Thank you for contacting us!",
            message=user_plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[EMAIL],
            html_message=user_html_message
        )
        return redirect("contact")
    else:
     return render(request, "contact.html")
        
def show_item(request):
    return render(request, "roughpaper.html")

     


#roadside-------------
def roadside(request):
   return render(request,"roadside.html")

#------------appointment--




import pdfkit
from django.core.mail import send_mail
from .models import Booking
from cl.forms import AppointmentForm
from datetime import date as realdate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def book_appointment(request, package):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            pickup_slot = form.cleaned_data['pickup_slot']
            namee = form.cleaned_data.get('CarBrand')
            email = form.cleaned_data.get('email')
            packagee = package

            # Check if slot is already booked
            if Booking.objects.filter(date=date, pickup_slot=pickup_slot).exists():
                messages.error(request, "This slot is already booked for the selected date.")
                return render(request, 'booking op.html', {'form': form, 'package': package})

            # Save the booking
            booking = form.save(commit=False)
            booking.CarBrand = namee
            booking.email = email
            booking.package = packagee
            booking.save()

            # Prepare email content
            user_context = {
                "name": request.user.username,
                "package": booking.package,
                "pickupdate": booking.date,
                "pickup_slot": booking.pickup_slot,
                "today": realdate.today().strftime("%B %d, %Y"),
                "phone": booking.phone,
                "address": booking.address,
                "id": booking.id,
                "carbrand":booking.CarBrand,
                "modelname": booking.ModelName
            }

            # Generate HTML for PDF
            user_html_message = render_to_string("confirmemail.html", user_context)
            user_plain_message = "Thank you for confirming your appointment ."

            # Set up wkhtmltopdf path
            path_wkhtmltopdf = settings.WKHTMLTOPDF_PATH  # Use settings instead of hardcoding path
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

            # Generate PDF
            
            options = {'enable-local-file-access': '', 'load-error-handling': 'ignore'}
            pdf_data = pdfkit.from_string(user_html_message, False, configuration=config, options=options)

                # Send confirmation email with PDF attachment
            email_message = EmailMessage(
                subject="Thank you for booking an appointment!",
                body=user_plain_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )
            email_message.attach('bookingconfirmation.pdf', pdf_data, 'application/pdf')
            email_message.send()

                # Success message after email is sent
            messages.success(request, "Appointment booked successfully! ")

           
            # Redirect or render a success page
            return render(request, 'booking op.html', {'form': form, 'package': package})

    else:
        form = AppointmentForm()

    return render(request, 'booking op.html', {'form': form, 'package': package})
