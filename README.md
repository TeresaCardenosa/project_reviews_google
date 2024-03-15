# Viewing Google Maps reviews

Since Google Maps landed in Spain in April 2006, it has become a fundamental tool for guiding us around the world: 25 million people use it every day. 
And it is not only a GPS tool, but also a purchasing decision tool, as its reviews have overtaken other players such as Booking or TripAdvisor and account for 85% of reviews on the Internet. 

For any brand, the management of reviews posted on Google can be decisive, not only for its growth metrics, but also for its own brand positioning. Platforms such as Partoo or the Google My Business interface itself allow us to respond to user reviews, but how do we know the total number of reviews we receive? How can we check whether the trend is positive or negative? Where can we see the historical results of our work? 

This repository, framed in the final project of the Data Analytics bootcamp at Ironhack, seeks to answer this need through a dashboard for visualising Google reviews. 

To develop it I use REAL reviews of REAL tabs. This is a review management project, started in 2018, launched by the communication department of a company. Due to privacy policy, the names of the establishment tokens used in the project have been encrypted. 


## Tech Stack

<img src="{https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue}" />
![image]({})

![image]({https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white})

![image]({https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white})


## Roadmap

Roadmap for the transformation of internal reviews to which we have access: 

1. When using the Partoo tool to manage customer reviews, we will have the reviews of all the cards managed on an annual basis in different .xlsx files. In total, there will be 6 files. 

2. We develop a pipeline where, through the terminal, we introduce only the file downloaded from Partoo and we indicate where we want to save the same file. In this pipeline we will clean our data and apply different transformations to it: 
    - Unify 'Date of the review' depending on whether the review has received a recent modification or not. 
    - Eliminate different columns that do not add value to the visualisation and for privacy reasons, such as the user id. 
    - Add two new columns for customer requirements: Typography and Territory. 

3. As the result is a total of 6 files (one for each year), we will contain all of them in order to have all the years in a single file. 

Transformation path of external reviews to which we do not have access: 

The client also requests to be able to "compare" the number of reviews registered on their establishments with other external files. In order to develop it: 

1. Connection to Google Places through the API to extract the business ID of the listing. We rejected the option of using the Google API because, as they are not our establishments, it only offers us the option of extracting the 5 most relevant reviews. 

2. We discarded the web scrapping option when we found the option of using SerpApi. This is an API where you can access the reviews 10 by 10 with a maximum of 100 free calls available. We used this option to extract the reviews of the last 12 months from 7 external tabs. 

3. We develop a pipeline where we clean our data and apply different transformations to it: 
    - Unify 'Date of the review' as the month in which it was written. 
    - Eliminate different columns that do not add value to the visualisation and privacy, such as the user id. 
    - Give new columns such as the name of the record, encrypted name of the record, address and postcode. 

At this point what we do is to concatenate both files generated, both own reviews and external reviews, in a single file. On this file we will apply the data visualisation. 




## Visualization

You can access the visualisation in Tableau public here: 
https://tabsoft.co/4ab24N5 

## Author

- [@TereCarde](https://www.github.com/TeresaCardenosa)