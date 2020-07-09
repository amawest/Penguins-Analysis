# Module 6 Visualization Test (R & Python)
# Palmer Penguins Dataset
# Github: https://github.com/allisonhorst/palmerpenguins

# 1: Import Data  ------------------------------------

rm(list=ls())
setwd("~/Desktop/r_notes")                 # best & simplest. 

penguins <- read.csv(header=TRUE, file = "penguins_size.csv")
penguins_no_nas <- na.omit(penguins) # remove missing values from data frame

# 2: Data Exploration --------------------------------

head(penguins)

library(dplyr)  # so we can use the pipe
penguins %>% 
  group_by(species) %>% 
  summarize(across(where(is.numeric), mean, na.rm = TRUE))

# 3: Data visualization ------------------------------

# 3.1: create a correlation matrix
penguins_cor <- na.omit(penguins[, c(3,4,5,6)])
res <- cor(penguins_cor)
round(res, 2)
# matches Python - check. 

# 3.2: graph a scatterplot in the same way as Python 
install.packages("plotly")
library(plotly)

plot_ly(penguins, 
        x = ~flipper_length_mm,
        y = ~body_mass_g, 
        color = ~flipper_length_mm, 
        size = ~flipper_length_mm) %>%
  layout(xaxis = list(title = "Flipper Length (mm)"),
         yaxis = list (title = "Body Mass (g)"))

plot_ly(penguins, 
        x = ~flipper_length_mm,
        y = ~body_mass_g, 
        color = ~species, 
        size = ~flipper_length_mm) %>%
  layout(xaxis = list(title = "Flipper Length (mm)"),
         yaxis = list (title = "Body Mass (g)"))
