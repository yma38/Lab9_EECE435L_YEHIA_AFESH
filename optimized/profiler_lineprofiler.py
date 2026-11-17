from line_profiler import LineProfiler
from profiler import slow_function, optimized_fast_function, memory_intensive_function, main

if __name__ == "__main__":
    lp = LineProfiler()
    lp.add_function(slow_function)
    lp.add_function(optimized_fast_function)
    lp.add_function(memory_intensive_function)
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()