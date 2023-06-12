#!/usr/bin/python3


"""
The Function for MyInt class that inherits from int.
"""


class MyInt(int):
    """
    A Cless MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        This overrides equality operator.
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        This overrides inequality operator.
        """

        return super().__eq__(other)
