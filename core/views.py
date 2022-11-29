from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from coinbase_commerce.client import Client

from Apex import settings
from .models import User, Booking, Discount
from .decorators import unauthorised_user, admin_view
from .forms import ClientForm, BookingForm, CustomUser, DiscountForm

@login_required(login_url='login')
@admin_view
def dashboard(request):
    clients = User.objects.filter(is_client = True)
    bookings = Booking.objects.all()

    context = {
        'clients': clients,
        'bookings': bookings
    }
    return render(request, 'admin/dashboard.html', context)

@login_required(login_url='login')
@admin_view
def client(request):
    clients = User.objects.filter(is_client = True)

    context = {
        'clients': clients,
    }
    return render(request, 'admin/client.html', context)

@login_required(login_url='login')
@admin_view
def admin_booking(request):
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings
    }
    return render(request, 'admin/booking.html', context)

@login_required(login_url='login')
@admin_view
def discount(request):
    discount = Discount.objects.all()

    context = {
        'discount': discount,
    }
    return render(request, 'admin/discount.html', context)

@login_required(login_url='login')
@admin_view
def discount_form(request):
    discount = DiscountForm()

    context = {
        'discount_form': discount,
    }
    return render(request, 'admin/discount_form.html', context)

@login_required(login_url='login')
@admin_view
def password_change(request):
    if request.method == 'POST':
        admin_email = request.user
        print(admin_email)
        user = User.objects.get(email = admin_email)
        print(user.password)
        new_password = request.POST['password']
        logout(request)
        user.set_password(new_password)
        user.save()
        return redirect('login')

    return render(request, 'admin/password_change.html')

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='login')
@admin_view
def profile(request):
    if request.user:
        user = User.objects.get(email = request.user)
        booking = Booking.objects.get(client=user)

        discount = user.discount_set.all()
        if not discount:
            discount = False

    context = {
        'client': user,
        'booking': booking,
        'discount': discount
    }
    return render(request, 'core/profile.html', context)

def payment(request, amount):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://127.0.0.1:8000/'
    celeb_booking = {
        'name': '',
        # 'booking_number': booking.booking_number,
        'local_price': {
            'amount': amount,
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url,
        'cancel_url': domain_url + 'about'
    }

    charge = client.charge.create(**celeb_booking)
    return redirect(charge.hosted_url)

@unauthorised_user
def booking(request):
    client_form = ClientForm()
    booking_form = BookingForm()

    if request.method == 'POST':
        client = User(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password'],
            gender = request.POST['gender'],
            country = request.POST['country'],
            state = request.POST['state'],
            dob = request.POST['dob'],
            phone = request.POST['phone'],
            area_code = request.POST['area_code'],
            avatar = request.FILES.get('avatar'),
            is_admin = False,
            is_client = True
        )
        client.save()

        booking = Booking(
            address = request.POST['address'],
            client = client
        )
        booking.save()

        messages.success(request, 'Profile created successfully!!!')

        login(request, client)
        return redirect('profile')

    context = {
        'client_form': client_form,
        'booking_form': booking_form,
    }
    return render(request, 'registration/signup.html', context)

def signin(request):
    form = CustomUser()

    if request.method == 'POST':
        form = CustomUser(request.POST)

        try:
            client = User.objects.get(email = request.POST.get('email'))
        except:
            messages.error(request, 'email or password is incorrect!!!')
            return redirect('login')

        login(request, client)
        return redirect('profile')
        
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)

def about(request):
    return render(request, 'core/about.html')

def celebrities(request):
    return render(request, 'core/celebrities.html')