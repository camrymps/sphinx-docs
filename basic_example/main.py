import random


def print_hello_world(include_world=True):
    """A function for printing the text "Hello world!"

    :param include_world: Optional - weather or not to include "world" in the printed output
    :type include_world: bool
    :see: "Describing code in Sphinx" - https://www.sphinx-doc.org/en/master/tutorial/describing-code.html
    """
    if include_world == False:
        print("Hello!")
    else:
        print("Hello world!")


def random_number(range=None):
    """A function that returns a random number

    :param range: Range (ex: [1, 100])
    :type range: int[]
    :return: A randomly generated number
    :rtype: int
    """
    return random.randint()
