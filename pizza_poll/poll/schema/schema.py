"""
Schema for 'poll' queries.
"""

import graphene

from .queries import PollQuery


schema = graphene.Schema(query=PollQuery)
