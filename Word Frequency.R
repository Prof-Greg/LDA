# Code to take document set and calcualte the relative word frequency of all the words.
# Uses python coded preprocessing as input
#Outputs stop word analysis

library("tm", lib.loc="/Users/greglakomski/lib/R")
library("plyr", lib.loc="/Users/greglakomski/lib/R")
#setwd('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/test')
setwd('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare')
#data <- read.table('test.csv',stringsAsFactors = TRUE,sep = '',header=FALSE, fill = TRUE)
data <- read.csv('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array4.csv',nrows = 2461,stringsAsFactors = FALSE,sep = "",header= FALSE)
data <- data[-1,]
#data <- data[-1,]
review_text <- paste(data, collapse=" ")
source <- VectorSource(review_text)
corpus <- Corpus(source)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, stripWhitespace)
dtm <- DocumentTermMatrix(corpus)
dtm2 <- as.matrix(dtm)
frequency <- colSums(dtm2)
frequency <- sort(frequency, decreasing=TRUE)
head(frequency)
library("wordcloud", lib.loc="/Users/greglakomski/lib/R")
words <- names(frequency)
wordcloud(words[1:100], frequency[1:100])
freq_list <- cbind(words,frequency)
freq_list <- as.data.frame(freq_list)
freq_list$per <- freq_list$frequency
freq_list$cum <- freq_list$frequency
freq_list$delta <- freq_list$per

i <- sapply(freq_list, is.factor)
freq_list[i] <- lapply(freq_list[i], as.character)
freq_list$frequency <- as.numeric(freq_list$frequency)
freq_list$per <- as.numeric(freq_list$per)
freq_list$delta <- as.numeric(freq_list$delta)

for ( i in 1: nrow(freq_list))
{
  freq_list$per <-  freq_list$frequency / sum(freq_list$frequency)
}

freq_list$cum <- freq_list$per

for ( i in 2: nrow(freq_list))
{
  freq_list$cum[i] <-  freq_list$cum[i] + freq_list$cum[i-1]
}

for ( i in 2: nrow(freq_list))
{
  freq_list$delta[i] <-  freq_list$cum[i] - freq_list$cum[i-1]
}

cbind(words,frequency)


# Seperates out the highest freq terms - I picked the dividing line after looking at the output
stop <- freq_list[freq_list$delta > .02,]
stop  <- stop[[1]]

write.table(freq_list,'/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/stopaanlysis.csv',sep = "")


