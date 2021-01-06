#!/usr/bin/env python

import angr
from IPython import embed
from traceback import print_stack as bt

# variables address
KEY = 0x301010
A = 0x301014
B = 0x301018

var_list = {
    KEY: 'KEY',
    A: 'A',
    B: 'B',
}

def mem_read(state):
    addr = state.solver.eval(state.inspect.mem_read_address)
    if addr in var_list:
        # key - Set this to a tuple of increasingly specific identifiers (for example, ('mem', 0xffbeff00) or ('file', 4, 0x20)) 
        # to cause it to be tracked, i.e. accessable through solver.get_variables.
        # http://angr.io/api-doc/angr.html#angr.state_plugins.solver.SimSolver.BVS
        state.inspect.mem_read_expr = state.solver.BVS(var_list[addr], state.inspect.mem_read_length*8, key=('var', 0))

if __name__ == "__main__":

    p = angr.Project('./test', main_opts={'base_addr': 0x100000})
    e_state = p.factory.entry_state()
    e_state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS)
    e_state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)


    e_state.inspect.b('mem_read', action=mem_read, when=angr.BP_AFTER)

    sm = p.factory.simulation_manager(e_state)


    sm.run()

    for s in sm.deadended:
        print('---')
        print(s.solver.constraints)
        
        # angr uses key ('mem', addr, 1) to track some symbols(all symbols UNINITIALIZED)
        # I dont know where these symbols are used
        symbols = s.solver.get_variables('var')
        for var in symbols:
            print('%s eval to %x' % (var[1], s.solver.eval(var[1])))

    print('angr is going to terminate!')
    embed()
