
# This code is used after results of model are first processed in python code and common_theta.csv has been generated
# I used this code to generat theta box plots in the paper

setwd('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare')
s
data <- read.csv('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/common_theta.csv',stringsAsFactors = FALSE,sep = " ",header= FALSE)

library(reshape2)
library(ggplot2)

colnames(data) <- c('Topic 1','Topic 2','Topic 3','Topic 4','Topic 5','Topic 6','Topic 7','Topic 8','Topic 9','Topic 10','Topic 11','Topic 12')

meltdata <- melt(data[1:12])

colnames(meltdata) <- c('cluster','theta')

meltdata <- meltdata[which (meltdata$cluster == 'Topic 1'| meltdata$cluster == 'Topic 4'| meltdata$cluster == 'Topic 8'| meltdata$cluster == 'Topic 10'),]

#melt2 <- meltdata[meltdata$theta>.5,]

melt2 <- meltdata

target_data <- data[3,c(1,4,8,10)]

melt_target_data <- melt(target_data)

colnames(melt_target_data) <- c('cluster','theta')

melt2$cluster <- factor(melt2$cluster,levels = c("Topic 4","Topic 1","Topic 8","Topic 10"),ordered = TRUE)

bp <- ggplot() + geom_boxplot(data = melt2,aes(x = cluster, y = theta)) +scale_shape_identity()+ scale_shape_discrete(solid = T)+
  geom_point(data = melt2[melt2$cluster == 'Topic 8',],aes(x = cluster, y = theta))+
  geom_point(data = melt_target_data,size = 7,shape =17,aes(x = cluster, y = theta))


bp <- bp + scale_color_discrete(guide = FALSE)
bp <- bp + scale_size_continuous(guide = FALSE)
print(bp)