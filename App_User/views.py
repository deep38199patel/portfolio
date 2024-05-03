from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactUsForm, SignUpForm, SignInForm
from .models import ContactUs
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactUsForm()
        return context
    
    def post(self, request, **kwargs):
        contact_fm = ContactUsForm(data=request.POST)

        if contact_fm.is_valid():
            firstname = request.POST.get('sender_firstname')
            lastname = request.POST.get('sender_lastname')
            sender_email = request.POST.get('sender_email')
            message = request.POST.get('message')


            come_time = timezone.now()
            contact_user = ContactUs(sender_firstname=firstname, sender_email=sender_email, sender_lastname=lastname,
                                     message=message, come_time=come_time)
            contact_user.save()
            messages.success(request, 'Your Query Successfully Send! We Contact you in 24h under medium Email!')
            return redirect(self.success_url)
        
        else:
            print(contact_fm.errors)
            return render(request, self.template_name, {'contact_form': contact_fm})


class LogInView(TemplateView):
    template_name = 'login.html'
    success_url = '/profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signIn_form'] = SignInForm()
        return context

    def post(self, request, **kwargs):
        log_fm = SignInForm(request=request, data=request.POST)
        if log_fm.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect(self.success_url)
                else:
                    return redirect(self.success_url)
        else:
            print(log_fm.errors)
            return render(request, self.template_name, {'signIn_form': log_fm})

    
class SignUpView(TemplateView):
    template_name = 'signup.html'
    success_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_form'] = SignUpForm()
        return context

    def post(self, request, **kwargs):
        my_data = SignUpForm(request.POST)
        if my_data.is_valid():
            username = request.POST.get('username')
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            password1 = request.POST.get('password1')
            email = request.POST.get('email')
            new_user = User(username=username, first_name=firstname, last_name=lastname, email=email)
            new_user.set_password(password1)
            new_user.save()
            messages.success(request, 'Your Account Successfully Created !')
            return redirect(self.success_url)
        else:
            print(my_data.errors)
            return render(request, self.template_name, {'signup_form': my_data})

      
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContactList'] = ContactUs.objects.all()
        context['contact_form'] = ContactUsForm()
        return context
    
    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            action = request.POST.get('action')
        
            if action == 'sign-out':
                logout(request)
                return redirect('/')
            
            elif action == 'delete-contact':
                contact_id = request.POST.get('contact_id')
                
                contact_item = ContactUs.objects.filter(pk=contact_id)
                contact_item.delete()

                messages.success(request, 'Your Query Successfully solved!')
                return redirect('/profile')
            
            elif action == 'update-contact':
                contact_id = request.POST.get('contact_id')
                contact_item = ContactUs.objects.filter(id=contact_id).first()
                if request.POST.get('fetch_form') == 'fetch_form':
                    update_fm = ContactUsForm(instance=contact_item)
                    context = self.get_context_data()
                    context['pass_action'] = 'update-contact'
                    context['contact_form'] = update_fm
                    context['contact_id'] = contact_id
                    return render(request, self.template_name, context)
                    
                else:
                    update_fm = ContactUsForm(request.POST, instance=contact_item)
                    if update_fm.is_valid():
                        update_fm.save(contact_id)
                        messages.success(request, 'Contact Information Successfully Updated!')
                        return redirect('/profile')
                    else:
                        messages.error(request, 'Something Went Wrong!', 'danger')
                        return redirect('/profile')
            else:
                return redirect('/')
        else:
            return redirect('/')