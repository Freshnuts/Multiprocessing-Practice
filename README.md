# Multiprocessing-Practice

A script repository focusing on multiprocessing functions, methodologies,<br>
practices, and standards.

<h1>mp_loop</h1>

Program creates a loop on multiple processes threads.<br>
<br>
Options:
1. t1 - Calls multiprocessing.Process().
2. t1loop - Initializes multiprocessing.Process(). Aka - Calls looper()<br>
   on a seperate thread. NO LOCK.
3. t1join - Lock thread AFTER t1 is initiated by t1loop. 

When the loop is active on Process #1, you can still access the menu.<br>
<br>
p01.start()
<br>
4. t1lock - Lock thread from the beginning.<br>
<br>
p01.start() # Start the process thread.
p01.join()  # Lock the process thread, until it is finished.
5. t2 - Creates thread #2.
6. t2loop - Starts the thread, and runs the loop function.
't1shell' initializes the t1 process thread. 't1join' can be run<br>
AFTER 't1shell' starts 't1' running the loop. 't1lock' is used in <br>
replacement of 't1shell' to LOCK the running process until it's finished.<br>

