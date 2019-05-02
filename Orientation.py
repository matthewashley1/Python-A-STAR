

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import Checking


# Determines direction choice to take when snake is going in the down direction!
def orientation_down(snake, food):

    event = KEY_DOWN

    snake_above = []
    snake_right = []
    snake_left = []

    for x in range(len(snake)):
        if x >= 3:
            snake_above.append([(snake[x][0] - 1), snake[x][1]])
            snake_right.append([snake[x][0], (snake[x][1] + 1)])
            snake_left.append([snake[x][0], (snake[x][1] - 1)])

    if (snake[0][0] == food[0]) or (food[0] < snake[0][0]):
        if food[1] > snake[0][1]:
            event = KEY_RIGHT

            if snake[0] in snake_left[1:]:
                event = KEY_DOWN

        elif food[1] < snake[0][1]:
            event = KEY_LEFT

            if snake[0] in snake_right[1:]:
                event = KEY_DOWN

        # else:
        #     if snake[0] not in snake_left[1:]:
        #         event = KEY_RIGHT
        #
        #     elif snake[0] not in snake_right[1:]:
        #         event = KEY_LEFT

    if snake[0] in snake_above[1:]:

        if Checking.check_left(snake) and Checking.check_right(snake):

            if Checking.distance_left(snake) > Checking.distance_right(snake):
                event = KEY_LEFT

                if Checking.check_enclosed(snake, "Left", "Down"):
                    event = KEY_RIGHT

                    if snake[0] in snake_left[1:]:
                        event = KEY_LEFT

            else:
                event = KEY_RIGHT

                if Checking.check_enclosed(snake, "Right", "Up"):
                    event = KEY_LEFT

                    if snake[0] in snake_right[1:]:
                        event = KEY_RIGHT

        elif Checking.check_left(snake):
            event = KEY_RIGHT

            if snake[0][1] == 58:
                event = KEY_LEFT

        elif Checking.check_right(snake):
            event = KEY_LEFT

            if snake[0][1] == 1:
                event = KEY_RIGHT

        else:
            event = KEY_RIGHT

    if snake[0][0] == 18:

        if Checking.check_enclosed(snake, "Left", "Down") and Checking.check_enclosed(snake, "Right", "Down"):
            if Checking.distance_wall_left(snake) > Checking.distance_wall_right(snake):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

            else:
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

        elif Checking.check_enclosed(snake, "Left", "Down"):
            event = KEY_RIGHT

            if snake[0][1] == 58:
                event = KEY_LEFT

        elif Checking.check_enclosed(snake, "Right", "Down"):
            event = KEY_LEFT

            if snake[0][1] == 1:
                event = KEY_RIGHT

        else:
            if Checking.distance_wall_left(snake) > Checking.distance_wall_right(snake):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

            else:
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

    if event == KEY_LEFT:
        if Checking.check_left(snake) and Checking.check_right(snake):
            if Checking.check_enclosed(snake, "Left", "Down"):
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

    if event == KEY_RIGHT:
        if Checking.check_left(snake) and Checking.check_right(snake):
            if Checking.check_enclosed(snake, "Right", "Down"):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

    return event


# Determines direction choice to take when snake is going in the up direction!
def orientation_up(snake, food):

    event = KEY_UP

    snake_below = []
    snake_right = []
    snake_left = []

    for x in range(len(snake)):
        if x >= 3:
            snake_right.append([snake[x][0], (snake[x][1] + 1)])
            snake_below.append([(snake[x][0] + 1), snake[x][1]])
            snake_left.append([snake[x][0], (snake[x][1] - 1)])

    if (snake[0][0] == food[0]) or (food[0] > snake[0][0]):
        if food[1] > snake[0][1]:
            event = KEY_RIGHT

            if snake[0] in snake_left[1:]:
                event = KEY_UP

        elif food[1] < snake[0][1]:
            event = KEY_LEFT

            if snake[0] in snake_right[1:]:
                event = KEY_UP

        # else:
        #     if snake[0] not in snake_left[1:]:
        #         event = KEY_RIGHT
        #
        #     elif snake[0] not in snake_right[1:]:
        #         event = KEY_LEFT

    if snake[0] in snake_below[1:]:

        if Checking.check_left(snake) and Checking.check_right(snake):

            if Checking.distance_left(snake) > Checking.distance_right(snake):
                event = KEY_LEFT

                if Checking.check_enclosed(snake, "Left", "Up"):
                    event = KEY_RIGHT

                    if snake[0] in snake_left[1:]:
                        event = KEY_LEFT

            else:
                event = KEY_RIGHT

                if Checking.check_enclosed(snake, "Right", "Up"):
                    event = KEY_LEFT

                    if snake[0] in snake_right[1:]:
                        event = KEY_RIGHT

        elif Checking.check_left(snake):
            event = KEY_RIGHT

            if snake[0][1] == 58:
                event = KEY_LEFT

        elif Checking.check_right(snake):
            event = KEY_LEFT

            if snake[0][1] == 1:
                event = KEY_RIGHT

        else:
            event = KEY_RIGHT

    if snake[0][0] == 1:

        if Checking.check_enclosed(snake, "Left", "Up") and Checking.check_enclosed(snake, "Right", "Up"):
            if Checking.distance_wall_left(snake) > Checking.distance_wall_right(snake):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

            else:
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

        elif Checking.check_enclosed(snake, "Left", "Up"):
            event = KEY_RIGHT

            if snake[0][1] == 58:
                event = KEY_LEFT

        elif Checking.check_enclosed(snake, "Right", "Up"):
            event = KEY_LEFT

            if snake[0][1] == 1:
                event = KEY_RIGHT

        else:
            if Checking.distance_wall_left(snake) > Checking.distance_wall_right(snake):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

            else:
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

    if event == KEY_LEFT:
        if Checking.check_left(snake) and Checking.check_right(snake):
            if Checking.check_enclosed(snake, "Left", "Up"):
                event = KEY_RIGHT

                if snake[0] in snake_left[1:]:
                    event = KEY_LEFT

    if event == KEY_RIGHT:
        if Checking.check_left(snake) and Checking.check_right(snake):
            if Checking.check_enclosed(snake, "Right", "Up"):
                event = KEY_LEFT

                if snake[0] in snake_right[1:]:
                    event = KEY_RIGHT

    return event


# Determines direction choice to take when snake is going in the left direction!
def orientation_left(snake, food):

    event = KEY_LEFT

    snake_above = []
    snake_below = []
    snake_right = []

    for x in range(len(snake)):
        if x >= 3:
            snake_above.append([(snake[x][0] - 1), snake[x][1]])
            snake_right.append([snake[x][0], (snake[x][1] + 1)])
            snake_below.append([(snake[x][0] + 1), snake[x][1]])

    if (snake[0][1] == food[1]) or (food[1] > snake[0][1]):
        if food[0] > snake[0][0]:
            event = KEY_DOWN

            if snake[0] in snake_above[1:]:
                event = KEY_LEFT

        elif food[0] < snake[0][0]:
            event = KEY_UP

            if snake[0] in snake_below[1:]:
                event = KEY_LEFT

        # else:
        #     if snake[0] not in snake_above[1:]:
        #         event = KEY_DOWN
        #
        #     elif snake[0] not in snake_below[1:]:
        #         event = KEY_UP

    if snake[0] in snake_right[1:]:

        if Checking.check_up(snake) and Checking.check_down(snake):

            if Checking.distance_up(snake) > Checking.distance_down(snake):
                event = KEY_UP

                if Checking.check_enclosed(snake, "Up", "Left"):
                    event = KEY_DOWN

                    if snake[0] in snake_above[1:]:
                        event = KEY_UP

            else:
                event = KEY_DOWN

                if Checking.check_enclosed(snake, "Down", "Left"):
                    event = KEY_UP

                    if snake[0] in snake_below[1:]:
                        event = KEY_DOWN

        elif Checking.check_up(snake):
            event = KEY_DOWN

            if snake[0][0] == 18:
                event = KEY_UP

        elif Checking.check_down(snake):
            event = KEY_UP

            if snake[0][0] == 1:
                event = KEY_DOWN

        else:
            event = KEY_DOWN

    if snake[0][1] == 1:

        if Checking.check_enclosed(snake, "Up", "Left") and Checking.check_enclosed(snake, "Down", "Left"):
            if Checking.distance_wall_top(snake) > Checking.distance_wall_bottom(snake):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

            else:
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

        elif Checking.check_enclosed(snake, "Up", "Left"):
            event = KEY_DOWN

            if snake[0][0] == 18:
                event = KEY_UP

        elif Checking.check_enclosed(snake, "Down", "Left"):
            event = KEY_UP

            if snake[0][0] == 1:
                event = KEY_DOWN

        else:
            if Checking.distance_wall_top(snake) > Checking.distance_wall_bottom(snake):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

            else:
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

    if event == KEY_UP:
        if Checking.check_up(snake) and Checking.check_down(snake):
            if Checking.check_enclosed(snake, "Up", "Left"):
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

    if event == KEY_DOWN:
        if Checking.check_up(snake) and Checking.check_down(snake):
            if Checking.check_enclosed(snake, "Down", "Left"):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

    return event


# Determines direction choice to take when snake is going in the right direction!
def orientation_right(snake, food):

    event = KEY_RIGHT

    snake_above = []
    snake_below = []
    snake_left = []

    for x in range(len(snake)):
        if x >= 3:
            snake_above.append([(snake[x][0] - 1), snake[x][1]])
            snake_below.append([(snake[x][0] + 1), snake[x][1]])
            snake_left.append([snake[x][0], (snake[x][1] - 1)])

    if (snake[0][1] == food[1]) or (food[1] < snake[0][1]):
        if food[0] > snake[0][0]:
            event = KEY_DOWN

            if snake[0] in snake_above[1:]:
                event = KEY_RIGHT

        elif food[0] < snake[0][0]:
            event = KEY_UP

            if snake[0] in snake_below[1:]:
                event = KEY_RIGHT

        # else:
        #     if snake[0] not in snake_above[1:]:
        #         event = KEY_DOWN
        #
        #     elif snake[0] not in snake_below[1:]:
        #         event = KEY_UP

    if snake[0] in snake_left[1:]:

        if Checking.check_up(snake) and Checking.check_down(snake):

            if Checking.distance_up(snake) > Checking.distance_down(snake):
                event = KEY_UP

                if Checking.check_enclosed(snake, "Up", "Right"):
                    event = KEY_DOWN

                    if snake[0] in snake_above[1:]:
                        event = KEY_UP

            else:
                event = KEY_DOWN

                if Checking.check_enclosed(snake, "Down", "Right"):
                    event = KEY_UP

                    if snake[0] in snake_below[1:]:
                        event = KEY_DOWN

        elif Checking.check_up(snake):
            event = KEY_DOWN

            if snake[0][0] == 18:
                event = KEY_UP

        elif Checking.check_down(snake):
            event = KEY_UP

            if snake[0][0] == 11:
                event = KEY_DOWN

        else:
            event = KEY_DOWN

    if snake[0][1] == 58:

        if Checking.check_enclosed(snake, "Up", "Right") and Checking.check_enclosed(snake, "Down", "Right"):
            if Checking.distance_wall_top(snake) > Checking.distance_wall_bottom(snake):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

            else:
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

        elif Checking.check_enclosed(snake, "Up", "Right"):
            event = KEY_DOWN

            if snake[0][0] == 18:
                event = KEY_UP

        elif Checking.check_enclosed(snake, "Down", "Right"):
            event = KEY_UP

            if snake[0][0] == 1:
                event = KEY_DOWN

        else:
            if Checking.distance_wall_top(snake) > Checking.distance_wall_bottom(snake):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

            else:
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

    if event == KEY_UP:
        if Checking.check_up(snake) and Checking.check_down(snake):
            if Checking.check_enclosed(snake, "Up", "Right"):
                event = KEY_DOWN

                if snake[0] in snake_above[1:]:
                    event = KEY_UP

    if event == KEY_DOWN:
        if Checking.check_up(snake) and Checking.check_down(snake):
            if Checking.check_enclosed(snake, "Down", "Right"):
                event = KEY_UP

                if snake[0] in snake_below[1:]:
                    event = KEY_DOWN

    return event


