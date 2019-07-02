from Memory import *
from Reader import *
from Executor import *

memory = Memory()
reader = Reader(memory)
executor = Executor(memory)
memory.consolePrintMemory()
reader.launch()
memory.consolePrintMemory()
executor.executor()
memory.consolePrintMemory()
memory.consolePrintBuffer()