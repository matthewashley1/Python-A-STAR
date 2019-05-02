

# Checks if head of snake is encircled by body of snake!
def check_for_encircle(snaking):

    down_left = False
    down_right = False
    up_left = False
    up_right = False

    for x in range(len(snaking)):
        if snaking[x][0] > snaking[0][0] and snaking[x][1] < snaking[0][1]:
            down_left = True
        if snaking[x][0] > snaking[0][0] and snaking[x][1] > snaking[0][1]:
            down_right = True
        if snaking[x][0] < snaking[0][0] and snaking[x][1] < snaking[0][1]:
            up_left = True
        if snaking[x][0] < snaking[0][0] and snaking[x][1] > snaking[0][1]:
            up_right = True

    if down_left and down_right and up_left and up_right:
        return True
    else:
        return False


# Checks if X or Y direction of playing grid is blocked by snake body!
def check_for_blockage(snaking):

    status = False

    x_count = 0
    y_count = 0

    for x in range(20):
        for z in range(len(snaking)):
            if snaking[z][0] == x:
                x_count = x_count + 1
                break

    for y in range(59):
        for h in range(len(snaking)):
            if snaking[h][1] == y:
                y_count = y_count + 1
                break

    if x_count == 18 or y_count == 58:
        status = True

    return status


# Checks if direction choice is blocked in choice of direction and previous direction!
def check_enclosed(snaking, wish, direction):

    status = False

    if wish == "Up":
        if direction == "Left":
            for z in range(len(snaking)):
                if snaking[z][0] == (snaking[0][0] - 1):
                    if snaking[0][1] < snaking[z][1]:
                        status = True

        if direction == "Right":
            for z in range(len(snaking)):
                if snaking[z][0] == (snaking[0][0] - 1):
                    if snaking[0][1] > snaking[z][1]:
                        status = True

    if wish == "Down":
        if direction == "Left":
            for z in range(len(snaking)):
                if snaking[z][0] == (snaking[0][0] + 1):
                    if snaking[0][1] < snaking[z][1]:
                        status = True

        if direction == "Right":
            for z in range(len(snaking)):
                if snaking[z][0] == (snaking[0][0] + 1):
                    if snaking[0][1] > snaking[z][1]:
                        status = True

    if wish == "Left":
        if direction == "Up":
            for z in range(len(snaking)):
                if snaking[z][1] == (snaking[0][1] - 1):
                    if snaking[0][0] < snaking[z][0]:
                        status = True

        if direction == "Down":
            for z in range(len(snaking)):
                if snaking[z][1] == (snaking[0][1] - 1):
                    if snaking[0][0] > snaking[z][0]:
                        status = True

    if wish == "Right":
        if direction == "Up":
            for z in range(len(snaking)):
                if snaking[z][1] == (snaking[0][1] + 1):
                    if snaking[0][0] < snaking[z][0]:
                        status = True

        if direction == "Down":
            for z in range(len(snaking)):
                if snaking[z][1] == (snaking[0][1] + 1):
                    if snaking[0][0] > snaking[z][0]:
                        status = True

    return status


# Checks if body of snake is in the down direction!
def check_down(snaking):

    status = False

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][1] == snaking[z][1]:
                if snaking[0][0] < snaking[z][0]:
                    status = True

    return status


# Checks if body of snake is in the up direction!
def check_up(snaking):

    status = False

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][1] == snaking[z][1]:
                if snaking[0][0] > snaking[z][0]:
                    status = True

    return status


# Checks if body of snake is in the left direction!
def check_left(snaking):

    status = False

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][0] == snaking[z][0]:
                if snaking[0][1] > snaking[z][1]:
                    status = True

    return status


# Checks if body of snake is in the right direction!
def check_right(snaking):

    status = False

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][0] == snaking[z][0]:
                if snaking[0][1] < snaking[z][1]:
                    status = True

    return status


# Calculates the amount of move spaces between the head of the snake and the body of the snake in the down direction!
def distance_down(snaking):

    distance = 0

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][1] == snaking[z][1]:
                if snaking[0][0] < snaking[z][0]:
                    distance = snaking[z][0] - snaking[0][0]
                    break

    return distance


# Calculates the amount of move spaces between the head of the snake and the body of the snake in the up direction!
def distance_up(snaking):

    distance = 0

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][1] == snaking[z][1]:
                if snaking[0][0] > snaking[z][0]:
                    distance = snaking[0][0] - snaking[z][0]
                    break

    return distance


# Calculates the amount of move spaces between the head of the snake and the body of the snake in the left direction!
def distance_left(snaking):

    distance = 0

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][0] == snaking[z][0]:
                if snaking[0][1] > snaking[z][1]:
                    distance = snaking[0][1] - snaking[z][1]
                    break

    return distance


# Calculates the amount of move spaces between the head of the snake and the body of the snake in the right direction!
def distance_right(snaking):

    distance = 0

    for z in range(len(snaking)):
        if z > 0:
            if snaking[0][0] == snaking[z][0]:
                if snaking[0][1] < snaking[z][1]:
                    distance = snaking[z][1] - snaking[0][1]
                    break

    return distance


# Calculates amount of move spaces between the head of the snake and the wall of the playing grid in the up direction!
def distance_wall_top(snaking): return snaking[0][0]


# Calculates amount of move spaces between the head of the snake and the wall of the playing grid in the down direction!
def distance_wall_bottom(snaking): return 19 - snaking[0][0]


# Calculates amount of move spaces between the head of the snake and the wall of the playing grid in the left direction!
def distance_wall_left(snaking): return snaking[0][1]


# Calculates amount of move spaces between the head of the snake and the wall of the playing grid in the right direction!
def distance_wall_right(snaking): return 59 - snaking[0][1]

