from Memory import *
from Reader import *
from Executor import *
memory = Memory()
reader = Reader(memory)
executor = Executor(memory)
memory.consolePrintMemory()
reader.launch()
executor.executor()
memory.consolePrintMemory()