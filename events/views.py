from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm
from datetime import date

def event_list(request):
    query = request.GET.get('q')
    events = Event.objects.select_related('category').prefetch_related('participants').annotate(
        participant_count=Count('participants')
    )
    if query:
        events = events.filter(Q(name__icontains=query) | Q(location__icontains=query))
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(
        Event.objects.select_related('category').prefetch_related('participants'),
        pk=event_id
    )
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'participant_form.html', {'form': form})

def participant_update(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participant_form.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def organizer_dashboard(request):
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=date.today()).count()
    past_events = Event.objects.filter(date__lt=date.today()).count()
    today_events = Event.objects.filter(date=date.today())

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'today_events': today_events
    }
    return render(request, 'dashboard.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})


def organizer_dashboard(request):
    show = request.GET.get('show', 'events')  # default to total events

    total_participants = Participant.objects.all()
    total_events = Event.objects.all()
    upcoming_events = Event.objects.filter(date__gte=date.today())
    past_events = Event.objects.filter(date__lt=date.today())
    today_events = Event.objects.filter(date=date.today())

    context = {
        'total_participants_count': total_participants.count(),
        'total_events_count': total_events.count(),
        'upcoming_events_count': upcoming_events.count(),
        'past_events_count': past_events.count(),

        'show': show,
        'total_participants': total_participants if show == 'participants' else None,
        'total_events': total_events if show == 'events' else None,
        'upcoming_events': upcoming_events if show == 'upcoming' else None,
        'past_events': past_events if show == 'past' else None,
        'today_events': today_events if show == 'today' else None,
    }
    return render(request, 'dashboard.html', context)

