from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField('State Name', max_length=63)
    slug = models.SlugField()
    user = models.OneToOneField(User)
    description = models.TextField('Description of State')
    
    industry = models.IntegerField()
    economy = models.IntegerField()
    social_freedom = models.IntegerField()
    political_freedom = models.IntegerField()
    religion = models.IntegerField()
    education = models.IntegerField()
    environment = models.IntegerField()
    employment = models.IntegerField()
    crime = models.IntegerField()
    health = models.IntegerField()
    military = models.IntegerField()
    happiness = models.IntegerField()
    
    motto = models.CharField('National Motto', max_length=255)
    animal = models.CharField('State Animal', max_length=63)
    currency = models.CharField('State Currency', max_length=63)

    def make_choice(self, issue, solution):
        StateChoice(issue=issue, choice=choice, state=self).save()
    
    def get_complete_relations(self, relation_type=None):
        """
        This method returns all States that have a mutual relation with this 
        state. If a relation_type is set then it only returns mutual relations of that 
        relation type.
        """
        outgoing = Relationship.objects.filter(from_state=self).values_list('to_state',
            flat=True)
        incoming = Relationship.objects.filter(to_state=self).values_list('from_state',
            flat=True)
        return State.objects.filter(id__in=set(outgoing).intersection(set(incoming)))
    
    def get_outgoing_relations(self, relation_type=None):
        """
        This method returns all States that have an incoming relation from this
        state. If a relation_type is set then it only returns outgoing relations
        of that relation type.
        """
        return State.objects.filter(relationship__from_state = self)
    
    def get_incoming_relation(self, relation_type=None):
        """
        This method returns all States that have an outgoing relation to this
        state. If a relation_type is set then it only returns incoming relations
        of that relation type.
        """
        return State.objects.filter(relationship__to_state = self)

class StateChoice(models.Model):
    issue = models.ForeignKey(Issue)
    choice = models.ForeignKey(IssueChoice)
    state = models.ForeignKey(State)
    

class Issue(models.Model):
    problem = models.TextField()
    
class IssueChoice(models.Model):
    issue = models.ForeignKey(Issue, related_name='solutions')
    solution = models.TextField()
    
    
class Ruler(models.Model):
    user = models.ForeignKey(User)
    power = models.IntegerField()
    money = models.IntegerField()
    corruption = models.IntegerField()
    rank = models.IntegerField()
    title = models.CharField(max_length = 63)

RELATION_CHOICES=(
    ('a','ally'),
    ('e','enemy')
)
    

class Relationship(models.Model):
    """
    A single directed edge in the social graph.  Usually represented as the
    verb "follows".
    """
    from_state = models.ForeignKey(State)
    to_state = models.ForeignKey(State)
    date_added = models.DateTimeField(default=datetime.now)
    relation = models.CharField(max_length=1, choices=RELATION_CHOICES)
    
    def __unicode__(self):
        return "%s is following %s" % (self.from_user.username, 
            self.to_user.username)

    def save(self, **kwargs):
        """
        A mostly-generic save method, except that it validates that the user
        is not attempting to follow themselves.
        """
        if self.from_user == self.to_user:
            raise ValueError("Cannot follow yourself.")
        super(UserLink, self).save(**kwargs)
    
    class Meta:
        unique_together = (('to_user', 'from_user'),)


ALLOW_ALL = "Allow All"
ALLOW_SOME = "Allow Some"
ENDORSE_SOME = "Endorse Some"
DISALLOW_SOME = "Disallow Some"
DISALLOW_ALL = "Disallow All"

((0,ALLOW_ALL)
 (1,ALLOW_SOME)
 (2,ENDORSE_SOME)
 (3,DISALLOW_SOME)
 (4,DISALLOW_ALL))

class Decree(models.Model):
    """
    A topic with a decree with it.  This is best explained through example. The
    topic could be pets, and the decree could be, from the list of decree
    choices, ALLOW_SOME.  This means that all described pets in  are allowed.
    the described pets are in a variable called list.  List is a many to one
    link to DecreeItems.
    
    For more help we will look at all of the choices for decree. For all of
    these examples assume that `Pet` is the topic
    
    The five choices are ALLOW_ALL, ALLOW_SOME, ENDORSE_SOME, DISALLOW_SOME, and
    DISALLOW_ALL.
    
    ALLOW_ALL: This does not have a list, it means that all types of pets are
    allowed for the denoted state.
    
    ALLOW_SOME: This is accompanied with a list, it means that only the pets on
    the list are allowed in the denoted state.
    
    ENDORSE_SOME: This is accompanied with a list, it means that any pet is
    allowed, but only the ones on the list are politically endorsed by the
    denoted state.
    
    DISALLOW_SOME: This is accompanied with a list, it means that all pets are
    allowed, except for those found on the list in the denoted state.
    
    DISALLOW_ALL: This does not have a list, it means that no types of pets are
    allowed in the denoted state.
    """
    state = models.ForeignKey(State)
    decree = models.IntegerField()
    topic = models.CharField(max_length=63)
    
class DecreeItem(models.Model):
    decree = models.ForeignKey(Decree, related_name='list')
    item = models.CharField(max_length=63)
    
    
    