## Recently California passed proposition 1. The bill is unprecedented in its size and scope: $6.4 Billion dollars for new housing and treatment facilities. The bill accounts for only 10,000 inpatient beds. 

Anecdotal reports, on a account of HIPPA based restrictions, estimate that California’s homelessness crisis and our mental health crisis are one in the same. 

More than 170,000 Californians are unhoused - the majority living in shelters or on the streets. Estimates, taken from relatively small data sets, estimate that between 60% and 80% of the homeless suffer from substance abuse issues, mental illness, or both.

Due to a lack of data, this was a hotly contested issue. The bill passed by only a .3% margin: 28,000 votes. The one thing that is for certain: the bill either is conflating the housing crisis with the homelessness crisis, in a push to create low income housing, or it doesn’t go nearly far enough. The available bes, for in-patient care, would account for only 5% of those currently unhoused.  

Our challenges in assessing the issue is shared by the leading psychiatric data scientists. In a Meta-analysis of all studies that met a thorough criteria of the major health issues, 22 of 33 had fewer than 1000 subjects. The others were conducted by surveys.

Mental illness does not present with a simple nasal swab or blood test. It is an unseen issue that many believe affects the lives of well over 100,000 individuals in California alone. For unseen illness, one must delve into unseen data. This is a task uniquely qualified for machine learning and predictive models; endeavoring to discover what lies beneath the narrowly constricted studies, enormous public health budgets, and a crisis and a crisis that is global in scope. In this study, we sought to uncover a predictive model, based on global data, and discover a grain of truth on this hotly contested debate.

Starting with a macro analysis of global trends, in attempt to see if California was an outlier, if so, to what extent. A global pandemic made this an even greater challenge, besides the challenge of internationally accepted diagnostic criteria.

As such, we chose the largest global dataset available.




Because anxiety and depression go hand in hand with lockdown, disease, and financial strain, one condition stands out from the rest: Schizophrenia. The mysterious affliction is not exacerbated by macroeconomic factors and lockdowns, and serves as a canary in the coal mine, relative to the rest of the data. It is also the most physically damaging, with high rates of homelessness, 3x the likelihood of life threatening comorbidities, and early death.  Even more so than other mental illnesses, there appears to be no cure, absent early intervention, making a predictive model that can identify it, masking as another affliction, all the more prescient.

1 Why Then does it appear schizophrenia, though affecting such a small part of the population is on the rise globally






We tested several predictive models: supervised learning, unsupervised, and there were some clear and not so clear correlations, depending on the model.



2 Scatterplot + violin
Anxiety x bipolar y
The regression line in the scatter plot suggests a positive correlation between anxiety and bipolar metrics.
Eating disorders do not correlate with other mental illnesses, save schizophrenia.

The relationship between bipolar disorder and eating disorders while also taking into consideration the schizophrenia scores of individuals, perhaps to see if there is a pattern or clustering based on the severity or scores of schizophrenia. The positive slope of the regression line indicates that as bipolar scores increase, there is a general increase in eating scores. The data's color-coding allows for a deeper analysis of how these two metrics might interact with schizophrenia scores.

3 Eating y, Bipolar X    Schizophrenia color bar
Eating dosorders, while not correlating previously, lines up with the positive regression of schizo and bipolar.


4 Correlation Matrix
Pandas, Matplotlib and Seaborn for heatmap
Looking at the heatmap, we can interpret some relationships:
Schizophrenia and Depressive: A strong negative correlation (-0.47), suggesting that higher schizophrenia scores are associated with lower depressive scores, or vice versa.
Anxiety and Bipolar: A moderate positive correlation (0.58), indicating that higher anxiety scores might be associated with higher bipolar scores.
Eating and Schizophrenia: A moderate positive correlation (0.50), suggesting that higher eating scores are associated with higher schizophrenia scores.
This heatmap is a powerful tool for quickly identifying how variables relate to each other, which is essential in fields like psychology or medical research where understanding these relationships can guide further analysis or interventions. It should be noted that correlation does not imply causation, and these relationships simply indicate tendencies in the data, not direct cause-and-effect links.

Machine Learning Models

5 Mini Batch 
This learning rate is the inverse of the number of data assigned to a cluster during the process
Depress v schiz  Unrelated
Anxiety v schiz  Differing relationship between anxiety and schiz
Bippolar v schiz The distribution is different from the above two, indicating the relationship between schizophrenia and bipolar disorder may differ from those of depressive and anxiety symptoms.
Anorexia and schizophrenia The spread of the clusters could indicate different patterns of eating behavior associated with varying levels of schizophrenia symptoms. This type of analysis can be particularly useful in psychological or medical research to identify patterns that might not be immediately obvious and could inform treatment approaches or further studies.

6 Agglomerative Clustering - Hierarchical Clustering. Closer together - higher correlation

Choice of clustering method: The chosen clustering method and the number of clusters can significantly impact the patterns observed. Different methods or parameters could result in different groupings, so the approach should be carefully considered and validated.
In summary, the addition of clustering provides a nuanced view of the data, suggesting that individuals with mental health conditions might exhibit distinct patterns in their symptoms and behaviors that could be relevant for diagnostics or treatment. However, any conclusions should be validated with additional analysis and contextual understanding.



7 Not that Great   The Birch (Balanced Iterative Reducing and Clustering using Hierarchies) algorithm is a clustering method designed for very large datasets. It incrementally and dynamically clusters incoming multi-dimensional metric data points to try to produce the best quality clustering with the available resources (i.e., memory and time constraints).
Here's the breakdown of the plots:
Depressive vs. Schizophrenia:
Without Clustering: Scattered points represent individual data records, with schizophrenia scores on the x-axis and depressive symptoms on the y-axis.
With Clustering: After applying the Birch clustering method, the plot on the right indicates different subgroups, highlighting patterns or associations that may exist between depressive symptoms and schizophrenia.
Anxiety vs. Depressive:
Without Clustering: Points are plotted showing the relationship between depressive and anxiety scores without any clustering.
With Clustering: The Birch algorithm has grouped the data into clusters, which might indicate varying degrees of correlation or distinct patterns in how these two conditions are related.


8 (Density-Based Spatial Clustering of Applications with Noise) clustering method to different mental health metrics.
DBSCAN is a density-based clustering algorithm that groups points that are closely packed together and marks as outliers the points that are alone in low-density regions. It’s particularly effective for identifying clusters of arbitrary shapes and sizes in a dataset and is robust to outliers.

9 Kmeans
Elbow Plot Code: The code snippet generates an "elbow plot" where the x-axis represents the number of clusters, and the y-axis represents a metric measuring the within-cluster variation, typically the inertia or sum of squared distances from each point to its assigned cluster center.
Elbow Plot Output: The resulting plot is a curve that typically decreases as the number of clusters increases, and the 'elbow' of the curve represents a point after which the reduction in the within-cluster variation slows down, suggesting a good balance between the number of clusters and the cluster cohesion.
Vertical Dashed Line: A vertical dashed line at x = 3 suggests that the optimal number of clusters for this particular dataset is 3. This is the point where the elbow locator (KneeLocator) identified the elbow of the curve.
KneeLocator Output: Below the plot, the KneeLocator function is called with parameters that specify the range of cluster numbers to consider and the shape of the curve. The output 3 confirms the result indicated by the plot — that the optimal number of clusters is likely 3.
The elbow method is a heuristic used in determining the number of clusters in a data set. The idea is that one should choose a number of clusters so that adding another cluster doesn't give much better modeling of the data. In this context, "much better" is quantified using the within-cluster sum of squares. With K-means, this typically results in a plot where the rate of decrease sharply changes at a certain number of clusters, which is considered to be the appropriate number of clusters.
The interpretation from the plot is that using 3 clusters might be the most appropriate for the underlying dataset when using K-means clustering, as additional clusters do not significantly improve the compactness of the clusters. This is a common technique in exploratory data analysis and unsupervised machine learning for determining the initial number of clusters to use.

Silhouette is useless


10 N3 Clusters k means
Depressive vs. Schizophrenia:
The first row examines the relationship between depressive symptoms and schizophrenia, showing how data points are grouped into clusters.
Anxiety vs. Depressive:
The second row explores the relationship between anxiety and depressive symptoms, with K-Means revealing the distinct groupings within the dataset.
Bipolar vs. Anxiety:
The third row shows the relationship between bipolar disorder scores and anxiety levels, again with clustering highlighting potential patterns.
Eating vs. Schizophrenia:
The fourth row compares eating behaviors with schizophrenia scores, with clustering applied to uncover subgroups.
11 Means Shift

Mean Shift clustering may have identified different cluster distributions compared to the K-Means approach. This is evident from the varied distribution of the clustered data points, which suggests that the Mean Shift algorithm is capturing different structures within the data.
In a direct comparison:
K-Means Clustering might be preferred for its simplicity and efficiency, especially when the expected clusters are hypothesized to be globular.
Mean Shift Clustering is chosen for its adaptability to arbitrary cluster shapes and the model-free nature where no prior knowledge of the cluster count is needed.
When choosing between these two, it's essential to consider the data characteristics and the goals of the analysis. The underlying context of mental health metrics, which likely exhibit complex and non-linear relationships, might benefit from the flexibility of Mean Shift. However, the computational cost and the need for careful bandwidth selection are also important considerations.

12 Spectral.  Unlike kmeans which assumes clusters, spectral makes shapes, and ability to separate
It offers a different approach for more complex relationships.


