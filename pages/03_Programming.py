import streamlit as st
from utils import render_footer


posts = ["Data", "Database Management System"]
st.markdown("""
# Technology Page
---

Here you can see some posts about programming and technologies:

"""
)
data, dbms = st.tabs(posts)

with data:
    st.markdown("""
# Data Overview

Data is any sequence of one or more symbols; *datum* is a single symbol of data. 
Data requires interpretation to become information. Digital data is data that is
represented using the binary number system, instead of analog representation. 
In modern computer system, all data is digital. Data can be anything that acts as
valuable input and leads to a result (output information or another data), the 
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
Metadata helps translate data to information. Metadata is data about the data. 
Metadata may be implied specified or given.

Data relating to physical events or processes will have a temporal component. 
This temporal component may be implied. This is the case when a device such as a 
temperature logger receives data from a temperature sensor. When the temperature 
is received it is assumed that the data has a temporal reference of now. So the 
device record the date, time, and temperature together. When the data logger 
communicates temperatures, it must also report the date and time as metadata for 
each temperature reading.

Fundamentally, computes follow a sequence of instructions they are given in the 
form of data. A set of instructions to perform a given task (or tasks) is called 
a program. A program is data in form of coded instructions to control the 
operation of a computer or other machine. In the nominal case, the program, as 
executed by the computer, will consist of machine code. The elements of storage 
manipulated by the program, but not actually executed by the CPU, are also data. 
At its most essential, a single datum is a value stored at specific location. 
Therefore, it is possible for computer programs to operate on other computer 
programs by manipulating their programatic data.

To store data bytes in a file, they have to be serialized in a file format. 
Typically programs are stored in special file types, different from those used for 
other data. Executable files contain programs; all other files are also data files. 
However executable files may also contain data used by the program which is built 
into the program. In particular, some executable files have a data segment, which 
nominally contains constants and initial values for variables, both of which can be 
considered data. The line between program and data can become blurry. An interpreter, 
for example is a program. The input data to an interprewter is itself a program, just 
not one expressed in native machine language. In many cases the, interpreted program 
will be a human-readable text file, which is manipulated with a text editor program. 
Metaprogramming similarly involves programs manipulating other programs as data. 
Programs like compilers, linkers, debuggers, program updaters, vírus scanners and such 
use other programs as their data.

For example, a user might first instruct the operating system to load a word processor 
program from one file, and then use the running program to open and edit a document stored 
in another file. In this example. the document would be considerd data. If the word 
processor also features a  
""")
    st.markdown("""
## Data Types
A data type is an attribute associated witha  piece of data that tells a computer system
 how to interpret its value. Understanding data types ensures that data is collected in 
 the preferred format and the value of each property is as expected.
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

A dataset can be interpreted as a collection of data that is treated as a single
unit by a computer. It means that a dataset contains a lot of separete pieces of
data related to one particular subject. All the separate pieces of data are used
to train an algorithm with the ultimate goal of finding predictable patterns 
inside the whole dataset.

It is important to understand that a dataset is different from a database. A 
collection of separate pieces of data is a dataset while a collection of datasets 
is called database. While a dataset is limited to containing information related 
to just one topic, a database covers a wide range of topics.

Examples:
""")
    with st.expander("String"):
        st.markdown("""
It is a sequence of characters and the most commonly used data type to store text. Additionally, a string can also include digits and symbols, however, it is always treatd as text.

Examples:
- 42;
- +1-999-666-3333;
- some cool text;
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
    
    st.markdown("""
## Data Structure

A data structure is a storage that is used to store and organize data. It is a way 
of arranging data on a computer so that it can be accessed and updated efficiently.
It is not only used for organizing the data. It is also used for processing, 
retrieving, and storing data. There are different basic and advanced types of data 
structures that are used in almost every program or software system that has been
developed. So we must have good knowledge about data structures.
![DATA Structure](https://media.geeksforgeeks.org/wp-content/uploads/20220520182504/ClassificationofDataStructure-660x347.jpg)

Data Structure has two classifications: linear or non-linear:
""")
    with st.expander("Linear"):
        st.markdown("""
Data structure in which data elements are arranged sequentially or linearly, 
where each element is attached to its previous and next adjacent elements.
We can also classify the linear data structure in two other class:
- Static - has a fixed memory size. It is easier to access the 
elements in a static data structure. Example: Arrays.
- Dynamic - the size is not fixed. It can be randomly updated during the runtime 
which may be considered efficient concerning the memory (space) complexity of the 
code. Example: Queue, Stack, Linked list
""")
    with st.expander("Non-linear"):
        st.markdown("""
Are data structures where the elements are not placed sequentially or linearly. We
can't traverse all the elements in a single run only. Examples: Trees, Graphs.
""")
    st.markdown("""
## Big Data
The definition of big data is data that contains greater variety, arriving in 
increasing volumes and with more velocity. Big data is a term related to extracting 
meaningful data by analyzing the huge amount of complex variously formatted data 
generated at high speed, that cannot be handled, or processed by the traditional 
system. Day by day amount of data increasing exponentially because of today's 
various data production sources like smart eletronic devices. This is also known as 
the five Vs.

Big data is larger, more complex data sets, especially from new data sources. These 
data sets are so voluminous that traditional data processing software just can't manage
them. But these massive volumes of data can be used to address business problems you
wouldn't have been able to tackle before.

The five Vs of big data are:
- Volume;
- Velocity;
- Variety;
- Value;
- Veracity;
""")
    with st.expander("History of big data"):
        st.markdown("""
Although the concept of big data itself is relatively new, the origins of large data 
sets go back to the '60s and '70s when the world of data was just getting started with
the first data centers and the development of the relational database. Around 2005, 
people began to realize just how much data users generated through Facebook, Youtube, 
and other online services. Hadoop (an open-source framework created specifically to 
store and analyze big data sets) was developed that same year. NoSQL also began to 
gain popularity during this time.

The development of open-source frameworks, such as Hadoop or Spark, was essential for 
the growth of big data because they make big data easier to work with and cheaper to store.
In the years since then, the volume of big data has skyrocketed. Users are still generating
huge amounts of data, but it's not just humans who are doing it. With the advent of the IoT,
more objects and devices are connected to the internet gathering data on customer usage 
patterns and product performance. The emergence of machine learning has produced still more 
data.

While big data has come far, its usefulness is only just beginning. Cloud computing has 
expanded big data possibilities even further. The cloud offers truly elastic scalability, 
where developers can simply spin up ad hoc clusters to test a subset of data. And graph 
databases are becoming increasingly important as well with their ability to display massive
amounts of data in a way to makes analytics fast and comprehensive.

""")
    st.markdown("""
## Data Labelling
The process of identifying raw data such as images, texts, videos, etc and adding 
meaningful insights or informative labels so that the machine learning model can 
learn from it is called data labelling.

Data labelling is also important for supervised learning, an approach utilised by 
most practical machine learning models right now. A properly labelled dataset is 
used as the standard to train a machine learning model. The process begins with 
humans making judgements about a fiven piece of unlabelled data.

## Data Mining
It is the process of extracting insight meaning, hidden patterns from collected 
data that is useful to take a business decision for the purpose of decrasing 
expenditure and increasing revenue.
""")

    

with dbms:
    st.markdown("""
# Database Management System
DBMS are software systems used to store, retrieve, and run queries on data. A 
DBMS serves as an interface between an end-user and a database, allowing users 
to create, read, update, and delete data in the database. The DBMS accepts the
request for data from an application and instructs the operating system to
provide the specific data. In large systems, a DBMS helps users and other 
third-party software store and retrieve data.

DBMS manage the data, the database engine, and the database schema, allowing 
for data to be manipulated or extracted by users and other programs. This helps 
provide data security, data integrity, concurrency, and uniform data 
administration procedures.

DBMS optimizes the organization of data by following a database schema design 
technique called normalization, which splits a large table into smaller tables 
when any of its attributes have redundancy in values. DBMS offer many benefits 
over traditional file systems, including flexibility and a more complex backup 
system.

DBMS allows users to create their own databases as per their requiremnets. The
term "DBMS" includes the user of the database and other application programs.
It provides an interface between the data and the software application.

Database management systems can be classified based on a variety of criteria 
such as the data model, the database distribution, or user numbers. The most 
widely used types of DBMS software are:
""")
    with st.expander("Distributed - DDBMS"):
        st.markdown("""
A distributed DBMS is a set of logically interrelated databases distributed 
over a network that is managed by a centralized database application. This type 
of DBMS synchronizes data periodically and ensures that any change to data is 
universally updated in the database.
""")
    with st.expander("Hierarchical - HDBMS"):
        st.markdown("""
Hierarchical databases organize model data in a tree-like structure. Data 
storage is either a top-down or bottom-up format and is represented using a 
parent-child relationship. In HDBMS parents may have many children, but 
children have only one parent.
""")
    with st.expander("Network - NDBMS"):
        st.markdown("""
The network database model allows each child to have multiple parents. It 
helps you to address the need to model more complex relationships like the
orders/parts many-to-many relationship. In this model, entities are organized
in a graph which can be accessed through several paths.
""")
    with st.expander("Object-oriented - OODBMS"):
        st.markdown("""
Object-oriented models store data in objects instead of rows and columns. It is 
based on object-oriented programming (OOP) that allows objects to have members 
such as fields, properties, and methods. The structure is called classes which
display data within it. 
""")
    with st.expander("Relational - RDBMS"):
        st.markdown("""
Relational DBMS (RDBMS) are the most popular data model because of its user-friendly 
interface. It is based on normalizing data in the rows and columns of the tables. 
This is a viable option when you need a data storage system that is scalable, 
flexible, and able to manage lots of information.
""")
    st.markdown("""
DBMS provides security and removes redundancy, has many advantages over traditional 
Flat File management system. It has self-describing nature, insulation between 
programs and data abstraction and it also supports multiple views of the data, etc.

Although DBMS system is useful, it is still not suited for the specific task. It is 
not recommended when you do not have the budget or the expertise to operate a DBMS. 
In such cases, Excel/CSV/Flat Files could do just fine.
""")
render_footer()