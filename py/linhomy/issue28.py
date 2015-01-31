def compose_2(n):
    '''Yield all non-negative solutions to i + j = n.
    '''

    m = n + 1
    for i in range(m):
            yield i, n - i



def iter_deltas(size_vec):
    '''Yield changes contributed by size_vec.

    '''
    length = len(size_vec)

    if length == 0:
        raise ValueError

    if length == 1:
        yield [[0, 0]]
        return

    # Iterate over how many available for use.
    avail = size_vec[0]
    for used in range(avail + 1):

        # Based on number used, set up done and todo.
        done = ((used, used),)
        todo = size_vec[1:]
        carried = used

        yield from recurse_deltas(done, carried, todo)


def recurse_deltas(done, carried, todo):

    avail = todo[0]             # Should never fail.

    if len(todo) == 1:          # End recursion.

        # Iterate over available for use.
        for used in range(avail + 1):

            # Compute and yield, based on used and carried.
            # Need to use all of carried here.
            suffix = (used, 2 * used + carried)
            yield done + (suffix,)

        return                  # Done.


    # Store previous values, prior to recursion.
    prev_done = done
    prev_carried = carried
    todo = todo[1:]

    for used in range(avail + 1):

        for kept, carried in compose_2(prev_carried + used):

            suffix = (used, used + kept)
            done = prev_done + (suffix,)
            yield from recurse_delta(done, carried, todo)
