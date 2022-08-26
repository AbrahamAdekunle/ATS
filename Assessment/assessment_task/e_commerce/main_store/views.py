from django.db.models import Q
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category, Item, OrderedItem, Cart, WishList, Checkout
from .forms import CheckoutForm


# Create your views here.


def get_cart_total(pk):
    cart = Cart.active_objects.filter(user_id=pk).first()
    ordered_items = cart.ordered_items.all()
    prices = 0

    for item in ordered_items:
        prices += item.item.get_real_price() * item.quantity

    return prices


def index(request):
    sales = []
    categories = Category.objects.all()

    search = request.GET.get("search") if request.GET.get("search") is not None else ""

    items = Item.objects.filter(Q(name__icontains=search) | Q(sub_category__category__name__icontains=search))

    all_settled_carts = Cart.objects.filter(is_checked_out=True)

    for cart in all_settled_carts:
        for goods in cart.ordered_items.all():
            sales.append(goods)
    print(sales)

    context = {
        "categories": categories,
        "items": items,
        "sales": sales
    }
    return render(request, "main_store/index.html", context)


def add_to_cart(request, pk):
    if request.user.is_authenticated:
        marked_item = Item.objects.get(id=pk)
        ordered_item, created = OrderedItem.active_objects.get_or_create(user=request.user, item=marked_item)
        selected_cart = Cart.active_objects.filter(user=request.user).first()

        if selected_cart is not None:
            if ordered_item in selected_cart.ordered_items.all():
                ordered_item.quantity += 1
                ordered_item.save()
                messages.success(request, f'{ordered_item} added successfully')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                selected_cart.ordered_items.add(ordered_item)
                messages.success(request, f'{ordered_item} added successfully')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            new_cart = Cart.objects.create(user=request.user, )
            new_cart.ordered_items.add(ordered_item)
            new_cart.save()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:
        marked_item = Item.objects.get(id=pk)
        ordered_item, created = OrderedItem.active_objects.get_or_create(session=request.session.session_key,
                                                                         item=marked_item
                                                                         )
        selected_cart = Cart.active_objects.filter(session=request.session.session_key).first()

        if selected_cart is not None:
            if ordered_item in selected_cart.ordered_items.all():
                ordered_item.quantity += 1
                ordered_item.save()
                messages.success(request, f'{ordered_item} added successfully')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                selected_cart.ordered_items.add(ordered_item)
                messages.success(request, f'{ordered_item} added successfully')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        else:
            new_cart = Cart.objects.create(
                session=request.session.session_key,
                ordered_items=OrderedItem.objects.add(ordered_item),
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="nucleus:sign_in")
def remove_from_cart(request, pk, id):
    if request.user.id != pk:
        return HttpResponseForbidden()

    selected_cart = Cart.active_objects.filter(user_id=pk).first()
    selected_item = OrderedItem.active_objects.get(user_id=pk, item_id=id)

    selected_cart.ordered_items.remove(selected_item)
    selected_item.save()

    selected_item.quantity = 1
    selected_item.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="nucleus:sign_in")
def order_summary(request, pk):
    if request.user.id != pk:
        return HttpResponseForbidden()

    selected_cart = Cart.active_objects.filter(user_id=pk).first()
    user_wishlist = WishList.objects.get(user_id=pk)
    selected_wishlist = user_wishlist.saved_items.all()
    if selected_cart is not None:
        ordered_items = selected_cart.ordered_items.all()
        total = get_cart_total(pk)

        context = {
            "ordered_items": ordered_items,
            "cart": selected_cart,
            "total": total,
            "wishlist": selected_wishlist,
        }
        return render(request, "main_store/cart_summary.html", context)
    else:
        messages.error(request, "Cart is empty")
        return HttpResponseRedirect(reverse("main_store:index"))


@login_required(login_url="nucleus:sign_in")
def reduce_quantity(request, pk, id):
    if request.user.id != pk:
        return HttpResponseForbidden()

    selected_item = OrderedItem.active_objects.get(user_id=pk, item_id=id)
    if selected_item.quantity > 1:
        selected_item.quantity -= 1
        selected_item.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    messages.error(request, f"{selected_item} quantity can't go below 1, You could remove it instead ")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="nucleus:sign_in")
def increase_quantity(request, pk, id):
    if request.user.id != pk:
        return HttpResponseForbidden()

    selected_item = OrderedItem.active_objects.get(user_id=pk, item_id=id)
    selected_item.quantity += 1
    selected_item.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="nucleus:sign_in")
def saved_items(request, pk, id):
    user_wishlist, created = WishList.objects.get_or_create(user_id=pk)
    item = Item.objects.get(id=id)

    if item not in user_wishlist.saved_items.all():
        user_wishlist.saved_items.add(item)
        messages.error(request, f"{item.name} saved in wish list")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    user_wishlist.saved_items.remove(item)
    messages.error(request, f"{item.name} removed from wish list")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="nucleus:sign_in")
def user_checkout(request, pk):
    if request.user.id != pk:
        return HttpResponseForbidden()

    # TRY AND APPLY TIMEDELTA AMD TIMEZONE
    form = CheckoutForm()
    selected_cart = Cart.active_objects.filter(user_id=pk).first()
    items = selected_cart.ordered_items.all()
    total = get_cart_total(pk)

    if request.method == "POST":
        form = CheckoutForm(request.POST, request.FILES)

        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.user = request.user
            checkout.save()

            selected_cart.is_checked_out = True
            selected_cart.save()

            messages.success(request, "Your goods will be delivered to you within 3 working days")
            return HttpResponseRedirect(reverse("main_store:index"))

        messages.error(request, "kindly check the form, invalid details")

    context = {
        "form": form,
        "items": items,
        "total": total
    }
    return render(request, "main_store/checkout_form.html", context)
