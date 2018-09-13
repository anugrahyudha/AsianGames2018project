library(dplyr)

country_medal_table <- read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_country_medal_table.csv")

medallists <- read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_medallists.csv")
wm_medallists <- read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_women_medallists.csv")
mn_medallists <- read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_men_medallists.csv")


summary(wm_medallists) #unstandardized lower & upper case of name & surname
#surname 'NA' =/= Not Available

table(wm_medallists$country, wm_medallists$sport)

ath_mn_medallists <-read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_athlete_men_medallists.csv")

summary(ath_mn_medallists) #unstandardized lower & upper case of name & surname
summary(factor(ath_mn_medallists$age))

summary(ath_mn_medallists$birth_country)


ath_wm_medallists <-read.csv("D:/Portofolio Data Scientist/scraping asian games 2018/ag2018_athlete_women_medallists.csv")

summary(ath_wm_medallists) #unstandardized lower & upper case of name & surname
View(ath_wm_medallists)
#surname 'NA' =/= Not Available

summary(factor(ath_wm_medallists$age))


#ath_wm_medallists$social = ""

ath_medallists = rbind(ath_wm_medallists, ath_mn_medallists)
#Error in rbind(deparse.level, ...) : 
# numbers of columns of arguments do not match
#Belum ada kolom social di women

summary(ath_medallists)
View(ath_medallists)

ath_medallists$id = as.integer(row.names(ath_medallists))
ath_medallists <- ath_medallists %>%
  mutate(gender = factor(case_when(id < 1463 ~ "female",
                                   TRUE ~ "male")))#WHY OH WHY GAK IKUTAN KENA ORDER DI BAWAH INI HUHUHU
all <- ath_medallists[with(ath_medallists, order(-gold, -silver, -bronze)),]
rownames(all) <- 1:nrow(all)
View(all)


# Ubah tipe data dari variabel 'bio' menjadi character
ath_wm_medallists$bio <- as.character(ath_wm_medallists$bio)
# Variabel 'url' sebenarnya adalah variabel identifier, karena tidak ada yang sama (unique) --> Ubah tipe data variabel 'url' menjadi character
ath_wm_medallists$url <- as.character(ath_wm_medallists$url)
# Variabel 'bio_url' sebenarnya adalah variabel identifier, karena tidak ada yang sama (unique) --> Ubah tipe data variabel 'bio_url' menjadi character
ath_wm_medallists$bio_url <- as.character(ath_wm_medallists$bio_url)


# Ubah tipe data dari variabel 'bio' menjadi character
ath_mn_medallists$bio <- as.character(ath_mn_medallists$bio)
# Variabel 'url' sebenarnya adalah variabel identifier, karena tidak ada yang sama (unique) --> Ubah tipe data variabel 'url' menjadi character
ath_mn_medallists$url <- as.character(ath_mn_medallists$url)
# Variabel 'bio_url' sebenarnya adalah variabel identifier, karena tidak ada yang sama (unique) --> Ubah tipe data variabel 'bio_url' menjadi character
ath_mn_medallists$bio_url <- as.character(ath_mn_medallists$bio_url)


summary(ath_wm_medallists$birth_country)

table(ath_wm_medallists$nationality, ath_wm_medallists$birth_country)


#ath_wm_medallists$birth_country_code = NA #bisa pakai ini, atau di akhir case_when, diberikan TRUE ~ "", hasil lebih baik dalam tampilan View

ath_wm_medallists <- ath_wm_medallists %>% 
  mutate(birth_country_code = factor(case_when(birth_country == 'Bahrain' ~ "BRN",
                                               birth_country == 'Cambodia' ~ "CAM",
                                               birth_country == 'Canada' ~ "CAN",
                                               birth_country == 'China' ~ "CHN",
                                               birth_country == 'Chinese Taipei' ~ "TPE",
                                               birth_country == 'DPR Korea' ~ "PRK",
                                               birth_country == 'Ethiopia' ~ "ETH",
                                               birth_country == 'Hong Kong, China' ~ "HKG",
                                               birth_country == 'India' ~ "IND",
                                               birth_country == 'Indonesia' ~ "INA",
                                               birth_country == 'Islamic Republic of Iran' ~ "IRI",
                                               birth_country == 'Japan' ~ "JPN",
                                               birth_country == 'Jordan' ~ "JOR",
                                               birth_country == 'Kazakhstan' ~ "KAZ",
                                               birth_country == 'Kenya' ~ "KEN",
                                               birth_country == 'Kyrgyzstan' ~ "KGZ",
                                               birth_country == "Lao People's Democratic Republic" ~ "LAO",
                                               birth_country == 'Lebanon' ~ "LBN",
                                               birth_country == 'Macau, China' ~ "MAC",
                                               birth_country == 'Malaysia' ~ "MAS",
                                               birth_country == 'Mongolia' ~ "MGL",
                                               birth_country == 'Morocco' ~ "MAR",
                                               birth_country == 'Myanmar' ~ "MYA",
                                               birth_country == 'Nigeria' ~ "NGR",
                                               birth_country == 'Pakistan' ~ "PAK",
                                               birth_country == 'Philippines' ~ "PHI",
                                               birth_country == 'Republic of Korea' ~ "KOR",
                                               birth_country == 'Singapore' ~ "SGP",
                                               birth_country == 'Thailand' ~ "THA",
                                               birth_country == 'Turkmenistan' ~ "TKM",
                                               birth_country == 'United Arab Emirates' ~ "UAE",
                                               birth_country == 'United States' ~ "USA",
                                               birth_country == 'Uzbekistan' ~ "UZB",
                                               birth_country == 'Vietnam' ~ "VIE", #)))
                                               TRUE ~ "")))

table(ath_wm_medallists$nationality, ath_wm_medallists$birth_country_code)

ath_wm_medallists <- ath_wm_medallists %>% 
  mutate(naturalized = factor(case_when(as.character(birth_country_code) == "" ~ -1, #kasih tagar di awal
                                        as.character(birth_country_code) == as.character(nationality) ~ 0,
                                        as.character(birth_country_code) != as.character(nationality) ~ 1)))


#ath_wm_medallists$naturalized = NA

ath_wm_medallists <- ath_wm_medallists %>% 
  mutate(naturalized = factor(case_when(as.character(birth_country_code) == as.character(nationality) ~ 0,
                                        as.character(birth_country_code) != as.character(nationality) ~ 1)))

summary(ath_wm_medallists)

ath_wm_medallists[ath_wm_medallists$naturalized == 1,]
View(ath_wm_medallists[ath_wm_medallists$naturalized == 1,])


#ath_mn_medallists$birth_country_code = ""

ath_mn_medallists <- ath_mn_medallists %>% 
  mutate(birth_country_code = factor(case_when(birth_country == 'Australia' ~ "AUS",
                                               birth_country == 'Bahrain' ~ "BRN",
                                               birth_country == 'Belgium' ~ "BEL",
                                               birth_country == 'Cambodia' ~ "CAM",
                                               birth_country == 'China' ~ "CHN",
                                               birth_country == 'Chinese Taipei' ~ "TPE",
                                               birth_country == 'DPR Korea' ~ "PRK",
                                               birth_country == 'Egypt' ~ "EGY",
                                               birth_country == 'Ethiopia' ~ "ETH",
                                               birth_country == 'Georgia' ~ "GEO",
                                               birth_country == 'Great Britain' ~ "GBR",
                                               birth_country == 'Hong Kong, China' ~ "HKG",
                                               birth_country == 'India' ~ "IND",
                                               birth_country == 'Indonesia' ~ "INA",
                                               birth_country == 'Iraq' ~ "IRQ",
                                               birth_country == 'Islamic Republic of Iran' ~ "IRI",
                                               birth_country == 'Jamaica' ~ "JAM",
                                               birth_country == 'Japan' ~ "JPN",
                                               birth_country == 'Jordan' ~ "JOR",
                                               birth_country == 'Kazakhstan' ~ "KAZ",
                                               birth_country == 'Kenya' ~ "KEN",
                                               birth_country == 'Kingdom of Saudi Arabia' ~ "KSA",
                                               birth_country == 'Kuwait' ~ "KUW",
                                               birth_country == 'Kyrgyzstan' ~ "KGZ",
                                               birth_country == "Lao People's Democratic Republic" ~ "LAO",
                                               birth_country == 'Lebanon' ~ "LBN",
                                               birth_country == 'Macau, China' ~ "MAC",
                                               birth_country == 'Malaysia' ~ "MAS",
                                               birth_country == 'Mongolia' ~ "MGL",
                                               birth_country == 'Morocco' ~ "MAR",
                                               birth_country == 'Nepal' ~ "NEP",
                                               birth_country == 'Netherlands' ~ "NED",
                                               birth_country == 'Nigeria' ~ "NGR",
                                               birth_country == 'Pakistan' ~ "PAK",
                                               birth_country == 'Philippines' ~ "PHI",
                                               birth_country == 'Qatar' ~ "QAT",
                                               birth_country == 'Republic of Korea' ~ "KOR",
                                               birth_country == 'Russia' ~ "RUS",
                                               birth_country == 'Singapore' ~ "SGP",
                                               birth_country == 'Sudan' ~ "SUD",
                                               birth_country == 'Syria Arab Republic' ~ "SYR",
                                               birth_country == 'Tajikistan' ~ "TJK",
                                               birth_country == 'Thailand' ~ "THA",
                                               birth_country == 'Turkey' ~ "TUR",
                                               birth_country == 'Turkmenistan' ~ "TKM",
                                               birth_country == 'United Arab Emirates' ~ "UAE",
                                               birth_country == 'United States' ~ "USA",
                                               birth_country == 'Uzbekistan' ~ "UZB",
                                               birth_country == 'Vietnam' ~ "VIE",
                                               birth_country == 'Yemen' ~ "YEM", #)))
                                               TRUE ~ "")))

#ath_mn_medallists$naturalized = ""

ath_mn_medallists <- ath_mn_medallists %>% 
  mutate(naturalized = factor(case_when(as.character(birth_country_code) == "" ~ -1, #kasih tagar di awal
                                        as.character(birth_country_code) == as.character(nationality) ~ 0,
                                        as.character(birth_country_code) != as.character(nationality) ~ 1)))

summary(ath_mn_medallists)

ath_mn_medallists[ath_mn_medallists$naturalized == 1,] #bagaimana caranya menghilangkan row yang berisikan NA?
View(ath_mn_medallists[ath_mn_medallists$naturalized == 1,])

ath_mn_medallists %>%
  filter(naturalized == 1) %>%
  group_by(nationality, birth_country) %>% 
  summarize(count = n()) #count per gold, silver, bronze
