
# News Recommendation System - MIND Dataset
[PDF Report](./20240920_AML_HW1_Report.pdf)
## Overview

This project is part of **CSCI 6365 Advanced Machine Learning** coursework, where I implemented a news recommendation system using various collaborative filtering approaches. The dataset used is **MIND-small**, provided by Microsoft, which contains user interactions with news articles. The approaches used in this project include:

- **User-Based Collaborative Filtering**
- **Content-Based Collaborative Filtering**
- **Singular Value Decomposition (SVD)**

The goal of this project is to recommend news articles to users based on their browsing history, and evaluate the system using **Recall** and **Precision**.

## Dataset

The **MIND-small** dataset consists of two main files:

1. **behaviors.tsv**: Contains user interactions with news articles, including:
   - `impressionId`, `userId`, `timestamp`, `click_history`, and `impressions` (clicked and not-clicked data).
   
2. **news.tsv**: Contains details about the news articles, including:
   - `itemId`, `category`, `subcategory`, `title`, `abstract`, `url`, `title_entities`, and `abstract_entities`.

## Approaches

### 1. User-Based Collaborative Filtering
In this approach, I recommend news articles by finding users with similar reading habits (history) and recommending news articles that these similar users have read. The process includes:
- Calculating user preference scores based on subcategory counts.
- Finding the top 500 most similar users using **cosine similarity**.
- Aggregating and ranking the news articles from similar users.

### 2. Content-Based Collaborative Filtering
In this approach, I recommend news articles that are similar to what the user has already consumed. It uses:
- The subcategory of the news articles the user has previously read.
- **Softmax normalization** to calculate preference scores.
- Recommending news articles that belong to the user’s most preferred subcategories.

### 3. Singular Value Decomposition (SVD)
The SVD method applies matrix factorization to the user-news interaction matrix:
- The matrix is constructed with users as rows and news articles as columns, where each entry is 1 if the user clicked the article.
- **SVD** is used to reduce the dimensionality and create latent factors.
- Different values of `k` (number of latent factors) were experimented with.

## Experimental Setup

I used the users' browsing history data to calculate which news articles to recommend. Specifically, I used the `click_history` field from the `behaviors.tsv` file, which records the list of news articles that users have clicked on in the past. This historical data was used to compute each user's preference scores and generate personalized recommendations.

To verify the effectiveness of the recommendations, I used the actual clicked data from the `impressions` field, which contains the news articles presented to the user during specific sessions and indicates whether each article was clicked or not. By comparing the recommended news with the ones users actually clicked on, I evaluated the system.

## Evaluation Metrics

The performance of the recommendation system was evaluated using the following metrics:
- **Recall**: Measures the proportion of relevant news articles successfully recommended out of all the news users actually clicked on.
- **Precision**: Measures the proportion of relevant news articles among all the recommended news. A high precision means that the recommendations are mostly relevant to the user's interests.

## Results

The results of each method were evaluated based on different values of **Top N** (the number of news articles recommended):

| **Top N** | **User-Based Recall** | **User-Based Precision** | **Content-Based Recall** | **Content-Based Precision** | **SVD Recall** | **SVD Precision** |
|-----------|-----------------------|--------------------------|--------------------------|-----------------------------|----------------|-------------------|
| 10        | 0.1559                | 0.0640                   | 0.0018                   | 0.0010                      | 0.0007         | 0.0010            |
| 100       | 0.4833                | 0.0240                   | 0.0180                   | 0.0006                      | 0.0012         | 0.0002            |
| 1000      | 0.8422                | 0.0047                   | 0.0832                   | 0.0004                      | 0.0267         | 0.0001            |
| 10000     | 0.8426                | 0.0046                   | 0.3448                   | 0.0002                      | 0.1425         | 0.0001            |

## Conclusion

The **User-Based Collaborative Filtering** approach performed the best in terms of recall and precision, leveraging actual user behavior to recommend news articles. The **Content-Based** method struggled to capture diversity in recommendations, while **SVD** performed poorly likely due to the sparse interaction matrix, as users engage with a limited number of news articles.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ryan0980/Mind_News_Rec_Sys.git
   cd Mind_News_Rec_Sys
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebooks or Python scripts to generate recommendations and evaluate the system.

## References

- [Collaborative Filtering : Data Science Concepts (YouTube)](https://www.youtube.com/watch?v=Fmtorg_dmM0)
- [MIND: Microsoft News Recommendation Dataset (Kaggle)](https://www.kaggle.com/datasets/arashnic/mind-news-dataset)
- [MIND recommender from scratch (Kaggle)](https://www.kaggle.com/code/enemis/mind-recommender-from-scratch/notebook)

