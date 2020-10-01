"""
Queries for 'polls' app schema.
"""

import graphene

from graphene_django.filter import DjangoFilterConnectionField

from .types import PizzaType, ToppingType, VoteType


class PizzaQuery(graphene.ObjectType):
    """
    Query functions for a Pizza model.
    """

    single_pizza = graphene.relay.node.Field(PizzaType)
    all_pizzas = DjangoFilterConnectionField(PizzaType)


class ToppingQuery(graphene.ObjectType):
    """
    Query functions for a Topping model.

    """

    name = graphene.String()

    single_topping = graphene.relay.node.Field(ToppingType)
    all_toppings = DjangoFilterConnectionField(ToppingType)


class VoteQuery(graphene.ObjectType):
    """
    Query functions for a Topping model.
    """

    single_vote = graphene.relay.node.Field(VoteType)
    all_votes = DjangoFilterConnectionField(VoteType)


class PollQuery(PizzaQuery, ToppingQuery, VoteQuery):
    """
    Common app query.
    """

    pass
