#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Computer:
    
    def __init__(self, state, inputs=None):
        self.state = state
        self.inputs = inputs or []
        self.outputs = []
        self.running = True
        self.i = 0
        self.out_log = []
        self.relative_base = 0
        self.waiting_input = False
        self.debug = False
        
    def print_debug(self, text):
        if self.debug is True:
            print(text)
            
    def write_value(self, i, mode, value):
        if str(mode) is '2':
            self.state[self.relative_base + self.state[i]] = value
        self.state[self.state[i]] = value
        
    def read_value(self, i, mode):
        if str(mode) is '1':
            return self.state[i]
        if str(mode) is '2': 
            return self.state[self.relative_base + self.state[i]]
        return self.state[self.state[i]]

    def add(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.write_value(self.i+3, modes.get(2, 0), a+b)
        self.i+=4
        return True
    
    def multiply(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.write_value(self.i+3, modes.get(2, 0), a*b)
        self.i+=4
        return True
    
    def val_in(self, modes):
        if not self.inputs:
            self.waiting_input = True
            return True
        self.waiting_input = False
        x = self.inputs.pop(0)
        self.write_value(self.i+1, modes.get(0, 0), x)
        self.i+=2
        return True
    
    def val_out(self, modes):
        o = self.read_value(self.i+1, modes.get(0, 0))
        self.outputs.append(o)
        self.out_log.append(o)
        self.i+=2
        return True
    
    def jump_true(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.i = self.i+3 if a == 0 else b
        return True
        
    def jump_false(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.i = b if a == 0 else self.i+3
        return True
        
    def less_than(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.write_value(self.i+3, modes.get(2, 0), 1 if a < b else 0)
        self.i+=4
        return True
        
    def equals(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        b = self.read_value(self.i+2, modes.get(1, 0))
        self.write_value(self.i+3, modes.get(2, 0), 1 if a == b else 0)
        self.i+=4
        return True
    
    def add_relative_base(self, modes):
        a = self.read_value(self.i+1, modes.get(0, 0))
        self.relative_base += a
        self.i+=2
        return True
        
    def kill(self, modes):
        self.outputs.append("KILL")
        return False
                              
    def fail(self, se, modes):
        print(f"Unknown operation: {self.state[self.i:self.i+4]} Exiting...")
        return False
    
    operations = {
        1: add,
        2: multiply,
        3: val_in,
        4: val_out,
        5: jump_true,
        6: jump_false,
        7: less_than,
        8: equals,
        9: add_relative_base,
        99: kill
    }
    
    def tick(self):
        op = int(str(self.state[self.i])[-2:])
        modes = {i:x for i, x in enumerate(str(self.state[self.i])[:-2][::-1])}
        try:
            return self.operations.get(op, self.fail)(self, modes)
        except IndexError as e:
            self.state = self.state + [0 for x in range(len(self.state))]
            return True
                
    def run_program(self):
        running = True
        while(running):
            running = self.tick()
        return self.state
    


# In[ ]:




