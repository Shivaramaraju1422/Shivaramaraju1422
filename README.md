# Exercise Set 0
### ex_0_0.py
Write a Python script named `ex_0_0.py` that prints the output `Hello World!`.

### ex_0_1.py
Write a Python script named `ex_0_1.py` that implements the following:

1. Assign the text string 1'Hello World!'1 to a variable named `greeting`.
2. Print the value stored in `greeting`.

### ex_0_2.py
Write a Python script named `ex_0_2.py` that implements the following:

1. Assign the text `addison` to a variable named 'first_name'
2. Assign the text `bellamy` to a variable named 'last_name'
3. Concatenate `first_name`, followed by a space, followed by `last_name` and assign the result to the variable `full_name`.
4. Use the appropriate string method on `full_name` so that the first letter of each name is capitalized. *Assign this value to a variable name `full_name_title`.*
5. Print the contents of the `full_name_title` variable.

For reference on applicable string methods, visit [this RealPython](https://realpython.com/python-strings/) article on the topic.

### ex_0_3.py
Write a Python script that contains a function `format_name` that
takes two positional arguments `first` and `last`.  The function
should *return* the full name in appropriate name casing (as in
`ex_0_2.py`).

*Note: your script should not print anything*

Here are two example runs from the Python REPL:
```
>>> format_name('addison', 'bellamy')
'Addison Bellamy'
>>> first_name = 'addison'
>>> last_name = 'bellamy'
>>> format_name(first_name, last_name)
'Addison Bellamy'
```

### ex_0_4.py
Write a Python module named ex_0_4.py that implements the
following. Note that your script should include two functions and the
script should not print anything.

*Tip: Run (or import) your Python

1. Define a function with name `int_sum` that takes one positional
   argument `n`.  Use a loop inside the function to calculate the sum
   of the fist `n` non-zero integers.

   Example run:

   ```
   >>> result = int_sum(5)
   >>> print(result)
   >>> 15
   ```

2. Define a function called `odd_sum` that takes one positional
   argument `n`. Use a loop inside the function to calculate the sum
   of the first `n` odd integers.*Note: any odd integer can be
   expressed as `2n + 1`*.  Which means that you can loop over the range `0, 1, ..., 
   n` and add `2n + 1` to your sum. 

   Example run:

   ```
   >>> result = odd_sum(5)
   >>> print(result)
   >>> 25
   ```


### ex_0_5.py
*Hint: this exercise is really about string indexing.*

Write a Python module named `ex_0_5.py` that solves the following
problem. The Global Historical Climatology Network uses a fixed length
file format. NOAA uses this format for reporting daily ground station
data. The format specification can be found
[here](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt). For
this exercise, we are only interested in one element, Minimum soil
temperature.  Minimum soil temperature (and maximum soil temperature)
elements are fixed length fields which begin with `SN` and end with a
two character code representing ground cover and depth code.  In this
exercise, you will extract these codes from the text element and
return them as integers.


In your `ex_0_5.py` module, write the following functions:

1. Function `ground_cover` takes one positional string argument and
   returns the ground cover code as an integer.
2. Function `depth` takes one positional string argument and returns
   the depth **code** as an integer.

Here's an example run (shown from the interactive prompt):

```
>>> min_soil_temp = 'SN07'
>>> ground_cover(min_soil_temp)
0
>>> depth(min_soil_temp)
7
```


Here's the full description of the minimum soil temperature element.

```
SN*# = Minimum soil temperature (tenths of degrees C)
	          where * corresponds to a code
	          for ground cover and # corresponds to a code for soil
		  depth.

		  Ground cover codes include the following:
		  0 = unknown
		  1 = grass
		  2 = fallow
		  3 = bare ground
		  4 = brome grass
		  5 = sod
		  6 = straw multch
		  7 = grass muck
		  8 = bare muck

		  Depth codes include the following:
		  1 = 5 cm
		  2 = 10 cm
		  3 = 20 cm
		  4 = 50 cm
		  5 = 100 cm
		  6 = 150 cm
		  7 = 180 cm
```
