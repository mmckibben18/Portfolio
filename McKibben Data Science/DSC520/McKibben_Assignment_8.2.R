# Makayla McKibben
# DSC520
# Week 8
# Exercise 8.2
# 07.29.2024



# Install and call relevant packages
install.packages("purrr")
library(purrr)
install.packages("tidyverse")
library(stringr)
library(dplyr)
install.packages("ggplot2")
library(ggplot2)
install.packages("Metrics")
library(car)
library(Metrics)


# Call and clean housing data
housing <- read.csv(file = 'Housing.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

# Take a quick look to see how the data is structured
head(housing, 5)
# Group the needed data
mod_sq_ft <- cbind(housing$Sale.Price, housing$sq_ft_lot)
# Assign relevant headers
colnames(mod_sq_ft) <- c("Sales Price", "Lot sq. ft.")
# Check structure of new data set
head(mod_sq_ft, 5)
# Turn it into a data frame
mod_sq_ft <- as.data.frame(mod_sq_ft)
# Check structure of new data set
class(mod_sq_ft)
head(mod_sq_ft, 5)
# Remove empty rows
mod_sq_ft <- mod_sq_ft[complete.cases(mod_sq_ft),]
# Check structure of new data set
class(mod_sq_ft)
head(mod_sq_ft, 5)
# Plot data to get an idea of the relationship
plot(mod_sq_ft$`Lot sq. ft.`, mod_sq_ft$`Sales Price`)
# Create model
model_sq_ft <- lm(`Sales Price` ~ `Lot sq. ft.`, data = mod_sq_ft)
# Check values
summary(model_sq_ft)

# Explain results
# R2 is 0.01435 and adj. R2 is 0.01428, this converts to an accuracy of 1% for prediction of sales price from lot square footage.
# The intercept is 641800 with a standard error of 3800. The slope is 0.851 with a std. error of 0.0622.
# The F-ratio is 187.3 with a p-value of 2.2e-16 so we should consider that it is significant.

# Get residuals
mod_sq_ft$residuals <- resid(model_sq_ft)
mod_sq_ft$std_residuals <- rstandard(model_sq_ft)
mod_sq_ft$stud_residuals <- rstudent(model_sq_ft)

# Plot residuals
plot(model_sq_ft)
hist(mod_sq_ft$std_residuals)
qqPlot(mod_sq_ft$residuals)

# Explain results
# The Residuals vs. Fitted data is not an even distribution. There is a group that is more concentrated and overall it makes the general shape of a triangle indicating Heteroscedasticity.

# Explain qq plot
# The qq plot shows the residuals form a sigmoid shape that deviates from the central line, this indicates that the residuals are not normally distributed. This is verified by a histogram of the standardized residuals.

# Create new variable that combines the total number of bedrooms and bathrooms
bed_bath <- housing$bedrooms + housing$bath_full_count + housing$bath_half_count + housing$bath_3qtr_count
# Group the needed data
mod_mp <- cbind(housing$Sale.Price, housing$square_feet_total_living, bed_bath)
# Assign relevant headers
colnames(mod_mp) <- c("Sales Price", "Sq. ft. Total Living", "Bedrooms + Bathrooms")
# Check structure of new data set
head(mod_mp, 5)
# Turn it into a data frame
mod_mp <- as.data.frame(mod_mp)
# Check structure of new data set
class(mod_mp)
head(mod_mp, 5)
# Remove empty rows
mod_mp <- mod_mp[complete.cases(mod_mp),]
# Check structure of new data set
class(mod_mp)
head(mod_mp, 5)
# I believe that liveable square feet and the number of bedrooms and bathrooms are going to be better indicators of sales price than the size of the lot the house is on.
# People often have requirements for the number of bedrooms and bathrooms a home may have, this is often more important than the size of the lot.

# Plot data to get an idea of the relationship
plot(mod_mp$`Sq. ft. Total Living`, mod_mp$`Sales Price`)
# Linear, positively correlated

# Plot data to get an idea of the relationship
plot(mod_mp$`Bedrooms + Bathrooms`, mod_mp$`Sales Price`)
# Linear, positively correlated

# Create model
model_mp <- lm(`Sales Price` ~ `Sq. ft. Total Living` + `Bedrooms + Bathrooms`, data = mod_mp)
# Check values
summary(model_mp)

# Explain model results
# The R2 value is .2072 and the adjusted R2 is 0.2071, this indicates that our model predicts 20.7% of our sales price value from the predictor variables. That is nearly 20% better than the first model.
# The intercept is 222,319 with a std. error of 14,106. The b1 (Sq. ft. of the living space) value is 196 with a std. error of 4.8 and b2 (Bedrooms + Bathrooms) is -9578 with a std. error  of 3192.
# The F-ratio is 10x larger than in our previous model and the p-value is < 0.001 so there is a 99.9% chance we reject the null hypothesis.

# Obtain residuals of new model
mod_mp$residuals <- resid(model_mp)
mod_mp$std_residuals <- rstandard(model_mp)
mod_mp$stud_residuals <- rstudent(model_mp)

# Plot residuals
plot(model_mp)
hist(mod_mp$std_residuals)
qqPlot(mod_mp$residuals)

# Explain the residuals
# The Residuals vs. Fitted data is not an even distribution although, it is closer than the previous model. There is a group that is more concentrated and overall it makes the general shape of a triangle indicating Heteroscedasticity.

# Explain qq plot
# The qq plot shows the residuals form a sigmoid shape that deviates from the central line, this indicates that the residuals are not normally distributed. This is verified by checking a histogram of the standardized residuals.

# Anova for comparing both models
anova(model_sq_ft, model_mp)

# Anova comparison
# The anova test gave us an F(1, 12862) = 3128 with a Pr(>F) of < 2.2e-16 which tells us the second model is a significant improvement over the original model.

# Bias comparison
# I believe both models are biased similarly based on comparisons of the residual v fitted and qq plots. The linear fit of both indicate that the low end is biased high and the high end is biased low.

# Prediction accuracy first model
lot_preds <- predict(model_sq_ft, newdata = mod_sq_ft)
lot_rmse <- rmse(mod_sq_ft$`Sales Price`, lot_preds)
lot_rmse

# RMSE for the first model
# 401452.5

# Prediction accuracy second model
mp_preds <- predict(model_mp, newdata = mod_mp)
mp_rmse <- rmse(mod_mp$`Sales Price`, mp_preds)
mp_rmse

# RMSE for second model
# 360043.1

# RMSE Difference
diff_rmse <- lot_rmse - mp_rmse
diff_rmse

# Yes, the second model improved upon the RMSE relative to the first model. The difference is 41409.44