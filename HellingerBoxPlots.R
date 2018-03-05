# This code is used after results of model are first processed in python code and common_theta.csv has been generated
# I used this code to generat hellinger box plots in the paper

setwd('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare')

data <- read.csv('/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/target_to_peer_data_out.csv',
                 stringsAsFactors = FALSE,sep = " ",header= FALSE)

library(reshape2)
library(ggplot2)

colnames(data) <- c('Hellinger')

data$Target <- "1"



bp <- ggplot() + geom_boxplot(data = data,aes(x = factor(0),y = Hellinger)) + scale_shape_identity()+ 
  scale_shape_discrete(solid = T)+
  geom_point(data = data[data$Hellinger == 0,],size = 5, shape  = 18, colour = 'black' ,aes(x = factor(0), y = Hellinger)) +
  theme(axis.title.x  = element_blank(), axis.ticks = element_blank(), axis.text.x = element_blank())
  #geom_point(data = melt_target_data,aes(x = cluster, y = theta, color = 'RED', size = 20))


bp <- bp + scale_color_discrete(guide = FALSE)
bp <- bp + scale_size_continuous(guide = FALSE)
print(bp)