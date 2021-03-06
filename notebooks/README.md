**[1.0_initial_look.ipynb](/notebooks/explore/1.0_initial_look.ipynb)**
---

This notebook serves as an intial exploratory look into the beer review data provided for the CiBO data science exercise. In order to generate the data, please run `make data` from the project root directory.
 
**TOC:**
* [Initial thoughts](/notebooks/explore/1.0_initial_look.ipynb)
* [Missing data](/notebooks/explore/1.0_initial_look.ipynb)

**[2.0_brewery_highest_abv.ipynb](/notebooks/explore/2.0_brewery_highest_abv.ipynb)**
---

The goal of this notebook is to try and answer the question
> Which brewery produces the strongest beers by ABV%?

**NOTE**: analysis [1.0_initial_look](1.0_initial_look.ipynb) identified that various attributes had missing data:
- `beer_abv` not available for all beers
- `brewery_name` not available for each `brewery_id` -> therefore, we should be grouping on `brewery_id`
 
**TOC:**
* [Potential issues](/notebooks/explore/2.0_brewery_highest_abv.ipynb)
* [Remove outliers](/notebooks/explore/2.0_brewery_highest_abv.ipynb)
* [Remove brewery 6513 & those with a low beer count](/notebooks/explore/2.0_brewery_highest_abv.ipynb)

**[3.0_recommend_3_beers.ipynb](/notebooks/explore/3.0_recommend_3_beers.ipynb)**
---

The goal of this notebook is to try and answer the question
> If you had to pick 3 beers to recommend using only this data, which would you pick?
 
**TOC:**
* [Initial thoughts](/notebooks/explore/3.0_recommend_3_beers.ipynb)
* [Checking missing data](/notebooks/explore/3.0_recommend_3_beers.ipynb)
* [Identifying trolls](/notebooks/explore/3.0_recommend_3_beers.ipynb)
* [Identifying best beer](/notebooks/explore/3.0_recommend_3_beers.ipynb)
* [Effect size](/notebooks/explore/3.0_recommend_3_beers.ipynb)

**[4.0_factors_for_beer_quality.ipynb](/notebooks/explore/4.0_factors_for_beer_quality.ipynb)**
---

The goal of this notebook is to try and answer the question
> Which of the factors (aroma, taste, appearance, palette) are most important in determining the overall quality of a beer?

Another way of wording the questions is:
> Which of the beer score factors (aroma, taste, appearance, palette) explain the most variance in the attribute `review_overall`.

**NOTE:** we learned several things in analysis [3.0_recommend_3_beers](3.0_recommend_3_beers.ipynb) that impact this analysis:
- we can remove the reviews that had no associated `review_profilename`
- there were numerous "troll" reviewers which should be removed from the dataset (trolls written to *../../data/interim/trolls.csv*)
 
**TOC:**
* [Univariate linear regression](/notebooks/explore/4.0_factors_for_beer_quality.ipynb)
* [Multivariate linear regression](/notebooks/explore/4.0_factors_for_beer_quality.ipynb)
* [Random Forest regression](/notebooks/explore/4.0_factors_for_beer_quality.ipynb)

**[5.0_beer_style.ipynb](/notebooks/explore/5.0_beer_style.ipynb)**
---

The goal of this notebook is to try and answer the question
> If I enjoy a beer's aroma and appearance, which beer style should I try?

In other words, which beer style in general are correlated with the highest scores in `review_aroma` and `review_appearance`?
 
**TOC:**
* [Descriptive stats](/notebooks/explore/5.0_beer_style.ipynb)
* [Machine learning classification](/notebooks/explore/5.0_beer_style.ipynb)

**[6.0_bonus.ipynb](/notebooks/explore/6.0_bonus.ipynb)**
---

This notebook serves to answer the "bonus" question:

> Generate 10,000 random numbers (i.e. sample) from a Logistic distribution with parameters “location" = 10 and “scale” = 2.

**[1.0_report.ipynb](/notebooks/reports/1.0_report.ipynb)**
---

This notebook serves as the master report document which will present the analysis results for the CiBO data science exercise. The exercise is structured around a beer review data set available [online](https://urldefense.proofpoint.com/v2/url?u=https-3A__s3.amazonaws.com_demo-2Ddatasets_beer-5Freviews.tar.gz&d=DwMFaQ&c=imBPVzF25OnBgGmVOlcsiEgHoG1i6YHLR0Sj_gZ4adc&r=8bgQeuykrF3aSX4ERnAE37e9TNni25ddf39sbnkKHrQ&m=hkI6yrD7SBn4Z9WO9Zt31KmSuYIswplFpvMihrHqFd4&s=PStqu-SKl1ZEMNBu4MLVtzHvrTddC9h1mM3NqDgmYmI&e=) for which the following must be explored:
> 1. Which brewery produces the strongest beers by ABV%?
> 2. If you had to pick 3 beers to recommend using only this data, which would you pick?
> 3. Which of the factors (aroma, taste, appearance, palette) are most important in determining the overall quality of a beer?
> 4. If I enjoy a beer's aroma and appearance, which beer style should I try?
 
**TOC:**
* [Initial data exploration](/notebooks/reports/1.0_report.ipynb)
* [Q1: Which brewery produces the strongest beers by ABV%?](/notebooks/reports/1.0_report.ipynb)
  * [Introduction](/notebooks/reports/1.0_report.ipynb)
  * [Dealing with noisy ABV%](/notebooks/reports/1.0_report.ipynb)
  * [Choosing a brewery](/notebooks/reports/1.0_report.ipynb)
  * [Summary](/notebooks/reports/1.0_report.ipynb)
* [Q2: If you had to pick 3 beers to recommend using only this data, which would you pick?](/notebooks/reports/1.0_report.ipynb)
  * [Introduction](/notebooks/reports/1.0_report.ipynb)
  * [Removing suspicious reviews (trolls)](/notebooks/reports/1.0_report.ipynb)
  * [Determining best beer](/notebooks/reports/1.0_report.ipynb)
  * [Summary](/notebooks/reports/1.0_report.ipynb)
* [Q3: Which of the factors (aroma, taste, appearance, palette) are most important in determining the overall quality of a beer?](/notebooks/reports/1.0_report.ipynb)
  * [Introduction](/notebooks/reports/1.0_report.ipynb)
  * [Analysis](/notebooks/reports/1.0_report.ipynb)
  * [Summary](/notebooks/reports/1.0_report.ipynb)
* [Q4: If I enjoy a beer's aroma and appearance, which beer style should I try?](/notebooks/reports/1.0_report.ipynb)
  * [Introduction](/notebooks/reports/1.0_report.ipynb)
  * [Descriptive stats](/notebooks/reports/1.0_report.ipynb)
  * [Machine learning classification](/notebooks/reports/1.0_report.ipynb)
  * [Summary](/notebooks/reports/1.0_report.ipynb)
* [Q5: Generate 10,000 random numbers (i.e. sample) from a Logistic distribution with parameters “location" = 10 and “scale” = 2.](/notebooks/reports/1.0_report.ipynb)

