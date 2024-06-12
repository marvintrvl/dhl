from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .models import Order, Package, Customer

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'core/register.html')
    
    # Get data from request
    username = request.data.get('email')  # Use email as username
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')
    address = request.data.get('address')
    city = request.data.get('city')
    house_number = request.data.get('house_number')
    postal_code = request.data.get('postal_code')
    country = request.data.get('country')
    birthday = request.data.get('birthday')
    phone_number = request.data.get('phone_number')

    # Create user
    user = Customer.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        address=address,
        city=city,
        house_number=house_number,
        postal_code=postal_code,
        country=country,
        birthday=birthday,
        phone_number=phone_number
    )

    # Get or create auth token for user
    token, created = Token.objects.get_or_create(user=user)

    # Return token response
    data = {'token': token.key}
    return redirect('index')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Customer.objects.filter(email=email).first()

        if user and user.check_password(password):
            login(request, user)
            return redirect('index')
        else:
            return Response(status=400)

@api_view(['GET', 'POST'])
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'packaging/order_detail.html', {'order': order})

@login_required
def user_balance(request):
    user = request.user
    return render(request, 'core/user_balance.html', {'balance': user.balance})

@login_required
def profile(request):
    user = request.user
    return render(request, 'core/profile.html', {'user': user})

@login_required
def order_list(request):
    orders = Order.objects.filter(package__recipient=request.user)
    return render(request, 'core/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'core/order_detail.html', {'order': order})

def index(request):
    return render(request, 'core/index.html')

def details(request):
    return render(request, 'core/details.html')
    
@api_view(['GET'])
def scan_qr_code(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if package.status != 'EMPTY':
        # Credit deposit to recipient's balance first
        package.recipient.balance += package.deposit_paid
        package.recipient.save()

        package.reuse_count += 1

        # Clear package details except for the id
        package.status = 'EMPTY'
        package.gps_tracking_code = ''
        package.is_cleared = True
        package.sender = None
        package.recipient = None
        
        # Save the package
        package.save()
        
        # Redirect to a success page
        return redirect('scan_success')
    
    return Response(status=400, data={'error': 'Package already returned or invalid status'})


def scan_success(request):
    return render(request, 'core/scan_success.html')