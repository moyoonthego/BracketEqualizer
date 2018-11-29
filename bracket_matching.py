# Leave as global vars, so we can add [ or { functionality later
CLOSE_BRACKET = ')'
OPEN_BRACKET = '('
MISMATCH1 = ')(('
MISMATCH2 = '))('

def solution(parentheses):
    '''
    (str) -> str
    This function takes a lines of braces, and checks to see if it's brackets
    are matching or not, adding them if needed.
    '''
    # NOTE: This program could easily be transferred to C# or java, but being
    # a simple function, it is best scripted in python
    # set up counters for how many start and ending parenthesis are missing
    open_count = 0;
    close_count = 0;
    output = parentheses
    # Base case:
    if (parentheses == ""):
        return output
    # Second base case:
    if (parentheses == ")("):
        return OPEN_BRACKET + output + CLOSE_BRACKET
    else:
        # get count of open and close brackets
        close_count = parentheses.count(CLOSE_BRACKET)
        open_count = parentheses.count(OPEN_BRACKET)
        # get count of mismatched brackets
        mismatched = parentheses.count(MISMATCH1) + parentheses.count(MISMATCH2)
        # add parentheses, so long as the count are not equal
        while (close_count != open_count):
            # close needed
            if (close_count < open_count):
                # close brackets can only be applied to end or beginning, so
                # obviously we will add to the end
                close_count+=1
                output = output + CLOSE_BRACKET

            # open needed
            elif (open_count < close_count):
                # brackets applied to end or beginning, so add open to beginning
                open_count+=1
                output = OPEN_BRACKET + output
        return output
