from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.models import User
from django.db.models import Q
import datetime

from management.models import User, Shop, Order, Order_List, Wallet, Transaction, Comment, Menu
# Create your views here.


# login
def user_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                if(user.user_type=="shop"):
                    return redirect('shop')
                else:
                    return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def sign_up(request):
    context = {}
    msg = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        if password == password2:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type=user_type
            )
            user.save()
            context['username'] = username
            context['password'] = password
            context['success'] = 'Successfully Registered Welcome! %s' % (
                first_name)
            return render(request, template_name='login.html', context=context)
    else:
        context['error'] = 'Something went wrong or Password does not match'

    return render(request, template_name='signup.html', context=context)


# @login_required
def index(request):
    menu = Menu.objects.all
    shop = Shop.objects.all
    context = {
        'menu': menu,
        'shop': shop
    }
    return render(request, template_name='index.html', context=context)

@login_required
def shop(request):
    msg = ''
    button_text = 'Create'
    context = {}
    if request.method == 'POST':
        name = request.POST.get('shop_name')
        description = request.POST.get('shop_desc')
        location = request.POST.get('shop_location')
        total_table = request.POST.get('shop_table')
        shop = Shop.objects.filter(user_id_id=request.user.id)
        if not shop:
            shop = Shop.objects.create(
                name=name,
                description=description,
                location=location,
                total_table=total_table,
                user_id_id=request.user.id
            )
        else:
            shop = shop[0]
            shop.name=name
            shop.description=description
            shop.location=location
            shop.total_table=total_table
        shop.save()
        msg = 'Successfully Edit Shop: คุณ %s' % (request.user.first_name)
    
    shop = Shop.objects.filter(user_id_id=request.user.id)[0]
    if not shop:
        button_text = "Create"
    else:
        button_text = "Edit"
    context = {
        'msg': msg,
        'button_text': button_text,
        'shop': shop
    }
    return render(request, template_name='shop.html', context=context)
    #return redirect('menu')

@login_required
def add_menu(request):
    context = {}
    msg = ''
    button_text = 'Create'
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name')
        description = request.POST.get('description')
        menu_price = request.POST.get('menu_price')
        menu_id = request.POST.get('menu_id')
        if not menu_id:
            shop = Shop.objects.filter(user_id_id=request.user.id)[0]
            menu = Menu.objects.create(
                menu_name=menu_name,
                description=description,
                menu_price=menu_price,
                shop_id_id = shop.id
            )
            button_text = "Add"
            menu.save()
            msg = 'Successfully Add menu: คุณ %s' % (request.user.first_name)
        else:
            menu = Menu.objects.get(pk=menu_id)
            menu.menu_name=menu_name
            menu.description=description
            menu.menu_price=menu_price
            menu.save()
            return redirect(reverse('edit_menu', kwargs={'menu_id':menu.id}))
    context = {
        'msg': msg,
        'button_text':button_text
    }
    return render(request, template_name='add_menu.html', context=context)

@login_required
def edit_menu(request, menu_id):
    menu = ''
    msg = ''
    button_text = 'Edit'
    try:
        menu = Menu.objects.get(pk=menu_id)
    except:
        #not found message
        msg = 'not found'
    context = {
        'msg': msg,
        'menu': menu,
        'button_text': button_text
    }
    return render(request, template_name='add_menu.html', context=context)
    #return render(request, template_name='add_menu.html', context=context)
@login_required
def menu(request):
    shop = Shop.objects.filter(user_id_id=request.user.id)[0]
    menus = Menu.objects.filter(shop_id_id=shop.id)
    context = {
        'menus': menus
    }
    return render(request, template_name='menu.html', context=context)

@login_required
def topup(request):

    zones = Zone.objects.all()
    search = request.GET.get('search', '')

    members_search = Member.objects.filter(
        Q(first_name__startswith=search)
    )

    return render(request, template_name='topup.html', context={
        'member_search': members_search,
        'zones': zones,
        'search': search
    })


@login_required
def member_regis(request):
    msg = ''
    context = {}
    if request.method == 'POST':
        member_fname = request.POST.get('member_first_name')
        member_lname = request.POST.get('member_last_name')
        member = Member.objects.create(
            first_name=member_fname,
            last_name=member_lname,
            money=100
        )
        member.save()
        msg = 'Successfully registered Member: คุณ %s' % (member.first_name)
    else:
        context['error'] = 'Something went wrong please try again'

    context = {
        'msg': msg
    }
    
    return render(request, template_name='register_member.html', context=context)


@login_required
def check_in(request):
    booking = SeatBooking.objects.all()
    date_time_now = datetime.datetime.now()
    date_today = datetime.date.today()
    members = Member.objects.all()
    zones = Zone.objects.all()
    users = User.objects.all()
    member_name = request.POST.get('member_name')
    msg = ''
    # user = request.user.pk
    # member_id = members.filter(first_name=member_name).id

    if request.method == 'POST':
        seat_booking = SeatBooking.objects.create(
            member_id=request.POST.get('member_id'),
            zone_id=request.POST.get('zone_id'),
            create_by=request.user,
            time_check_in=request.POST.get(date_time_now),
            create_date=request.POST.get(date_today)
        )
        mem = Member.objects.filter(first_name=member_name).values('id')
        seat_booking.member_id = mem
        seat_booking.save()
        # msg = 'Successfully Check-in Member: คุณ %s เวลา: %s' % (
        #     members.filter(id=member_id).first_name, date_time_now.time().isoformat())
    else:
        seat_booking = SeatBooking.objects.none()

    context = {
        'users': users,
        'members': members,
        'seat_booking': seat_booking,
        'booking':booking,
        'zones': zones,
        'msg': msg
    }
    return render(request, template_name='index.html', context=context)


@login_required
def check_out(request):
    zones = Zone.objects.all()
    member_name = request.POST.get('member_name')
    mem = Member.objects.filter(first_name=member_name)
    mem_id = mem.values('id')
    mem_money = mem.values('money')
    booking = SeatBooking.objects.filter(member_id=mem_id)
    # time_in = SeatBooking.objects.get(member_id=mem_id).values('time_check_in')
    # zoneid = SeatBooking.objects.get(member_id=mem_id).values('zone_id')
    # booking_time_check_in = SeatBooking.objects.filter(member_id=mem_id).values('time_check_in')
    date_time_now = datetime.datetime.now()
    booking.update(time_check_out=date_time_now)
    context = {
        'zones': zones,
        'booking': booking
    }
    return render(request, template_name='index.html', context=context)


def calculate_total_price(zone_id, check_in_time, check_out_time):
    price = 0
    if zone_id == "1":
        price = 20
    elif zone_id == "2":
        price = 60
    elif zone_id == "3":
        price = 100

    seconds_input = (check_out_time-check_in_time).seconds
    time = str(datetime.timedelta(seconds=seconds_input)).split(':')
    hour = int(time[0])
    minute = int(time[1])

    if minute == 0:
        return hour*price
    else:
        return (hour+1)*price


@login_required
def search_member(request):
    zones = Zone.objects.all()
    booking = SeatBooking.objects.all()
    search = request.GET.get('search', '')

    members_search = Member.objects.filter(
        Q(first_name__startswith=search)
    )

    return render(request, template_name='index.html', context={
        'member_search': members_search,
        'zones': zones,
        'booking':booking,
        'search': search
    })


def index_log(request):
    booking = SeatBooking.objects.all()
    members = Member.objects.all()

    context = {
        'booking': booking,
        'members': members
    }
    return render(request, template_name='index.html', context=context)
