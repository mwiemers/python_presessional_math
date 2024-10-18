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
and related digital skills independently. Our materials are written in a tutorial style and consist of explanations and/or examples followed by one
or multiple tasks. More challenging tasks might require you to combine techniques that you have learned in previous tasks, search online for examples/solutions 
or ask our Python experts or your fellow students for help. Developing expertise and confidence in your ability to get help from online resources is a 
crucial skill for every programmer, which is why we will often encourage you to search online.
            
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

| Date  | Time  | Location  | 
|---|---|---|
| 30-Sep-2024 | 13.00 | LSE LIFE Workspace 2 |
| 04-Oct-2024 | 12.00 | LSE LIFE Workspace 2 |
| 07-Oct-2024 | 14.00 | LSE LIFE Workspace 2 |
| 10-Oct-2024 | 13.30 | LSE LIFE Workspace 2 |
| 14-Oct-2024 | 13.30 | LSE LIFE Workspace 2 |
| 18-Oct-2024 | 11.00 | LSE LIFE Workspace 2 |
| 23-Oct-2024 | 10.30 | LSE LIFE Workspace 2 |
| 25-Oct-2024 | 11.00 | LSE LIFE Workspace 2 |

&nbsp;

<div class="highlight red">
Sign ups for the Python workshops will be available from <b>04 January 2024</b>.
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
