import streamlit as st
import pandas as pd
from load_css import local_css


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

local_css("css/style.css")

st.title("Python Workshop Format")

st.markdown("""

## DSL Python workshops
            
### Workshop Format

The primary focus of our workshops is to support you in developing skills and strategies that will enable you to continue to learn programming 
and related digital skills independently. Our lessons are designed as projects which are broken down into a series of smaller, more maneagble tasks. 
To solve these tasks, you will use the same resources that coders around the world rely on when they don't know how to do something – 
online resources/tools, colleagues, and trial and error.
            
Our workshops are each two-hours long and follow an open-format, which means that you can choose which topic to work on. It is advised to work through the materials 
in order unless you are already familiar with a particular topic.


### The Python Fundamentals workshops series

The Python Fundamentals workshops are for beginners that have no prior experience in programming with Python and cover the following topics:

- Numerical variables
- String variables
- Converting types
- Lists
- For loops
- Conditionals
- Writing functions
- Dictionaries
- While loops
- Final Coding Challenges

&nbsp; 
            
Each of the notebooks will take you roughly 1 hour to complete. We estimate that the average learner will required 10-12 hours to complete 
all topics excluding the final coding challenge, which will take another 1-3 hours to complete.
            
The workshops will be run on a regular basis through September and early October. 
            
Dates and times for the in-person workshops:  

| Day        | Date              | Time     | Location |
|------------|-------------------|----------|----------|
| Tuesday    | 30 September 2025 | 13:30-15:30 | R08      |
| Thursday   | 02 October 2025   | 10:30-12:30 | R08      |
| Wednesday  | 08 October 2025   | 10:00-12:00 | R08      |
| Thursday   | 09 October 2025   | 13:00-15:00 | R08      |
| Monday     | 13 October 2025   | 11:00-13:00 | R08      |
| Wednesday  | 15 October 2025   | 14:00-16:00 | R08      |
| Wednesday  | 22 October 2025   | 14:00-16:00 | R08      |
| Friday     | 24 October 2025   | 10:30-12:30 | R08      |

&nbsp;

<div class="highlight red">
Sign ups for the Python workshops will be available from a week before start of term.
<br>
<br>
There are a limited number of spaces available for each session!
<br>
<br> 
<b>Please use 
<a href="https://apps.lse.ac.uk/training-system/userBooking/course/9993200">this link</a> to secure your spot.</b>
If you can no longer attend, please cancel your booking so another student can book.</div>


""",
            unsafe_allow_html=True
            )
