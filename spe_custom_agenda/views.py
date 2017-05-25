from datetime import datetime
from icalendar import Calendar, Event
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404

from .models import CustomAgendaItems


def export(request, agenda_id):
    event = get_object_or_404(CustomAgendaItems, id = agenda_id)

    cal = Calendar()
    site = Site.objects.get_current()

    cal.add('prodid', '-//%s Events Calendar//%s//' % (site.name, site.domain))
    cal.add('version', '2.0')

    site_token = site.domain.split('.')
    site_token.reverse()
    site_token = '.'.join(site_token)

    ical_event = Event()
    ical_event.add('location', event.location)
    ical_event.add('summary', event.title)
    # ical_event.add('description', event.session_description)
    start = datetime.combine(event.start_date, event.start_time)
    ical_event.add('dtstart', start)
    end = datetime.combine(event.start_date, event.end_time)
    ical_event.add('dtend', end and end or start)
    ical_event.add('dtstamp', end and end or start)
    ical_event['uid'] = '%d.event.events.%s' % (event.id, site_token)
    cal.add_component(ical_event)

    response = HttpResponse(cal.to_ical(), content_type="text/calendar")
    response['Content-Disposition'] = 'attachment; filename=%s.ics' % event.slug
    return response