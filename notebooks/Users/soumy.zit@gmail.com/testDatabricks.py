# Databricks notebook source
import pandas as pd
#!pip install tensorflow
import tensorflow as tf
# Import mlflow
import mlflow
import mlflow.sklearn
import os
import warnings
import sys

import pandas as pd
import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import lasso_path, enet_path
from sklearn import datasets





# COMMAND ----------

!pip install mlflow