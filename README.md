Contains `analyzeblocks.py`, a python 3 script for analyzing
blocked threads in java thread dumps.

When provided with a list of files containing java thread 
dumps the script will run through all files compiling a count 
of how many threads are blocked wating on each object. 

The output looks like this:

```sh
python3 analyzeblocks.py file1 file2 file3 file4

10ade7d0     2     2     0     2
1ede540d     0     0     0     1
23f9a1f4     1     1     1     1
24018082     1     1     1     0
10ade7d0     2     2     0     2
1ede540d     0     0     0     1
23f9a1f4     1     1     1     1
```

We can see in the output above that there are 2
 objects that have threads waiting for them in all 
four thread dumps suggesting that this object is 
being held for a relatively long time.
