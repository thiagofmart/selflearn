import streamlit as st
from utils import render_footer


posts = ["Data", "SQL & NoSQL"]
st.markdown("""
# Technology Page
---

Here you can see some posts about programming and technologies:

"""
)
data, sql_nosql = st.tabs(posts)

with data:
    st.markdown("""
# Data Overview
This post is an overview about data
""")
    st.markdown("""
## Data definition
Data is any sequence of one or more symbols; *datum* is a single symbol of data. 
Data requires interpretation to become information. Digital data is data that is
represented using the binary number system, instead of analog representation. 
In modern computer system, all data is digital. Data can be anything that acts as
valuable input and leads to a result (output inforamtion or another data), the 
data information translated into a form that can be easily processed by the
machine. In general, the data is essentially information converted into binary
digital form. In its most basic form, the information available is referred as
raw data.

Data exist in three states: data at rest, data in transit and data in use. Data 
within a computer, in most cases, moves as parallel data. Data moving to or from 
a computer, in most cases, moves as serial data. Data sourced from an analog 
device, such as a temperature sensor, may be converted to digital using an 
analog-to-digital-converter. Data representing quantities, characters, or 
symbols on which operations are performed by a computer are stored and recorded 
on magnetic, optical, eletronic or mechanical recording media, and transmitted in 
the form of digital electrical or optical signals. Data pass in and out of 
computers via peripheral devices.

Physical computer memory elements consist of an address and a byte/word of data 
storage. Digital data are often stored in relational databases, like tables or 
SQL databases, and can generally be represented as abstract key/value pairs. 
Data can be organized in many different types of data structures, including 
arrays, graphs, and objcets. Data structures can store data of many different 
types, including numbers, string, booleans and even other nested data structures.
""")

    st.markdown("""
## Metadata 
Metadata helps translate data to information. Metadata is data about the data. Metadata may be implied specified or given.

Data relating to physical events or processes will have a temporal component. This temporal component may be implied. This is the case when a device such as a temperature logger receives data from a temperature sensor. When the temperature is received it is assumed that the data has a temporal reference of now. So the device record the date, time, and temperature together. When the data logger communicates temperatures, it must also report the date and time as metadata for each temperature reading.

Fundamentally, computes follow a sequence of instructions they are given in the form of data. A set of instructions to perform a given task (or tasks) is called a program. A program is data in form of coded instructions to control the operation of a computer or other machine. In the nominal case, the program, as executed by the computer, will consist of machine code. The elements of storage manipulated by the program, but not actually executed by the CPU, are also data. At its most essential, a single datum is a value stored at specific location. Therefore, it is possible for computer programs to operate on other computer programs by manipulating their programatic data.

To store data bytes in a file, they have to be serialized in a file format. Typically programs are stored in special file types, different from those used for other data. Executable files contain programs; all other files are also data files. However executable files may also contain data used by the program which is built into the program. In particular, some executable files have a data segment, which nominally contains constants and initial values for variables, both of which can be considered data.
The line between program and data can become blurry. An interpreter, for example is a program. The input data to an interprewter is itself a program, just not one expressed in native machine language. In many cases the, interpreted program will be a human-readable text file, which is manipulated with a text editor program. Metaprogramming similarly involves programs manipulating other programs as data. Programs like compilers, linkers, debuggers, program updaters, vírus scanners and such use other programs as their data.

For example, a user might first instruct the operating system to load a word processor program from one file, and then use the running program to open and edit a document stored in another file. In this example. the document would be considerd data. If the word processor also features a  
""")
    st.markdown("""
## Data Types
A data type is an attribute associated witha  piece of data that tells a computer system how to interpret its value. Understanding data types ensures that data is collected in the preferred format and the value of each property is as expected.
The common data types are:
""")
    with st.expander("Integer"):
        st.markdown("""
It is the most common numeric data type userd to store numbers without a fractional component. 

Examples:
- -42;
- 42;
""")
    with st.expander("Floaing Point"):
        st.markdown("""
It is also a numeric data type used to store numbers that may have a fractional component like a monetary value do;

Examples:
- -42.000;
- 42.42;
""")
    with st.expander("Character"):
        st.markdown("""
It is used to store a single letter, digit, punctuation, mark, symbol, or blank space.

Examples:
- A;
- 0;
- $;
- @;

**_NOTE:_** space like this " " is also considered as a character;
""")
    with st.expander("String"):
        st.markdown("""
It is a sequence of characters and the most commonly used data type to store text. Additionally, a string can also include digits and symbols, however, it is always treatd as text.

Examples:
- 42;
- +1-999-666-3333;
- some cool text;
""")
    with st.expander("Boolean"):
        st.markdown("""
It represents the values true and false. When working with the boolean data type, it is helpful to keep in mind that sometimes a boolean value is also represented as 0 (for false) and 1 (for true);

Examples of representations:
- true;
- false;
- 1 (for true);
- 0 (for false);
- \+ (for true);
- \- (for false);
""")
    with st.expander("Enumerated"):
        st.markdown("""
It contatins a small set of predefined unique values (also know as elements or enumerators) that can be compared and assigned to a variable of enumerated data type.

The values of an enumerated type can be text-based or numerical. In fact the boolean data type is a pre-defined enumeration of values true and false.

For example, if rock and jazz are the enumerators, an enumerated type variable genre can be assigned either of the two values, but not both.

Assuming that you are asked to fill in your preferences on a music app and are asked to choose either one of the two genres via a dropdown menu, the variable genre will store either rock or jazz.

With enumerated type, values can be stored and retrieved as numeric indices (0, 1, 2) or strings;

Examples:
- genres = [rock, jazz]
- genres_indices = [0, 1]

""")
    with st.expander("Array"):
        st.markdown("""
Alson known as a list, an array is a data type that stores a number of elements in a specific order, typically all of the same type.

Since an array stores multiple elemets or values, the structure of data stored by an array is referred to as an array data structure.

Each element of an array can be retrieved using an integer index (0, 1, 2, ...), and the total number of elements in an array represents the length of an array. If you are asked to choose one or more of the three genres and you happen to like all three (cheers to that), the variable genre will store all three elements (rock, jazz, blues).

Examples:
- genres = [rock, jazz, blues]
- genres_indices = [0, 1, 2]
""")
    with st.expander("Date"):
        st.markdown("""
Needs no explanation; typically stores date in the YYYY-MM-DD format (ISO 8601 syntax)
""")
    with st.expander("Time"):
        st.markdown("""
Stores a time in the hh:mm:ss format. Besides the time of the day, it can also be used to store the time elapsed or the time interval between two events (timedelta) which could be more than 24 hours.

Examples:
- time_elapsed = 72:00:59 (+72 hours);
- some_time = 03:00:42;
""")
    with st.expander("Datetime"):
        st.markdown("""
Stores a value containing both date and time together in the YYYY-MM-DD hh-mm-ss format.

Examples:
- birthdate = 2002-03-24 23:42:02;
""")
    with st.expander("Timestamp"):
        st.markdown("""
Typically represented in Unix time, a timestamp represents the number of seconds that have elapsed since midnight (00:00:00 UTC), 1st January 1970.

It is tipically used by computer systems to log the precise date and time of an event, down to the number of seconds, in a format that is unaffected by time zones. Therefore unlike datetime, timestamp remains the same irrespective of your geographical location.

Examples;
- 1985‑09‑25 17:45:30.005;

""")
    st.markdown("""
## Data Sets

A dataset can be interpreted as a collection of data that is treated as a single unit by a computer. It means that a dataset contains a lot of separete pieces of data related to one particular subject. All the separate pieces of data are used to train an algorithm with the ultimate goal of finding predictable patterns inside the whole dataset.

It is important to understand that a dataset is different from a database. A collection of separate pieces of data is a dataset while a collection of datasets is called database. While a dataset is limited to containing information related to just one topic, a database covers a wide range of topics.
""")
    st.markdown("""
## Big Data

In the past decade, the advent of smartphones and smart consumer devices has led to a data explosion. We now have more devices generating and contributing data than ever before. As a result, the data types have also evolved to an extent where it is no longer restricted to just text, images, audio, and video information.

We now have data types that include log and web activity records. When the availabe data goes in the range of petabyte or larger, it is labelled as big data. In the world of artificial intelligence, the data availabre to an expert is generally classified into three types:
- Visual;
- Textual;
- Numerical.

## Data Labelling
The process of identifying raw data such as images, texts, videos, etc and adding meaningful insights or informative labels so that the machine learning model can learn from it is called data labelling.

Data labelling is also important for supervised learning, an approach utilised by most practical machine learning models right now. A properly labelled dataset is used as the standard to train a machine learning model. The process begins with humans making judgements about a fiven piece of unlabelled data.
""")
    

with sql_nosql:
    st.markdown("""
    I'm currently working on...
    """)

render_footer()