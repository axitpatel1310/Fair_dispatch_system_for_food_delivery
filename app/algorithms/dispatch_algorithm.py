def select_rider(order_zone, riders, metrics):

    candidates = []

    for rider in riders:

        deliveries = metrics.get(rider.id, 0)

        candidates.append((rider, deliveries))

    candidates.sort(key=lambda x: x[1])

    return candidates[0][0]