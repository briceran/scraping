getwd()
setwd('/Users/bricerandolph/Desktop/myrepos/scraping')
list.files(getwd())
archs = read.csv('architects.csv')
str(archs)
vec = c()


for (i in 1:dim(archs)[1]){
  rawnum= archs[i,1]
  areacode = substr(rawnum,1,3)
  head = substr(rawnum,4,6)
  tail = substr(rawnum, 7, 10)
  phone = c('(', areacode , ')',head,'-',tail)
  final = paste(phone, collapse = '')
  vec = c(vec,final)
}
vec
str(vec)
df = data.frame(vec)
str(df)
write.csv(df,file="archs.csv")
getwd()
