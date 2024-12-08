# SUMMONER'S PIPELINE
"Summoner's Pipeline" is a portfolio Data Engineering project designed to demonstrate and practice the use of modern tools for scalable data pipelines. It extracts information from the League of Legends API, stores raw data in Amazon S3, transforms it using Apache Spark, and loads it into Amazon Redshift. The pipeline processes data on matches, champions, and summoners, enabling advanced analysis and insights into the game.

---

## Project Architecture:
1. **Data Extraction**:
    - Data is fetched from the League of Legends API.
2. **Load to AWS S3**:
    - Raw data is stored in a S3 bucket for centralized backup.
3. **Transforming with Apache Spark**:
    - Data cleaning, transformation and modeling into a fact and dimension tables(dimensional modeling).
    - Validation and deduplication of data.
4. **Load to AWS Redshift**:
    - Data is stored in Redshift tables optimized for analytical queries.

---

## Data Modeling Architecture:
- **Dimension Tables**:
    - `dim_summoner`: Summoner information.
    - `dim_champions`: Champions details.
    - `dim_items`: Items information.
- **Fact Table**:
    - `fact_matches`: Contains metrics and statistics from matches.

---

## Conclusion:
This project highlights my journey in learning and applying modern data engineering tools and techniques. By working with AWS S3, Apache Spark, and Redshift, I developed a scalable and efficient data pipeline, gaining hands-on experience in extracting, transforming, and modeling data for analytical purposes. This pipeline demonstrates my ability to design and implement solutions for real-world data challenges.

---

## Contributions:
If you have suggestions or would like to contribute to this project, please feel free to open an issue or submit a pull request. Feedback is always welcome, as this project is part of my continuous learning journey.

---

## Contact:
- **Name:** Sebastián Esnaola
- **LinkedIn:** [www.linkedin.com/in/sebastian-esnaola]
- **Email:** isp2014asje@gmail.com