"""
Create a function which returns the state of a board after n moves
"""


def block_pushing(start_list: list, number: int):
    """
    Create a function which returns the state of a board after n moves. There are different types of blocks on the board, which are represented as strings.

    > is a pusher which moves right every turn, and pushes a block to the right if it occupies the same space as it.
    '#' is a block which can be pushed by the pusher. If a block is pushed onto another block, then the other block also joins the push chain!
    '-' is an empty space, which a block can be pushed into.
    Note that the pusher can push any number of blocks at a time, but is always stopped if the push chain hits the end of the list.
    Examples
    block_pushing(['-', '>', '#', '-', '#', '-', '-', '-'], 1) ➞ ['-', '-', '>', '#', '#', '-', '-', '-']

    block_pushing(['>', '#', '-', '#', '-', '-', '#'], 10) ➞ ['-', '-', '-', '>', '#', '#', '#']

    block_pushing(['>', '-', '>', '#', '-', '-', '#', '-'], 2) ➞ ['-', '-', '>', '-', '>', '#', '#', '-']

    block_pushing(['>', '>', '>', '-'], 3) ➞ ['-', '>', '>', '>']
    Notes
    There may be more than one pusher at a time on the board.
    Pushers are solid blocks, so a push chain of pushers should also stop when hitting the end of the list.
    5 <= len(lst) <= 500
    """
    pusher = ">"
    space = "-"

    for _ in range(number):
        pusher_indexes = [
            index for index, value in enumerate(start_list) if value == pusher
        ]
        for pusher_index in pusher_indexes:
            try:
                space_pos = pusher_index + start_list[pusher_index:].index(space)

                next_pusher = any(
                    index > pusher_index and index < space_pos
                    for index in pusher_indexes
                )
                if next_pusher:
                    next_pushers = [
                        index
                        for index, value in enumerate(
                            start_list[pusher_index + 1 : space_pos]
                        )
                        if value == pusher
                    ]
                    for i in next_pushers:
                        pusher_indexes.remove(pusher_index + 1 + i)
                start_list.pop(space_pos)
                start_list.insert(pusher_index, space)
            except ValueError:
                pass

    return start_list


if __name__ == "__main__":
    lst = ["#", ">", "#", "-", "-", ">", ">", ">", "-", "#", "-", "-"]
    block_pushing(lst, 2)
