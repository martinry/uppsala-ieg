library(ggthemes)
library(ggplot2)
library(maptools)
library(mapproj)
library(maps)
library(ggrepel)
library(dplyr)

setwd("/home/martin/uppsala-ieg")

world <- map_data("world")

#### berbee
denovo12 <- read.csv("denovo12.csv", sep = "\t", header = TRUE, dec = ',')
denovo12$Id <- factor(denovo12$Id)

#lat_lim <- c(30, 75)
#long_lim <- c(-160, 50)

lat_lim <- c(20, 75)
long_lim <- c(-40, 90)

p <- ggplot(world, mapping = aes(x = long, y = lat, group = group)) +
  geom_polygon(fill="gray80") +
  coord_cartesian(xlim = long_lim, lat_lim) +
  ggtitle("Archaeorhizomyces victus") +
  theme(axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        panel.background = element_rect(fill = "gray98"),
        panel.grid.major = element_line(color = "white"),
        axis.title.y=element_blank(),
        axis.title.x=element_blank())

p <-
  p + geom_text_repel(
    data = denovo12,
    inherit.aes = FALSE,
    #show.legend = NA,
    aes(x = Long, y = Lat, label = Id),
    colour = "black",
    size = 4
  )

p <-
  p + geom_jitter(
    data = denovo12,
    inherit.aes = FALSE,
    #show.legend = NA,
    position = position_jitter(width = 0.5, height = 0.5),
    size = 3,
    aes(x = Long, y = Lat, col = Ref)
  )

p



##########



#### jaedraasi

jaedraasi <- read.csv("jaedraasensis.csv", sep = "\t", header = TRUE, dec = ',')

#jaedraasensis
lat_lim <- c(30, 75)
long_lim <- c(-100, 70)

p <- ggplot(world, mapping = aes(x = long, y = lat, group = group)) +
  geom_polygon(fill="gray80") +
  coord_cartesian(xlim = long_lim, lat_lim) +
  ggtitle("Archaeorhizomyces jaedraasensis") +
  theme(axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        panel.background = element_rect(fill = "gray98"),
        panel.grid.major = element_line(color = "white"),
        axis.title.y=element_blank(),
        axis.title.x=element_blank())

p <-
  p + geom_text_repel(
    data = jaedraasi,
    inherit.aes = FALSE,
    show.legend = NA,
    aes(x = Long, y = Lat, label = Id),
    colour = "black",
    size = 4
  )

p <-
  p + geom_jitter(
    data = jaedraasi,
    inherit.aes = FALSE,
    show.legend = NA,
    position = position_jitter(width = 0.5, height = 0.5),
    size = 3,
    aes(x = Long, y = Lat, col = Ref)
  )

p

######


#### humophilus

humophilus <- read.csv("humophilus.csv", sep = "\t", header = TRUE, dec = ',')

#humophilus
lat_lim <- c(20, 85)
long_lim <- c(-130, 150)

p <- ggplot(world, mapping = aes(x = long, y = lat, group = group)) +
  geom_polygon(fill="gray80") +
  coord_cartesian(xlim = long_lim, lat_lim) +
  ggtitle("Archaeorhizomyces humophilus") +
  theme(axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        panel.background = element_rect(fill = "gray98"),
        panel.grid.major = element_line(color = "white"),
        axis.title.y=element_blank(),
        axis.title.x=element_blank())

p <-
  p + geom_text_repel(
    data = humophilus,
    inherit.aes = FALSE,
    show.legend = NA,
    aes(x = Long, y = Lat, label = Id),
    colour = "black",
    size = 4
  )

p <-
  p + geom_jitter(
    data = humophilus,
    inherit.aes = FALSE,
    show.legend = NA,
    position = position_jitter(width = 0.5, height = 0.5),
    size = 3,
    aes(x = Long, y = Lat, col = Ref)
  )

p

######


#### denovo0

denovo0 <- read.csv("denovo0.csv", sep = "\t", header = TRUE, dec = ',')

#denovo0
lat_lim <- c(20, 75)
long_lim <- c(-25, 50)

p <- ggplot(world, mapping = aes(x = long, y = lat, group = group)) +
  geom_polygon(fill="gray80") +
  coord_cartesian(xlim = long_lim, lat_lim) +
  ggtitle("Archaeorhizomyces victorem") +
  theme(axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        panel.background = element_rect(fill = "gray98"),
        panel.grid.major = element_line(color = "white"),
        axis.title.y=element_blank(),
        axis.title.x=element_blank())

p <-
  p + geom_text_repel(
    data = denovo0,
    inherit.aes = FALSE,
    show.legend = NA,
    aes(x = Long, y = Lat, label = Id),
    colour = "black",
    size = 4
  )

p <-
  p + geom_jitter(
    data = denovo0,
    inherit.aes = FALSE,
    show.legend = NA,
    position = position_jitter(width = 0.5, height = 0.5),
    size = 3,
    aes(x = Long, y = Lat, col = Ref)
  )

p

