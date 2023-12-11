def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    print("Hello World!")

    # Returning the docstring
    return greeting.__doc__

# Calling the function
greeting()
