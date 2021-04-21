## ----data----------------------------------------------------------------
col_names=c('instructions','cache-references','cache-misses','branches','branch-misses')
ransom_data <- read.table("ransomware.txt",header=FALSE,sep = ',',col.names=col_names)
str(ransom_data)

regular_data <- read.table("regular.txt",header=FALSE,sep = ',',col.names=col_names)
str(regular_data)

spec_data <- read.table("spec.txt",header=FALSE,sep = ',',col.names=col_names)
str(spec_data)

#install.packages("plotly")
library(plotly)
library(ggplot2)
plot_ly(x = seq(1,2335), y = ransom_data$cache.references, mode = 'lines')
ggplot(ransom_data , aes(x = seq(1,2335))) + 
  geom_line(aes(y = cache.references)) + 
  geom_line(aes(y = cache.misses)) +
  scale_colour_manual(values=c("blue", "orange"))

#install.packages('rnn')
#install.packages("keras")
# install.packages("devtools")
# devtools::install_github("rstudio/keras")
library(keras)
install_tensorflow()

library(rnn)
library(keras)
mod <- keras_model_sequential()
mod %>% 
  layer_dense(units = 256, activation = "relu", input_shape = c(784)) %>% 
  layer_dropout(rate = 0.4) %>% 
  layer_dense(units = 128, activation = "relu") %>%
  layer_dropout(rate = 0.3) %>%
  layer_dense(units = 10, activation = "softmax")

