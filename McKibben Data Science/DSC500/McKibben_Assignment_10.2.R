# Makayla McKibben
# DSC520
# Week 10
# Assignment 10.2

install.packages("ggplot2")
library(ggplot2)
install.packages("factoextra")
library(factoextra)
install.packages("tidyverse")
library(tidyverse)
library(gridExtra)
install.packages("caTools")
library(caTools)
library(class)
install.packages("caret")
library(caret)

# Set working directory
setwd("C:/Users/makay/OneDrive/Documents/DSC520")

# Import data from file binary classifier data
binary <- read.csv(file = 'binary-classifier-data.csv', header = TRUE, 
                   sep =",", stringsAsFactors = FALSE)
trinary <- read.csv(file = 'trinary-classifier-data.csv', header = TRUE, 
                    sep =",", stringsAsFactors = FALSE)
clust <- read.csv(file = 'clustering-data.csv', header = TRUE, 
                  sep =",", stringsAsFactors = FALSE)

# Check data structures
head(binary)
head(trinary)

# Code from week 9 
# Remove rows missing data
binary <- binary[complete.cases(binary),]
trinary <- trinary[complete.cases(trinary),]

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
# Percent accuracy = 51.2% from week 9

# Week 10 
# Base plots of datasets
bin_plot <-ggplot(binary, aes(x, y))
bin_plot + geom_point(color = "purple", shape = 8, size = 1.8) + 
  theme(panel.grid = element_line(color = "lightgrey", linewidth = 0.8, linetype = 1),
        panel.background = element_rect(color = "white", fill = "darkgrey")) +
  labs(title = "Binary Plot", x ="X", 
       y = "Y") + xlim(0, 100) + ylim(0, 100)

trin_plot <-ggplot(trinary, aes(x, y))
trin_plot + geom_point(color = "blue", shape = 8, size = 1.8) + 
  theme(panel.grid = element_line(color = "lightgrey", linewidth = 0.8, linetype = 1),
        panel.background = element_rect(color = "white", fill = "darkgrey")) +
  labs(title = "Trinary Plot", x ="X", 
       y = "Y") + xlim(0, 100) + ylim(0, 100)
# I do not believe a linear fit works for either of these models

# Binary knn model
# Create objects to submit to the knn function
bin_train_index <- createDataPartition(binary$label, times = 1, p = 0.8, list = FALSE)
bin_train <- binary[bin_train_index, ]
bin_test <- binary[-bin_train_index, ]
bin_label <- binary$label[1:length(bin_train_index)]

# Transform to dataframes
bin_train <- as.data.frame(bin_train)
bin_test <- as.data.frame(bin_test)

# Scale data length
bin_train_scale <- scale(bin_train[1:length(bin_train_index), , ])
bin_test_scale <- scale(bin_test[1:length(bin_train_index), , ])

# Create list with all k values
k <- list(3, 5, 10, 15, 20, 25)

# Make binary knn models
bin_pred_3 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[1])
bin_pred_5 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[2])
bin_pred_10 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[3])
bin_pred_15 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[4])
bin_pred_20 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[5])
bin_pred_25 <- knn.cv(train = bin_train_scale, cl = bin_label, k = k[6])

# Create tables of binary knn data
bm3 <- table(bin_label, bin_pred_3)
bm5 <- table(bin_label, bin_pred_5)
bm10 <- table(bin_label, bin_pred_10)
bm15 <- table(bin_label, bin_pred_15)
bm20 <- table(bin_label, bin_pred_20)
bm25 <- table(bin_label, bin_pred_25)

# Find accuracy of binary knn models
acc3b <- sum(diag(bm3))/length(bin_label)
sprintf("Accuracy for k = 3: %.2f%%", acc3b*100)
acc5b <- sum(diag(bm5))/length(bin_label)
sprintf("Accuracy for k = 5: %.2f%%", acc5b*100)
acc10b <- sum(diag(bm10))/length(binary$label)
sprintf("Accuracy for k = 10: %.2f%%", acc10b*100)
acc15b <- sum(diag(bm15))/length(binary$label)
sprintf("Accuracy for k = 15: %.2f%%", acc15b*100)
acc20b <- sum(diag(bm20))/length(binary$label)
sprintf("Accuracy for k = 20: %.2f%%", acc20b*100)
acc25b <- sum(diag(bm25))/length(binary$label)
sprintf("Accuracy for k = 25: %.2f%%", acc25b*100)

# The model from last weeks regression was 51.2% compared to mid to upper 90s for the small values of k for kmeans clusters. Kmeans grouping can find the optimal number of chunks to break thse datasets into while the regular scatter plot tries to come up with a single fit that will work with all of the data points simultaneously. 
# Make list of accuracy values
accb <- list(acc3b*100, acc5b*100, acc10b*100, acc15b*100, acc20b*100, acc25b*100)

# Accuracy plot binary dataset
accb <- as.numeric(accb)
k <- as.numeric(k)
bin_acc <- cbind(k[1:6], accb[1:6])
bin_acc <- as.data.frame(bin_acc)
bin_acc_plot <- ggplot(bin_acc, aes(x = k, y = accb, group = 1))
bin_acc_plot + geom_point(color = "darkred", shape = 18, size = 3.8) + 
  theme(panel.grid = element_line(color = "lightgrey", linewidth = 0.8, linetype = 1),
        panel.background = element_rect(color = "white", fill = "darkgrey")) +
  labs(title = "Binary Accuracy Plot", x ="K", 
       y = "Accuracy") + xlim(0, 25) + ylim(75, 100)

# Trinary knn model
# Create objects for the knn model of the trinary dataset
trin_train_index <- createDataPartition(trinary$label, times = 1, p = 0.8, list = FALSE)
trin_train <- trinary[trin_train_index, ]
trin_test <- trinary[-trin_train_index, ]
trin_label <- trinary$label[1:length(trin_train_index)]

# Transform to dataframe
trin_train <- as.data.frame(trin_train)
trin_test <- as.data.frame(trin_test)

# Scale values
trin_train_scale <- scale(trin_train[1:1255, , ])
trin_test_scale <- scale(trin_test[1:1255, , ])

# Re-establish the list of k values for knn
k <- list(3, 5, 10, 15, 20, 25)

# Make trinary knn models
trin_pred_3 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[1])
trin_pred_5 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[2])
trin_pred_10 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[3])
trin_pred_15 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[4])
trin_pred_20 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[5])
trin_pred_25 <- knn.cv(train = trin_train_scale, cl = trin_label, k = k[6])

# Make trinary tables
cm3 <- table(trin_label, trin_pred_3)
cm5 <- table(trin_label, trin_pred_5)
cm10 <- table(trin_label, trin_pred_10)
cm15 <- table(trin_label, trin_pred_15)
cm20 <- table(trin_label, trin_pred_20)
cm25 <- table(trin_label, trin_pred_25)

# Find accuracy of trinary knn models
acc3 <- sum(diag(cm3))/length(trin_label)
sprintf("Accuracy for k = 3: %.2f%%", acc3*100)
acc5 <- sum(diag(cm5))/length(trin_label)
sprintf("Accuracy for k = 5: %.2f%%", acc5*100)
acc10 <- sum(diag(cm10))/length(trinary$label)
sprintf("Accuracy for k = 10: %.2f%%", acc10*100)
acc15 <- sum(diag(cm15))/length(trinary$label)
sprintf("Accuracy for k = 15: %.2f%%", acc15*100)
acc20 <- sum(diag(cm20))/length(trinary$label)
sprintf("Accuracy for k = 20: %.2f%%", acc20*100)
acc25 <- sum(diag(cm25))/length(trinary$label)
sprintf("Accuracy for k = 25: %.2f%%", acc25*100)

# Accuracy list
acct <- list(acc3, acc5, acc10, acc15, acc20, accb)

# Accuracy plot trinary
k <- as.numeric(k)
acct <- as.numeric(unlist(acct))
acct <- acct[! acct < 1]
trin_acc <- cbind(k[1:6], acct[6:11])
trin_acc <- as.data.frame(trin_acc)
trin_acc_plot <- ggplot(trin_acc, aes(x = k, y = acct, group = 1))
trin_acc_plot + geom_point(color = "darkred", shape = 18, size = 3.8) + 
  theme(panel.grid = element_line(color = "lightgrey", linewidth = 0.8, linetype = 1),
        panel.background = element_rect(color = "white", fill = "darkgrey")) +
  labs(title = "Trinary Accuracy Plot", x ="K", 
       y = "Accuracy") + xlim(0, 25) + ylim(75, 100)


# K-means clustering
# Look at clustering data
head(clust)

# Plot clustering data
clust_plot <- ggplot(clust, aes(x = x, y = y, group = 1))
clust_plot + geom_point(color = "darkgreen", shape = 18, size = 0.8) + 
  theme(panel.grid = element_line(color = "lightgrey", linewidth = 0.8, linetype = 1),
        panel.background = element_rect(color = "white", fill = "darkgrey")) +
  labs(title = "Cluster Raw Data (Mario)", x ="X", 
       y = "Y") + xlim(0, 275) + ylim(100, 250)

# Make kmeans models and create their plot objects
km2 <- kmeans(clust, centers = 2, nstart = 20)
p2 <- fviz_cluster(km2, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 2')
km3 <- kmeans(clust, centers = 3, nstart = 20)
p3 <- fviz_cluster(km3, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 3')
km4 <- kmeans(clust, centers = 4, nstart = 20)
p4 <- fviz_cluster(km4, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 4')
km5 <- kmeans(clust, centers = 5, nstart = 20)
p5 <- fviz_cluster(km5, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 5')
km6 <- kmeans(clust, centers = 6, nstart = 20)
p6 <- fviz_cluster(km6, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 6')
km7 <- kmeans(clust, centers = 7, nstart = 20)
p7 <- fviz_cluster(km7, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 7')
km8 <- kmeans(clust, centers = 8, nstart = 20)
p8 <- fviz_cluster(km8, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 8')
km9 <- kmeans(clust, centers = 9, nstart = 20)
p9 <- fviz_cluster(km9, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 9')
km10 <- kmeans(clust, centers = 10, nstart = 20)
p10 <- fviz_cluster(km10, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 10')
km11 <- kmeans(clust, centers = 11, nstart = 20)
p11 <- fviz_cluster(km11, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 11')
km12 <- kmeans(clust, centers = 12, nstart = 20)
p12 <- fviz_cluster(km12, geom = "point", data = clust, choose.vars = km2$cluster) + ggtitle('k = 12')

# Print plots of kmeans clusters
grid.arrange(p2, p3, p4, p5, nrow = 4)
grid.arrange(p6, p7, p8, p9, nrow = 4)
grid.arrange(p10, p11, p12, nrow = 3)

# Calculating the averages
wss2 <- km2$tot.withinss/2
wss3 <- km3$tot.withinss/3
wss4 <- km4$tot.withinss/4
wss5 <- km5$tot.withinss/5
wss6 <- km6$tot.withinss/6
wss7 <- km7$tot.withinss/7
wss8 <- km8$tot.withinss/8
wss9 <- km9$tot.withinss/9
wss10 <- km10$tot.withinss/10
wss11 <- km11$tot.withinss/11
wss12 <- km12$tot.withinss/12

# Make kmeans table and plot
km <- list(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
km <- as.numeric(km)
wss <- list(wss2, wss3, wss4, wss5, wss6, wss7, 
            wss8, wss9, wss10, wss11, wss12)
wss <- as.numeric(wss)
wss_df <- tibble(km, wss)
wss_df
scree_plot <- ggplot(wss_df, aes(x = km, y = wss, group = 1)) + 
  geom_point(size = 4) + geom_line() + 
  scale_x_continuous(breaks = c(2, 4, 6, 8, 10, 12)) + xlab('Number of clusters')
scree_plot
# I'd say the "right" number of clusters would be five based
# on the elbow of the plot.