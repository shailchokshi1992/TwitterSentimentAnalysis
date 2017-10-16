import numpy as np  # a conventional alias

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import glob
import os
import string
import nltk
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import scipy.stats as stats
