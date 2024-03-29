from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

# Create your views here.
def index(request):
    context = {
        'day_list':Day.objects.all(),
    }
    return render(request, 'diary/day_list.html', context)

def add(request):
    form = DayCreateForm(request.POST or None)

    #methodがPOSTで、データも正しい場合
    if request.method == 'POST' and form.is_valid():
        form.save()
        #postがうまくいったらredirectさせないと、二重投稿される原因になる
        return redirect('diary:index')

    context = {
        'form': DayCreateForm()
    }
    return render(request, 'diary/day_form.html', context)

def update(request, pk):
    day = get_object_or_404(Day, pk=pk)
    #pkのなかにあるものだったらobjectを返すし、なかったら404
    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html', context)

def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)
    #pkのなかにあるものだったらobjectを返すし、なかったら404

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')
    context = {
        'day':day
    }
    return render(request, 'diary/day_confirm_delete.html', context)

def detail(request, pk):
    day = get_object_or_404(Day, pk=pk)
    #pkのなかにあるものだったらobjectを返すし、なかったら404

    context = {
        'day':day
    }
    return render(request, 'diary/day_detail.html', context)
