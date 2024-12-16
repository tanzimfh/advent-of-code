from collections import defaultdict

prereqs = defaultdict(set)
postreqs = defaultdict(set)
orders = []

with open("input.txt") as f:
    for line in f:
        if "|" in line:
            prereq, page = map(int, line.split("|"))
            prereqs[page].add(prereq)
            postreqs[prereq].add(page)
        elif "," in line:
            orders.append(list(map(int, line.split(","))))


def is_valid(order):
    unallowed = set()
    for page in order:
        if page in unallowed:
            return False
        unallowed.update(prereqs[page])
    return True


ans = 0
for order in orders:
    if is_valid(order):
        continue

    new_order = []
    num_prereqs = {page: len(prereqs[page].intersection(order)) for page in order}
    cur_postreqs = {page: postreqs[page].intersection(order) for page in order}
    next_pages = [page for page in order if num_prereqs[page] == 0]

    while len(new_order) < len(order):
        for page in next_pages:
            new_order.append(page)
            for postreq in cur_postreqs[page]:
                num_prereqs[postreq] -= 1
                if num_prereqs[postreq] == 0:
                    next_pages.append(postreq)
    ans += new_order[len(new_order) // 2]
print(ans)
