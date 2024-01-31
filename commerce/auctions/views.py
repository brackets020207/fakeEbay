from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import listing_form, bidding_form

from .models import User, Listing, Comment, Bid



def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form_data = listing_form(request.POST)
        if form_data.is_valid():
            new_listing = Listing(
                title = form_data.cleaned_data['title'],
                description = form_data.cleaned_data['description'],
                current_price = form_data.cleaned_data['start_price'],
                image_url = form_data.cleaned_data['img_url'],
                category = form_data.cleaned_data['category'],
                user = request.user
            )
            new_listing.save()
    return render(request, "auctions/create.html", {
        "form": listing_form()
        })

def view_listing(request, listing_id):
    if request.method == "POST": 
        if request.POST['submit_bid']:
            cur_listing = Listing.objects.get(id = listing_id)
            form_data = bidding_form(request.POST)
            if form_data.is_valid():                    
                if form_data.cleaned_data['bid_price'] > cur_listing.current_price:
                    cur_listing.current_price = form_data.cleaned_data['bid_price']
                    cur_listing.save()
                    new_bid = Bid(price = form_data.cleaned_data['bid_price'], listing = cur_listing, user = request.user)
                    new_bid.save()

    return render(request, "auctions/listing.html", {
            "listing": Listing.objects.get(id = listing_id),
            "bid_form": bidding_form()
        })