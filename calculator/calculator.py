class Calculator():
    """
    Calculator class with multiple arithmetic capabilities, storing the total value in a running memory that can be reset.

    Attributes:
        _memory (float): Calculator's current value.
        _precision (int): Calculator's precision setting.

    Methods:
        add(num): 
            Adds num to value stored in memory
        subtract(num): 
            Subtracts num to value stored in memory     
        multiply(num): 
            Multiplies num to value stored in memory
        divide(num): 
            Divides value stored in memory by num
        root(n): 
            Takes n-th root of the value stored in memory
        equals(): 
            Returns value stored in memory
        reset(): 
            Resets object's memory value to 0
    """
    def __init__(self, memory: float = 0, precision: int = 4) -> None:
        """
        Initializes the calculator with starting memory.
        
        Args:
            memory (float): Initial memory value. Starts with 0.
            precision (int): Precision / number of digits after the decimal. Set at 4.
        """
        self._memory = memory
        self._precision = precision


    def __str__(self) -> str:
        """
        Returns a string representation of the calculator's value.

        Returns:
            str: String showing current value.
        """
        return f'memory: {self._memory}, precision: {self._precision}'
    

    def add(self, num: float) -> None:
        """
        Adds a number to the current value.

        Args:
            num (float): Number to add.
        """
        self._memory += num
    

    def subtract(self, num: float) -> None:
        """
        Subtracts a number from the current value.

        Args:
            num (float): Number to subtract.
        """
        self._memory -= num
    

    def multiply(self, num: float) -> None:
        """
        Multiplies a number with the current value.

        Args:
            num (float): Number to multiply.
        """
        self._memory *= num
    

    def divide(self, num: float) -> None:
        """
        Divides the current value by a number.

        Args:
            num (float): Number to divide by.

        Raises:
            ValueError: If attempting to divide by 0.
        """
        if num == 0:
            raise ValueError("Cannot divide by 0")
        self._memory /= num
    

    def root(self, n: int) -> None:
        """
        Takes (n) root of the current value.

        Args:
            num (int): The n root.

        Raises: 
            ValueError: If attempting to root by 0 or by an even number when value is negative.
        """
        if n == 0:
            raise ValueError("The root 'n' cannot be 0")
        if self._memory < 0 and n % 2 == 0:
            raise ValueError("Cannot take even root of a negative number")
        self._memory = self._memory ** (1/float(n))
    

    @property
    def memory(self) -> float:
        """
        Getter method to access memory and control read access.

        Returns:
            float: Current memory value.
        """
        return self._memory
    

    @memory.setter
    def memory(self, memory: float) -> None:
        """
        Setter method to update memory and control write access.

        Args:
            memory (float): The new value to set to memory.
        """
        self._memory = float(memory)

    
    @property
    def precision(self) -> int:
        """
        Returns the current precision setting and controls read access.

        Returns:
            int: Precision setting
        """
        return self._precision

    
    @precision.setter
    def precision(self, p: int) -> None:
        """
        Validates and sets the precision setting.

        Args:
            p (int): Precision value to set.

        Raises:
            ValueError: If attempting to set a float, negative number or precision more than 6.
        """
        if isinstance(p, int) and 0 <= p <= 6:
            self._precision = p
        else:
            raise ValueError("Precision must be an integer between 0 and 6 inclusive")


    def equals(self) -> float:
        """
        Returns the current memory value rounded to the set precision. This method emulates pressing '=' on a calculator.
        
        Returns:
            float: Current memory value.
        """
        return round(self._memory, self._precision)
    

    def reset(self) -> float:
        """
        Resets memory to 0. Similar to pressing 'C' on a calculator.

        Returns:
            float: 0
        """
        self._memory = 0
        return self._memory