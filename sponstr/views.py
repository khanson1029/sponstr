from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from sponstr.models import Sponsor
from django.template.loader import get_template
from iommi import *
from .models import Sponsor

class SponsorPage(Page):
    template = get_template('sponsorship_workflow/base.html')
    sponsors = EditTable(
        auto__model=Sponsor,
        title=None,
        container__attrs={
        "class":
            {
                'pt-5': True,
                'fw-b':True
            }
        },
        columns__delete=Column.delete(
            attr=None,
            include=lambda request, **_: True,  
            cell__url=lambda row, **_: f'sponsorsdelete/{row.pk}', 
       ),
        actions__save={
            'display_name': None,
            'post_handler': lambda request, table, **_: table.save(request),
        },
    )


def index(request):
    print('Request for index page received')
    sponsors=Sponsor.objects.all()
    in_cash = 0
    in_kind = 0
    total = 0
    sponsor_count = 0
    for sponsor in sponsors:
        total += sponsor.spend
        sponsor_count += 1
        print(sponsor.spend)
        
    return render(request, 'sponsorship_workflow/index.html', {'total_spend':total, 'sponsor_count':sponsor_count})


def sponsors(request):
    print('Request for sponsors page received')
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsorship_workflow/sponsors.html', context)


def sponsor_update(request):
    print('Request for sponsors page received')
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsorship_workflow/sponsors.html', context)


def sponsorsdelete(request,id):
    print("hello")
    # Retrieve and delete the sponsor
    sponsor = get_object_or_404(Sponsor, pk=id)
    sponsor.delete()
    # Redirect back to your SponsorPage (replace 'sponsor_page' with your actual URL name)
    return render(request, 'sponsorship_workflow/sponsors.html')



@cache_page(60)
def details(request, id):
    print('Request for sponsor details page received')
    sponsor = get_object_or_404(Sponsor, pk=id)
    return render(request, 'sponsorship_workflow/details.html', {'sponsor': sponsor})


def create_sponsor(request):
    print('Request for add sponsor page received')
    return render(request, 'sponsorship_workflow/create_sponsor.html')


@csrf_exempt
def add_sponsor(request):
    try:
        company = request.POST['company_name']
        contact = request.POST['contact']
        email = request.POST['email']
        phone = request.POST['phone']
        status = request.POST['status']
        spend = request.POST['spend']
    except (KeyError):
        # Redisplay the form
        return render(request, 'sponsorship_workflow/add_restaurant.html', {
            'error_message': "You must include a restaurant name, address, and description",
        })
    else:
        sponsor = Sponsor()
        sponsor.company_name = company
        sponsor.contact = contact
        sponsor.email = email
        sponsor.phone_number = phone
        sponsor.status = status
        sponsor.spend = spend
        Sponsor.save(sponsor)

        return HttpResponseRedirect(reverse('sponsors'))
    
def sponsor_data_update(request):
    print('hello')