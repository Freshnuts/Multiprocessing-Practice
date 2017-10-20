# Multiprocessing-Practice

A script repository focusing on multiprocessing functions, methodologies,<br>
practices, and standards.

<h1>mp_loop</h1>

Program creates a loop on multiple processes threads.<br>
1. t1 - Calls multiprocessing.Process().
2. t1loop - Initializes multiprocessing.Process(). Aka - Calls looper()<br>
   on a seperate thread. NO LOCK.
3. t1join - Lock thread AFTER t1 is initiated by t1loop. 

When the loop is active on Process #1, you can still access the menu.<br>
p01.start()<br>
4. t1lock - Lock thread from the beginning.<br>
<br>
p01.start() # Start the process thread.<br>
p01.join()  # Lock the process thread, until it is finished.<br>
5. t2 - Creates thread #2.<br>
6. t2loop - Starts the thread, and runs the loop function.

