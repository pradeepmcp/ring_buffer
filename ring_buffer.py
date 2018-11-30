## @package ring_buffer
#  simple ring buffer class.
#
#  Size of buffer passed during class instantiation.
#  The buffer has overflow and underflow flags.
#  Overflow and underflow are cleared automatically based on the buffer __read or write operations.
class ring_buffer:
    
    ## The constructor
    def __init__(self, size):
        self.__free=0
        self.__read=0
        self.data=[]
        self.size=size
        self.overflow=False
        self.underflow=True
        self.overflow_count=0
        self.underflow_count=0
        self.__watch_for_overflow=False
        
    ## Appends element at the end of the buffer
    # @elem element to be appended to the buffer.
    def append(self, elem, count=0):
        self.data.append(elem)
        self.__free = (self.__free + 1) % self.size
                
        if self.__free <= self.__read:
            self.__watch_for_overflow = True
        
        if (self.__watch_for_overflow == True and self.__free > self.__read):
            self.overflow = True;
    
        if self.underflow == True:
            self.underflow = False

    ## pops the elem from the buffer as a return value
    # @return element popped from the buffer.
    def get_elem(self, count=0):
        if(self.__read < self.__free):
            self.__watch_for_overflow = False
            
        if (self.__read == self.__free):
            if self.overflow == True:
                self.elem = self.data[self.__read]
                self.__read = (self.__read + 1) % self.size
                self.overflow = False
                return self.elem
            else: 
                self.underflow = True
                raise EOFError("Buffer empty")
        else:
            self.elem = self.data[self.__read]
            self.__read = (self.__read + 1) % self.size
            return self.elem
