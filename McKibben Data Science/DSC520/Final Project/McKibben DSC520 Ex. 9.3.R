# Makayla McKibben
# Final Project 9.3
# Week 9
# 08.04.2024

# Import necessary packages
install.packages("tidyverse")
library(tidyverse)

# Import all data files
healthanxiety <- 
  read.csv(file = 'healthanxiety_dataset.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

indicators_anxiety <- 
  read.csv(file = 'Indicators_of_Anxiety_or_Depression.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

global_mental <- 
  read.csv(file = 'Mental Health Data Global.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

mental <- 
  read.csv(file = 'Mental Health Dataset.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

prevalence <- 
  read.csv(file = 'prevalence-of-anxiety-disorders-males-vs-females.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

meds <- 
  read.csv(file = 'psychiatric_drug_webmd_reviews.csv', header = TRUE, sep =",", stringsAsFactors = FALSE)

# Check out the data
# First dataset
head(healthanxiety)
# I don't believe this data is actually useful for me. There's lots of data but not useful for this particalur analysis

# Second dataset
head(indicators_anxiety)
# Turn data into a df
indicators_anxiety <- as.data.frame(indicators_anxiety)
# Find unique indicators
unique(indicators_anxiety$Indicator)
# Filter for only anxiety not depression
indicators_anxiety <- filter(indicators_anxiety, Indicator == 'Symptoms of Anxiety Disorder')
# Validate that it worked
head(indicators_anxiety, 8)

# Third dataset
head(global_mental)
# Turn data into a df
global_mental <- as.data.frame(global_mental)
# Remove columns that we don't need
colnames(global_mental)
global_mental <- subset(global_mental, select = -c(Schizophrenia...., Bipolar.disorder...., Eating.disorders...., Drug.use.disorders...., Depression...., Alcohol.use.disorders....))
# Remove rows missing data
global_mental <- global_mental[complete.cases(global_mental),]
# Rename 
global_mental <- global_mental %>% 
  rename(anxiety = Anxiety.disorders....)
# Check that the data has been trimmed down
head(global_mental, 8)

# Fourth dataset
head(mental)
# Turn data into dataframe
mental <- as.data.frame(mental)
# Remove columns that we don't need 
colnames(mental)
mental <- subset(mental, select = -c(Occupation, self_employed, family_history, Days_Indoors, Growing_Stress, Changes_Habits, Mental_Health_History, Mood_Swings, Coping_Struggles, Work_Interest, Social_Weakness, mental_health_interview, care_options))
# Remove rows missing data
mental <- mental[complete.cases(mental),]
# Check that the data has been trimmed
head(mental, 8)

# Fifth dataset
head(prevalence)
# Turn data into dataframe
prevalence <- as.data.frame(prevalence)
# Remove columns that we don't need
colnames(prevalence)
prevalence <- subset(prevalence, select = -c(Continent, Population..historical.estimates.))
# Rename columns
prevalence <- prevalence %>% 
  rename(index = index, entity = Entity, code = Code, year = Year, male = Prevalence...Anxiety.disorders...Sex..Male...Age..Age.standardized..Percent., female = Prevalence...Anxiety.disorders...Sex..Female...Age..Age.standardized..Percent.)
# Check changes
head(prevalence, 8)

# Sixth dataset
head(meds)
# Turn data into dataframe
meds <- as.data.frame(meds)
# Remove columns that we don't need
colnames(meds)
meds <- subset(meds, select = -c(time_on_drug, text))
# Find conditions that are anxiety related
unique(meds$condition)
# The following would qualify as something I don't know how to do that could be helpful to know.
# I don't know if there is a way to iterate through the unique items in the condition column and find conditions that are anxiety related using R.
# I would imagine it could be done through a loop and doing a partial match to condition which contains the letters "anx".
# I looked through the printed conditions myself and then coded the following lines

# Remove rows that aren't anxiety related
meds <- subset(meds, condition == "Anxious" | condition == "Severe Anxiety" | condition == "Repeated Episodes of Anxiety")
# Remove rows that have missing values
meds <- meds[complete.cases(meds),] 
# Check changes
head(meds, 8)

# Summarize all datasets 
head(indicators_anxiety, 8)
head(global_mental, 8)
head(mental, 8)
head(prevalence, 8)
head(meds, 8)
