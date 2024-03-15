Boyle
# Lab 06 - Intro to Numpy

Spyder comes with the numpy library. The numpy library allows data scientists
to do many convenient operations in python that are not built in to the regular
language. In this lab, you will practice using numpy to do descriptive
computations on a small data set.

Review the slides from March 11 and read the assigned
[Chapter 2 on Describing Data](https://ebookcentral.proquest.com/lib/allegheny-ebooks/reader.action?docID=1729064&ppg=31)

## Objectives

1. Use Spyder
2. Copy python code using numpy
3. Understand statistical data descriptors
4. Add original code to complete computations for quartiles


## Check a Spyder setting

Everyone, please verify a certain Sypder setting: 
TODO: click Spyder>preferences>editor>advanced settings>End-of-line characters
TODO: ensure that both little boxes are checked for `fix automatically` and
`convert on save`. 
TODO: ensure the drop down menu is set to `LF (unix)`
TODO: click `Apply` and `OK`

## Write out python code using numpy

TODO: fill out the following python files:

1. `vocal_data.py`
2. `calculate_mean.py`
3. `calculate_range.py`
4. `calculate_variance.py`
5. `calculate_standard_deviation.py`
6. `calculate_mode.py`
7. `calculate_median.py`
8. `calculate_quartiles.py`

NB: there may be TODOs within the files that you should read and implement. As
you work, delete all the TODO markers. For this lab, gatorgrade is only
checking that all TODO markers are removed, including from this README.md file.


## Run your code

Begin by clearing your console memory - there is a small trash icon for this,
or you can x out of the console. After the memory is clear, run the
`vocal_data.py` file. If implemented correctly, it should create four python
variables that store the data. Please verify that the python variables are
created in the `Variable Explorer` before continuing.

If the four variables are created, please run your calculation scripts. For
each script, you should put in one python variable at a time into the console
when it prompts you to `"write down the name of the variable to use:"`. So
for every script, you will run it four times using a different data variable as
input each time.

As you go, please fill out the following table which will be useful for
your blog post. If you don't know how to fill out a markdown table, reference
an online resource. The presentation of your work matters - illegible tables
as rendered in GitHub will not be graded.


| Variable Used | Mean | Mode | Variance | SD | Median | Range | Lower Quartile | Upper Quartile | Interquartile Range |
|---------------|------|------|----------|----|--------|-------|----------------|----------------|----------------------|


## Write a blog post

TODO: In blogpost.md, please write about all the following items in your own
words. Writing that is not original will not be graded.

- Which calculations are about central tendencies and why?
- Which calculations are about distributions of the data and why?
- Are mean, median, and mode giving you the same information?
- Why is median commonly used to describe the income of a group of people?
- What does it mean if variance is large?
- What was something you learned by writing the code?

Please include (a copy of) the filled out table, and make reference to it in
your writing as needed.

If you used external resources, please cite them at the end of the blog post
where lists of citations belong. No specific style is required, but please
provide enough information to properly credit the source and allow others to
find the source.


## Submit your work on GitHub


Before the deadline of March 18th at 11:500am, transfer your completed lab to
GitHub by using `git`.

In a terminal, use `cd` to change directories into the directory for this lab.
Then type:

- `git add .`
- `git commit -m "Short message about your work (5-10 words)"`
- `git push origin main`

DO NOT USE A MIXTURE OF GIT AND GITHUB EDITING WITHOUT A FRIEND WHO KNOWS HOW
TO MIX THEM AND RESOLVE MERGE CONFLICTS. MY ADVICE IS TO STICK WITH GIT!

## Review your work on GitHub

Please review your submission to ensure that it is clean work. Also review the
gatorgrade report in the GitHub Actions to make sure the baseline
requirements for this lab are met. Above the baseline, work is graded for

- clean work with few careless errors
- correct Markdown, code, and/or data not already gatorgraded
- correct images given the context of the lab
- correct explanations of concepts in writing
