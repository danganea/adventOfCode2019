def run_program(program):
        at = 0
        add_func  = lambda x,y: x + y
        mult_func = lambda x,y: x * y
        while at < len(program):
            op_number = program[at]
            #Process opcodes
            func = type(None)
            if op_number == 99:
                break
            elif op_number == 1:
                func = add_func
            elif op_number == 2:
                func = mult_func
            
            program[program[at + 3]] = func(program[program[at + 1]], program[program[at + 2]])
            
            at += 4
def main():
    with open("input.txt","r") as fp:

        #Parse program
        line = fp.readline()
        program = [int(x) for x in line.rstrip().split(',')]
        for x in range(0,100):
            for y in range(0,100):
                new_program = program.copy()
                new_program[1] = x
                new_program[2] = y
                run_program(new_program)
                if new_program[0] == 19690720 :
                    print(100 * x + y)
        run_program(program)


        # print(program)
            
main()
