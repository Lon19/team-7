# Team 7 - JPMorgan's Code for Good
This is the GitHub repo for our Code for Good 2019 entry.
We won the best solution for Autistica, coming 2nd place overall for the event

###### Teammates
Will Davitt, Tom Lancaster, Andrew Morton, Ioana Teju, Andreea Bila, Sebastian Stanici.
[@willdavitt](https://github.com/willdavitt "Will Davitt"), [@TinkerTavern](https://github.com/TinkerTavern "Tom Lancaster"), [@goninty](https://github.com/goninty "Andrew Morton"), [@Seba7159](https://github.com/Seba7159 "Sebastian Stanici")

## Task Introduction - Autistica
### Building brighter futures through autism research

Our project was designed for the charity Autistica. The task at hand was to create suitable data visualisations showing survey response data based on a user's previous data.
The core challenge being that it needs to be easily understandable for an autistic person, while still displaying the important information.

All we were given was some basic CSV files containing response data, and a few example graph visuals to go off.

## Our Approach - Agile
Given the short time, we knew it was important to get a grounding quickly, to break the problem down and come up with a solution.

We settled on 1-2 hourly stand ups with a quick run down on progress and goals, altering aims and the team structure as it was necessary.

### System Structure
We decided to make a robust, expandable solution to the problem, by taking the input data into account and basing our solution on that.
To do this, we needed to decipher the CSV data in a logical format. In order to do this, we designed our system with 4 key components:


#### 1) Backend API
Firstly we needed an API to take in the CSV file and interpret it to return usable data.
This required a large amount of tweaking and understanding of the format of data, as well as a question detection algorithm to figure out the type of question is being asked.
The data is then to be returned in a JSON format for simple use with..

#### 2) Back/Middle End - Django Webserver
This project is data heavy, so we needed a database to handle everything. To make this easier, we used a Django webserver, which has SQLite databases built into it.
This allows us to easily request the CSV data from the API to put into our database, to quickly access for the visualisations.
From this, we were able to quickly create endpoints for...

#### 3) Frontend - React
... Our React system to request and parse data from. Using React allowed us to quickly get a system set up to read and filter the data as needed, for displaying to the end user, using..

#### 4) Frontend - Bootstrap and D3
... Bootstrap to make everything good looking and compatible with many devices, without too much hassle. On top of this, we used the D3.js library to quickly create beautiful visualisations of the data we've returned in several different chart types.
