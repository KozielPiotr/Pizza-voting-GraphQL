"""
Schema for all project apps.
"""

import graphene

from pizza_poll.poll.schema import PollQuery


class Query(PollQuery):
    """
    Common query, inherits from apps queries.
    """

    pass


schema = graphene.Schema(query=Query)
