from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField('State Name', max_length=63)
    slug = models.SlugField()
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

    #TODO fill in the functions below
    def get_complete_relations(self, relation_type):
        """
        This method returns all relations that are mutual between this state and any other
        state. If a relation_type is set then it only returns mutual relations of that 
        relation type.
        """
        pass
    
    def get_outgoing_relations(self, relation_type):
        """
        This method returns all relations from this state to another state.  If a 
        relation_type is set then it only returns outgoing relations of that relation 
        type.
        """
        pass
    
    def get_incoming_relation(self, relation_type):
        """
        This method returns all relations to this state from another state. If a 
        relation_type is set then it only returns incoming relations of that relation
        type."""
        pass
        
class Issue(models.Model):
    problem = models.TextField()
    
class Option(models.Model):
    issue = models.ForeignKey(Issue)
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
    from_state = models.ForeignKey(State, related_name='following_set')
    to_state = models.ForeignKey(State, related_name='follower_set')
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




            
    