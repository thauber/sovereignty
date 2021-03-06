from django.views.generic.list_detail import object_detail
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from nationstates.models import *

def nation(request, state_slug):
    return object_detail(
        State.objects.all(),
        slug=nation_slug,
        template_name='nationstates/state.html')

@login_required
def issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    form = IssueForm(issue, request.POST or None)
    if form.is_valid():
        choice = IssueChoice.objects.get(id=form.cleaned_data['solutions'])
        user.state.make_choice(issue, choice)
        

def stats(request, state_slug):
    return object_detail(
        State.objects.all(),
        slug=state_slug,
        template_name='nationstates/state_stats.html')

@login_required
def home(request):
    try:
        Nation.get.object(user=request.user)
    except Nation.DoesNotExist, e:
        raise e

def relation_list(request, relation_type, state_slug, template_name="nationstates/relation_list.html"):

    state = get_object_or_404(State, slug=state_slug)
    context = {
        'list_type': list_type,
        'complete_relations': state.get_complete_relations(relation_type),
        'outgoing_relations': state.get_outgoing_relations(relation_type),
        'incoming_relations': state.get_incoming_relations(relation_type)
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
    )

def relate(request, state_slug, relation_type, template_name="nationstates/relate.html"):
    """
    Adds a "following" edge from the authenticated user to the user specified by
    the state_slug in the URL.
    """
    state = get_object_or_404(State, slug=state_slug)
    rel, created = Relation.objects.get_or_create(from_state=request.user.state, 
        to_state=state)
    # next = _get_next(request)    
    # TODO write _get_next
    # if next and next != request.path:
    #     request.user.message_set.create(
    #         #TODO add RELATION_PLURALS to models
    #         message=_('You are now %s with %s') % (RELATION_PLURALS[relation_type], state)
    #     return HttpResponseRedirect(next)
    context = {
        'other_state': state,
        'created': created,
        'relation_type': relation_type
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
    )
relate = login_required(relate)

def unrelate(request, state_slug, relation_type, template_name="nationstates/unrelate.html"):
    """
    Removes a "following" edge from the authenticated user to the user specified
    by the state_slug in the URL.
    """
    state = get_object_or_404(State, slug=state_slug)
    try:
        rel = Relation.objects.get(from_state=request.user.state, to_state=state)
        rel.delete()
        deleted = True
    except UserLink.DoesNotExist:
        deleted = False
    # TODO write _get_next
    # next = _get_next(request)
    # if next and next != request.path:
    #     request.user.message_set.create(
    #         message=_('You are no longer %s with %s') % (RELATION_PLURALS[relation_type], state)
    #     return HttpResponseRedirect(next)
    context = {
        'other_state': state,
        'deleted': deleted,
        'relation_type': relation_type,
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
    )
unrelate = login_required(unrelate)

#Possible Names?
# causus edlli
# hoplites
# phalanx
# peltast

