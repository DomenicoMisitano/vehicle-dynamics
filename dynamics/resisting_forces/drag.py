def drag_force(density, c_drag, area, relativevelocity):
    drag = - 0.5 * density * area * c_drag * relativevelocity * abs(relativevelocity)
    return drag
