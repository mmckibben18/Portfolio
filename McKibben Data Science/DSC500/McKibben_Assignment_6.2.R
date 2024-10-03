# Makayla McKibben
# DSC520
# Week 5
# Assignment 5.2

install.packages("purrr")
library(purrr)
install.packages("tidyverse")
library(stringr)
library(dplyr)
install.packages("ggplot2")
library(ggplot2)
install.packages("factoextra")
library(factoextra)

# Importing the data set
housing <- read.csv(file = 'Housing.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

# Checking what's in the data set
str(housing)

# Searching for houses in my price range
f_house <- filter(housing, between(Sale.Price, 0, 1000000), .by = Sale.Price) %>%
  arrange( , desc(Sale.Price), .by_group = TRUE, .locale = "en")

# Checking the results
f_house



complete_sale_f_house <- f_house[complete.cases(f_house$Sale.Price), ]
complete_sq_ft_f_house <- f_house[complete.cases(f_house$square_feet_total_living), ]
complete_lot_f_house <- f_house[complete.cases(f_house$sq_ft_lot), ]
f_house[apply(sapply(f_house, is.finite), 1, all),]
f_house <- select(f_house, c(Sale.Price, square_feet_total_living, bedrooms, sq_ft_lot), -Sale.Date, -sale_reason, -sale_instrument, -sale_instrument, -sitetype, -addr_full, -zip5, -ctyname, -postalctyn, -lon, -lat, -building_grade, -bath_full_count, -bath_half_count, -bath_3qtr_count, -year_built, -year_renovated, -current_zoning, -prop_type, -present_use)

n_clusters <- 5
wss <- numeric(n_clusters)
for (i in 1:5) {
  km <- kmeans(f_house, centers = i, nstart = 20)
  wss[i] <- km$tot.withinss
}


print(km)
head(km)

wss_df <- tibble(clusters = 1:5, wss = wss)
scree_plot <- ggplot(wss_df, aes(x = clusters, y = wss)) + geom_point(size = 4) + geom_line() + scale_x_continuous(breaks = c(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28)) + xlab('Number of Clusters')
scree_plot

# Plotting the data 
sale_price_square_ft_plot <- ggplot(f_house, aes(Sale.Price, square_feet_total_living, color = square_feet_total_living))
sale_price_square_ft_plot + geom_point()

sale_price_bedroom_plot <- ggplot(f_house, aes(Sale.Price, bedrooms, color = bedrooms))
sale_price_bedroom_plot + geom_point()

sale_price_lot_plot <- ggplot(f_house, aes(Sale.Price, sq_ft_lot, color = sq_ft_lot))
sale_price_lot_plot + geom_point()

f_house$cluster_id <- factor(km$cluster)
ggplot(f_house, aes(Sale.Price, square_feet_total_living, color = cluster_id)) + geom_point(alpha = 0.25) + xlab("Price") + ylab("Interior Sq. Ft.")
ggplot(f_house, aes(Sale.Price, bedrooms, color = cluster_id)) + geom_point(alpha = 0.25) + xlab("Price") + ylab("Bedrooms")
ggplot(f_house, aes(Sale.Price, sq_ft_lot, color = cluster_id)) + geom_point(alpha = 0.25) + xlab("Price") + ylab("Lot Sq. Ft.")
