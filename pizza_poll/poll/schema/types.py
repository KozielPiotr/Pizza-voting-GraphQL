"""
Types for 'polls' app schema.
"""

import graphene

from django.db.models import Count

from graphene_django import DjangoObjectType

from pizza_poll.poll.models import Pizza, Topping, Vote


class PizzaType(DjangoObjectType):
    """
    Returns info about of the pizza.
    """

    class Meta:
        model = Pizza
        interfaces = (graphene.relay.Node,)
        fields = []
        filter_fields = {"id": ["exact"]}

    votes_count = graphene.Int()
    toppings = graphene.List(graphene.String)

    def resolve_votes_count(self, info):
        """
        Counts number of votes casted on the pizza.
        """
        return self.votes.count()

    def resolve_toppings(self, info):
        """
        List of related toppings names (as the list of strings).
        """
        return [topping.name for topping in self.toppings.all()]


class ToppingType(DjangoObjectType):
    """
    Returns details of the topping.
    """

    class Meta:
        model = Topping
        interfaces = (graphene.relay.Node,)
        fields = ["name"]
        filter_fields = {"name": ["exact", "icontains"]}

    votes_count = graphene.Int()

    def resolve_votes_count(self, info):
        """
        Counts sum of votes casted for pizzas with the topping
        """
        return self.pizzas.aggregate(Count("votes"))["votes__count"]


class VoteType(DjangoObjectType):
    """
    Returns details of the vote.
    """

    pizza_composition = graphene.List(graphene.String)

    def resolve_pizza_composition(self, info):
        return [topping.name for topping in self.pizza.toppings.all()]

    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node,)
        fields = ["timestamp"]
        filter_fields = ["id", "timestamp"]
