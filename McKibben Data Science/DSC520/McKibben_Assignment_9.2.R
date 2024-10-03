# Makayla McKibben
# DSC520
# Week 9
# Exercise 9.2
# 08.03.2024

# Install and call relevant packages
install.packages("foreign")
library(foreign)
install.packages("tidyverse")
library(tidyverse)
install.packages("mlogit")
library(mlogit)

# Ex. 9.2 problem 1
# Import data from file
surgery <- read.arff("ThoraricSurgery.arff")

# Get a sense of the data's structure
head(surgery)

# Rename columns in dataset
surgery <- surgery %>% 
  rename(Diagnosis = DGN, FVC = PRE4, FEV1 = PRE5, Zubrod = PRE6, Pain_before = PRE7, 
         Haemoptysis_before = PRE8, Dyspnoea_before = PRE9, Cough_before = PRE10, 
         Weakness_before = PRE11, Size_of_tumour = PRE14, T2_Diabetes = PRE17, 
         MI = PRE19, PAD = PRE25, Smoker = PRE30, Asthma = PRE32)

# Check for rename
head(surgery)

# Remove any missing entries/rows
surgery <- surgery[complete.cases(surgery),]

# Create model
surg_model <- glm(Risk1Yr ~ AGE + Diagnosis + FVC + FEV1 + Zubrod + 
                    Pain_before + Haemoptysis_before + Dyspnoea_before  + 
                    Cough_before + Weakness_before + Size_of_tumour + T2_Diabetes + 
                    MI + PAD + Smoker + Asthma, data = surgery, family = binomial)

# Check probabilities
head(surgery, 10)

# Get summary of model
summary(surg_model)

# According to the summary if we look at Pr(>|z|) values we can see that 
# Dyspnoea_before, Size of tumor (especially if large), 
# having type 2 diabetes, and smoking had a significant effect on 1yr survival.

# Predicting the results from the model
model_acc <- predict.glm(surg_model, newdata = surgery)
model_acc

# Create the base for finding percentage of correct predictions
accuracy <- cbind(surgery$Risk1Yr, model_acc)
colnames(accuracy) <- c("1 Year Survival", "Model")
accuracy <- data.frame(accuracy)
head(accuracy)

results_model <- ifelse(accuracy$Model >= 0.5, "Positive", "Negative") 
results_data <- ifelse(surgery$Risk1Yr == 2, "Positive", "Negative")
head(results_data)
results_comb <- cbind(results_data, results_model)
head(results_comb)
colnames(results_comb) <- c("Data", "Model")
results_comb <- data.frame(results_comb)
num_correct <- length(which(results_comb$Data == results_comb$Model))

percent_correct <- (num_correct/length(results_comb$Data))*100
percent_correct

# Ex. 9.2 problem 2
# Import data from file binary classifier data
binary <- read.csv(file = 'binary-classifier-data.csv', header = TRUE, 
                   sep =",", stringsAsFactors = FALSE)

# Check data structure
head(binary)

# Remove rows missing data
binary <- binary[complete.cases(binary),]

# Create model
binary_model <- glm(label ~ x + y, data = binary, family = binomial)

# Check model
summary(binary_model)

# Predict results using model
pred_binary <- predict.glm(binary_model)

# Bind results to single dataframe
binary_acc <- cbind(binary$label, pred_binary)
colnames(binary_acc) <- c("Data", "Model")
binary_acc <- data.frame(binary_acc)

# Check results
head(binary_acc)

# Make necessary transformations
results_model_bin <- ifelse(binary_acc$Model >= 0.5, "Positive", "Negative") 
results_data_bin <- ifelse(binary_acc$Data == 1, "Positive", "Negative")
results_bin <- cbind(results_data_bin, results_model_bin)
colnames(results_bin) <- c("Data", "Model")
results_bin <- data.frame(results_bin)

# Find percent accuracy
num_correct_binary <- length(which(results_bin$Data == results_bin$Model))
percent_correct_binary <- (num_correct_binary/length(results_bin$Data))*100
percent_correct_binary

