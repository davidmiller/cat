"""
cat

Package init file
"""
from _version import __version__

class Box(object):
    """
    A class that adheres to the Heisenberg interpretation of
    Quantum Mechanics.

    Consider: an object is locked in a box.
    The object is either a list or a set. It is entangled.
    When we observe it in a way that is definitively set-like,
    say we ask for it's intersection, we Open The Box.
    At this point, it resolves itself into a set, and will remain a set
    in perpetuity.

    Why is this useful you ask?
    Well if you have to ask, then you almost certainly won't find the
    answer satisfying.
    If on the other hand you're the kind of person who responds to this
    with:
      "*excellent* - I want to do That Sort Of Thing all the time"
    then congratulations - now you can.
    """
    def __new__(klass):
        klass.__mro__ = klass.box

