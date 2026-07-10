from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import F, Sum
from django.urls import reverse
from .models import Counter


# Create your views here.
def index(request):
    counter, created = Counter.objects.get_or_create(user=request.user)

    counter.refresh_from_db()

    sum_counters = Counter.objects.aggregate(
        sum_counters = Sum("count")
    )["sum_counters"] or 0
    return render(request, "click/button.html",
                  {
                      "sum_counters": sum_counters,
                      "counter": counter,
                  })

def click(request):
    counter, created = Counter.objects.get_or_create(user=request.user)
    if request.method == "POST":
        counter.count = F("count") + 1 # Counter.objects.filter(pk=1).update(count=F("count") + 1)
        counter.save()                 # idk if it would work the same way
        counter.refresh_from_db()
        return HttpResponseRedirect(reverse("button"))
