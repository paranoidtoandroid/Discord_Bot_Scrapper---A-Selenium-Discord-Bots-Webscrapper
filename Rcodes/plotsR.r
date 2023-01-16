

# Load the required libraries
library(tidyverse)
library(car)

# Load the data from the CSV file
df <- read.csv("discord_bots.csv")

# Extract the tags from the data
tags <- unlist(strsplit(as.character(df$tags), ","))

# Count the number of occurrences of each tag
tag_counts <- table(tags)

# Get the 10 most common tags
most_common_tags <- head(sort(tag_counts, decreasing = TRUE), 10)

# Extract the tag names and counts
tag_names <- names(most_common_tags)
tag_counts <- most_common_tags

#ANOVA TEST


# Load the required packages
library(tidyverse)
library(car)


# Convert the tags column from a list to a character vector
df <- df %>% mutate(tags = map_chr(tags, paste, collapse = ", "))

# Conduct the ANOVA test
aov_result <- aov(votes ~ tags, data = df)

# Print the ANOVA table
summary(aov_result)

