def delete_nth(order,max_e):
    out = []
    for item in order:
        if out.count(item) < max_e:
            out.append(item)
    return out