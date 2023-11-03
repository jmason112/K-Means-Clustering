<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<h1>K-Means Clustering for Unsupervised Learning</h1>
<p>This script performs K-Means clustering on a cybersecurity breaches dataset to discover underlying patterns without predefined labels.</p>

<h2>Dependencies</h2>
<p>The script requires the following Python libraries:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>sklearn.cluster (for KMeans)</li>
<li>sklearn.metrics (for silhouette score)</li>
<li>matplotlib.pyplot (for plotting)</li>
</ul>

<h2>Usage</h2>
<p>Ensure that the dataset is available as <code>cybersecuritybreaches.csv</code> in the working directory. Run the script using the command:</p>
<pre><code>python script.py</code></pre>

<h2>Functionality</h2>
<p>The script performs the following operations:</p>
<ol>
<li>Loads the dataset from a CSV file.</li>
<li>Preprocesses data by selecting numerical features and handling missing values.</li>
<li>Performs K-Means clustering with multiple initializations.</li>
<li>Calculates and prints the WCSS and silhouette score for cluster evaluation.</li>
<li>Plots the data points and centroids to visualize the clusters.</li>
<li>May plot the WCSS and silhouette scores for different cluster counts (not fully shown).</li>
</ol>

<h2>Expected Outputs</h2>
<p>The script will output the following:</p>
<ul>
<li>Printed values of WCSS and silhouette score.</li>
<li>A scatter plot visualizing the clusters and their centroids.</li>
<li>Potentially additional plots for WCSS and silhouette scores for different cluster counts (if included).</li>
</ul>
</body>
</html>
