**[1.0_initial_look.ipynb](/notebooks/explore/1.0_initial_look.ipynb)**
---

General questions to think about:
- is each beer equally represented in the reviews, or do some beers get more/less reviews?
- do we have all the data, or are there datum missing? If so, we may have to impute
- are there any gross outliers which we should be careful of?
- if every beer was equally reviewed, how many reviews would we expect each beer to have?
- is each brewery equally represented in reviews?
- does each brewery have the same count of number of beers reviewed?
- do any of the reviewers have an "outlier" taste profile or do they rank beers quite differently to others?
- are the beer_style equally represented?

**[2.0_brewery_highest_abv.ipynb](/notebooks/explore/2.0_brewery_highest_abv.ipynb)**
---



**[3.0_recommend_3_beers.ipynb](/notebooks/explore/3.0_recommend_3_beers.ipynb)**
---

This question is quite open ended, best beer might be interpreted in the following ways:
- best overall beers in entire dataset
- best beers per `beer_type`
- best can be rated by any or a combination of the beer attributes: `review_overall`, `review_aroma`, `review_appearance`, `review_tast`, `review_palate`, `beer_abv`

**NOTE**: analysis [1.0_initial_look](1.0_initial_look.ipynb) identified various attributes with missing data that may impact this analysis:
- `beer_abv` not available for all beers
- `review_profilename` not available for each review -> it's uncertain what happend with this data - consider excluding?

**[4.0_factors_for_beer_quality.ipynb](/notebooks/explore/4.0_factors_for_beer_quality.ipynb)**
---

The goal of this notebook is to try and answer the question
> Which of the factors (aroma, taste, appearance, palette) are most important in determining the overall quality of a beer?

Another way of wording the questions is:
> Which of the beer score factors (aroma, taste, appearance, palette) explain the most variance in the attribute `review_overall`.

**NOTE:** we learned several things in analysis [3.0_recommend_3_beers](3.0_recommend_3_beers.ipynb) that impact this analysis:
- we can remove the reviews that had no associated `review_profilename`
- there were numerous "troll" reviewers which should be removed from the dataset (trolls written to *../../data/interim/trolls.csv*)

**[X.0_bonus.ipynb](/notebooks/explore/X.0_bonus.ipynb)**
---

This notebook serves ...

> Generate 10,000 random numbers (i.e. sample) from a Logistic distribution with parameters “location" = 10 and “scale” = 2.

**[1.0_report.ipynb](/notebooks/reports/1.0_report.ipynb)**
---



