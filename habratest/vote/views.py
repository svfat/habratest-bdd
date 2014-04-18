from django.shortcuts import render_to_response

from django.views.generic import ListView
from models import VoteItem

class VoteListView(ListView):
    model=VoteItem
    template_name="list.html"


def addvote(request, pk):
    item = VoteItem.objects.get(pk=pk)
    item.rating += 1
    item.save()
    return render_to_response('successful.html')