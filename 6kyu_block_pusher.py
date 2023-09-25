def block_pushing(lst, n):
    pusher = ">"
    space = "-"

    for move in range(n):
        pusher_indexes = [index for index, value in enumerate(lst) if value == pusher]
        for pusher_index in pusher_indexes:
            try:
                space_pos = pusher_index + lst[pusher_index:].index(space)

                next_pusher = any(
                    index > pusher_index and index < space_pos
                    for index in pusher_indexes
                )
                if next_pusher:
                    next_pushers = [
                        index
                        for index, value in enumerate(lst[pusher_index + 1 : space_pos])
                        if value == pusher
                    ]
                    for i in next_pushers:
                        pusher_indexes.remove(pusher_index + 1 + i)
                lst.pop(space_pos)
                lst.insert(pusher_index, space)
            except ValueError:
                pass

    return lst


if __name__ == "__main__":
    lst = ["#", ">", "#", "-", "-", ">", ">", ">", "-", "#", "-", "-"]
    block_pushing(lst, 2)
