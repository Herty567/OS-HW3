# OS-HW3
The design of this code is a thread-safe concurrent linked list using Python. The three main operations
are insert (adds nodes in the list), search, (searches for the node value), and delete (removes the first
node in the list that matches a given value. It makes sure to feature thread safety and concurrency to
get through the benchmarks.

How to run the code is have a Python IDE (I use PyCharm) and paste the code in and run. This should lead
to different workloads being tested (low, medium, high) and how long each of those operations take.

The analysis was that after simulating random linked list using the three main operations and 4 threads
the execution time would be shown to observe the performance under these workloads. As the work load got 
intensive the time taken to execute would increase. This is happening because more threads are trying to 
access the locks on the shared resources cause more execution time.
