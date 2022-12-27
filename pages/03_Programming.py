import streamlit as st
from utils import render_footer, generate_sha256hash, caching_async_mine
import numpy as np
import asyncio
from time import sleep


if "mining" not in st.session_state:
    st.session_state.mining = False
    st.session_state.nonce = 0
    
posts = ["Data", "Database Management System", "Blockchain"]
st.markdown("""
# Technology Page
---

Here you can see some posts about programming and technologies:

"""
)
data, dbms, blockchain= st.tabs(posts)

def create_block(block_id: int):
    with st.container():
        col1, col2 = st.columns([45, 1])
        with col1:
            block_number = st.number_input("Block Number"+(" "*block_id), min_value=1, step=1)
            nonce_place = st.empty()
            nonce = None
            data = st.text_area("Data"+(" "*block_id))
            output_place = st.empty()
            submit = st.button("Mine"+(" "*block_id))
            if submit:
                if not st.session_state.mining:
                    with st.spinner('Mining...'):
                        st.session_state.mining = True
                        nonce = caching_async_mine(block_number, data)
                        st.session_state.mining = False
            nonce = nonce_place.number_input("Nonce"+(" "*block_id), min_value=0, step=1, value=nonce if nonce!=None else st.session_state.nonce)

            hash = generate_sha256hash(str(block_number)+str(nonce)+str(data))
            output_place.markdown(f"Hash\n\n      {hash}")
            if hash[0:4] != "0000":
                st.error("Invalid Hash")
            else:
                st.success("Valid Hash")
        st.markdown("""
<style>
    /* Style containers */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border-width: 2px;
        border-style: solid;
        border-image: linear-gradient(45deg, rgb(255, 75, 75), rgb(255, 253, 128)) 1;
        padding-left: 20px;
        padding-bottom: 20px;
        padding-top: 20px;
    }
</style>
        """,unsafe_allow_html=True,)

def new_block(block_id: int):
    i = block_id-1
    with st.container():
        col1, col2 = st.columns([45, 1])
        with col1:
            block_number = st.number_input("Block Number"+(" "*(block_id+1)), min_value=1, step=1, value=block_id, disabled=True) # i'm incremmenting space to avoid duplicate inputs with same key
            nonce_place = st.empty()
            nonce = st.session_state.blockchain["nonce"][i]
            data = st.text_area("Data"+(" "*(block_id+1)))
            st.markdown(f"Previous Hash\n\n    {st.session_state.blockchain['previous'][i]}")
            output_place = st.empty()
            
            submit = st.button("Mine"+(" "*(block_id+1)))
            if submit:
                if not st.session_state.blockchain["mining"][i]:
                    with st.spinner('Mining...'):
                        st.session_state.blockchain["mining"][i] = True
                        nonce = caching_async_mine(
                            block_number = st.session_state.blockchain["block_id"][i], 
                            data = data,
                            previous = st.session_state.blockchain["previous"][i],
                        )
                        st.session_state.blockchain["mining"][i] = False
            nonce = nonce_place.number_input("Nonce"+(" "*(block_id+1)), min_value=0, step=1, value=nonce if nonce!=None else st.session_state.blockchain["nonce"][i])

            hash = generate_sha256hash(str(block_number)+str(nonce)+str(data)+str(st.session_state.blockchain['previous'][i]))
            st.session_state.blockchain["nonce"][i] = nonce
            st.session_state.blockchain["previous"][i+1] = hash
            output_place.markdown(f"Hash\n\n      {hash}")
            if hash[0:4] != "0000":
                st.error("Invalid Hash")
            else:
                st.success("Valid Hash")
        st.markdown("""
<style>
    /* Style containers */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border-width: 2px;
        border-style: solid;
        border-image: linear-gradient(45deg, rgb(255, 75, 75), rgb(255, 253, 128)) 1;
        padding-left: 20px;
        padding-bottom: 10px;
        padding-top: 20px;
    }
</style>
        """,unsafe_allow_html=True,)

def _add_block_connection(blocks_qtd, i):
    col1, col2, col3 = st.columns([100, 1, 100])
    if i!=blocks_qtd-1:
        with col2:
            st.markdown("""
<div style="
width: 2px; height:10px; 
border-width: 2px;
border-style: solid;
border-image: linear-gradient(45deg, rgb(255, 253, 128), rgb(255, 75, 75)) 1;
padding-top:30px; position:absolute">

</div>
            """, unsafe_allow_html=True)



def create_blockchain():
    blocks_qtd = 4
    if "blockchain" not in st.session_state:
        st.session_state.blockchain = {
        "block_id": np.array(range(1, blocks_qtd+1)),
        "data": np.array(["" for i in range(0, blocks_qtd)]),
        "mining": np.array([False for i in range(0, blocks_qtd)]),
        }
        hashs, previous, nonces = [], ["0"*64,], [caching_async_mine(1, "")]
        for i in range(0, blocks_qtd):
            nonce = caching_async_mine(
                block_number = st.session_state.blockchain["block_id"][i], 
                data = st.session_state.blockchain["data"][i],
                previous = previous[i],
                )
            _hash = generate_sha256hash(
                str(st.session_state.blockchain["block_id"][i])+\
                str(nonce)+\
                str(st.session_state.blockchain["data"][i])+\
                str(previous[i])
                )
            nonces.append(nonce)
            hashs.append(_hash)
            previous.append(_hash)
        st.session_state.blockchain["nonce"] = np.array(nonces)
        st.session_state.blockchain["previous"] = np.array(previous)
        st.session_state.blockchain["hash"] = np.array(hashs)

    for i in range(0, blocks_qtd):
        new_block(st.session_state.blockchain["block_id"][i])
        _add_block_connection(blocks_qtd, i)

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
    with st.expander("Floating Point"):
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
## Data Management

It is the process of collecting, sotring, organizing, and maintaining data so it 
can be used for various use cases like business intelligence. It involves creating 
data structures, including data models, to store data in a way that makes data 
retrieval efficient, as well as ensuring that data remains organized even when it 
is updated or added.

Data management also includes data security measures such as authentication and 
authorization to ensure only authorized users can access data. Additionally,
data management involves data quality control measures to ensure data accuracy 
and integrity. Finally, data management includes data anlytics tools to help 
create data analytics strategies. By using data managemnet processes, organizations 
can better utilize their data, put it into the hands of every employee with 
self-service business intelligence, and gain valuable insights into their operations.
""")
    st.markdown("""
### Types of Data Management
""")
    with st.expander("Data Pipelines"):
        st.markdown("""
These are automated systems that move data from one source to another, typically from 
a data source toa data storage. They can be used to create data flows between applications
and data stores, allowing for data transformation and analysis along the way. Data pipelines
can be used for data cleasing, data integration, real-time event processing, and more.

There are many different types of data pipeline architectures that can be used to move data
from one place to another. Some of the most common include:

- <strong>ETL (Extract, Transform, Load)</strong> - Used to move data from a variety of \
sources into a centralized repository, such as a data warehouse. The data is extracted from \
the sources, transformed into a consistent format and then loaded into the target repository. \
Some examples of data ETL are: 
    - [Matillion](https://www.matillion.com/products/etl-software/)
    - [Rudderstack](https://www.rudderstack.com/)
    - [Supermetrics](https://supermetrics.com/)


- <strong>ELT (Extract, Load, Transform)</strong> - It is similar to ETL, but the data \
transformation step is performed after the data is loaded into the target repository.\
This allows for more flexibillity in how the data is transformed, but can also lead to \
increased complexity. \
Some examples of data ELT are:
    - [Airbyte](https://airbyte.com/)
    - [Fivetran](https://www.fivetran.com/)
    - [Talend](https://www.talend.com/)


Data pipelines are an essential component of data architecture for modern organizations who 
want to make data-driven decisions. They allow you to collect, process, and store data.
Data pipelines come in different shapes and sizes, but all serve the same purpose of getting 
your data from Point A to Point B (and sometimes C). At the end of the day, however, 
organizations still need to explore this data, find insights and take action on them.

""", unsafe_allow_html=True)
    with st.expander("Data Catalogs"):
        st.markdown("""
Data catalogs are collections of metadata, combined with data management and search tools, 
that helps analysts and other data users to find the data that they need, serves as an 
inventory of available data, and provides information to evaluate fitness of data for 
intended uses. In other words Data catalogs is the management of metadata.

Data management, searching, data inventory, and data evaluation, depends on the central 
capability to provide a collection of metadata. Data catalogs  have become a standard 
for metadata management in the age of big data and self-service business intelligence.
The metadata that we need today is more expansive than metadata in the BI era. A data
catalog focuses first on datasets (the invetory of available data) and connects those 
datasets with rich information to inform people who work with data.
""")
    with st.expander("Data Warehouses"):
        st.markdown("""
It is a system that aggregates data from different sources into a single, central,
consistent data store to support data analysis, data mining, artificial intelligence
(AI), and machine learning. A data warehouse system enables an organization to run 
powerful analytics on huge volumes (petabytes and petabytes) of historical data in
ways that a standard database cannot.

Data warehousing systems have been part of business intelligence (BI) solutions for 
over three decades, but they have evolved recently with the emergence of new data 
types and data hosting methods. Traditionally, a data warehouse was hosted on-premises,
often on mainframe computer, and its functionality was focused on extracting data from 
other sources, cleansing and preparing the data, and loading and maintainning the data
in a relational database. More recently, a data warehouse might be hosted on a dedicated
appliance or in the cloud, and most data warehouses have added analytics capabilities 
and data visualization and presentation tools.

The architecture of a data warehouse have three tiers, which consists of a:
- Bottom tier: The bottom tier consists of a data warehouse server, usually a relational 
database system, which collects, cleanses, and transforms data from multiple data sources
through ETL or ELT.
- Middle tier:  consists of an OLAP (Online analytical processing) server which enables 
fast query speeds. Three types of OLAP models can be used in this tier, which are known 
as ROLAP MOLAP and HOLAP. The type of OLAP model used is dependent on the type of database 
system that exists.
- Top tier: Is represented by some kind of front-end user interface or reporting tool, 
which enables end users to conduct ad-hoc data analysis on their business data.

Schemas are ways in which data is organized within a database or data warehouse. There
are two main types of schema structures, the star schema and the snowflake schema, which
will impact the design of your data model.
- Star schema: This schema consist of one fact table which can be joined to a number of 
denormalized dimensions tables. It is considered the simples and most common type of schema,
and its users benefit from its faster speeds while querying.

- Snowflake schema: While not as widely adopted, the snowflake schema is another organization
structure in data warehouses. In this case, the fact table  is connected to a number of 
normalized dimension tables, and these dimension tables have child tables. Users of a snowflake 
schema benefit from its low levels of data redundancy, but it comes at a cost to query 
performance.

There are a few types of data warehouses:
- Cloud data warehouse - data warehouse built to run in the cloud, and it is offered to customers
as a managed service. Cloud-based data warehouses have grown more popular over the last five to 
seven years as more companies use cloud services and seek to reduce their on-premises data center
footprint.
- Data warehouse software (on-premises/license) - a business can purchase a data warehouse license 
and then deploy a data warehouse on their own on-premises infrastructure. Although this is typically
more expensive than a cloud data warehouse service, it might be a better choice for government entities,
financial institutions, or other organizations that want more control over their data or need to comply
with strict security or data privacy standards or regulations.
- Data warehouse appliance - it is a pre-integrated bundle of hardware and software, that business can 
connect to its network and start using as-is. A data warehouse appliance sits somewhere between cloud 
and on-premises implementations in terms of upfront cost, speed of deployment, ease of scalability, and
 management control.

""")
    with st.expander("Data Lakes"):
        st.markdown("""

""")
    with st.expander("Data Governance"):
        st.markdown("""

""")
    with st.expander("Data Security"):
        st.markdown("""

""")
    with st.expander("Data Modeling"):
        st.markdown("""

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

!(alt)[https://drive.google.com/drive/folders/1YjV6PWkAsdSdRPKCFULwt9hlhhJflhhl/]
""")

with blockchain:
    st.markdown("""
# Blockchain Demo
""")
    tabs = ["Hash", "Block", "Blockchain", "Distributed", "Tokens", "Coinbase"]
    _hash, block, _blockchain, distributed, tokens, coinbase = st.tabs(tabs)
    with _hash:
        # input block number
        # input nonce
        # input data
        # output hash
        st.markdown("## SHA 256 Hash")
        _data = str(st.text_area(" Data")).strip()
        _ = st.markdown(f"Hash\n\n      {generate_sha256hash(_data)}") if len(_data)>0 else st.markdown(f"Hash\n\n    Null")

    with block:
        st.markdown("## Block")
        create_block(1)
            
    with _blockchain:
        st.markdown("## Blockchain")
        create_blockchain()

    with distributed:
        st.markdown("")
    with tokens:
        st.markdown("")
    with coinbase:
        st.markdown("")


def set_session_state(key, value):
    st.session_state[key] = value




render_footer()