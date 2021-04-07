import turtle

def main():
    t1 = turtle.Turtle()
    wm = turtle.Screen()
    commands = {
        'forward': turtle.forward,
        'backwards': turtle.backward,
        'left': turtle.left,
        'right': turtle.right,
        'split': turtle.split
    }
    with open(input('instructions file for processing please - Turtle 115'), 'r') as instructions:
        for instruction in instructions:  # for line in intructions_file
            # split the line into command, pixels
            instruction, pixels = instruction.split()

            # If the parsed instruction is in `commands`, then run it.
            if instruction in commands:
                commands[instruction](pixels)
            else:
            # If it's not, then raise an error.
                raise()
if __name__ == "__main__":
    main()