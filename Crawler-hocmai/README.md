# Crawler - Hocmai

code crawl từ web hocmai 

Cấu trúc thư mục (Thư mục này độc lập với DV-Final-Crawler)


```
CRAWLER-HOCMAI/
├── data/
│   ├── full/                                       <- Data đã crawl về và được cấu trúc lại phù hợp
│   │   ├── diemchuan2018_demo.csv                  <- 3495 dòng dữ liệu. File này chưa full lắm (sẽ update sau).
│   │   ├── diemchuan2019_full.csv                  <- 5706 dòng dữ liệu.
│   │   ├── diemchuan2020_full.csv                  <- 4924 dòng dữ liệu.
│   │   ├── diemchuan2021_full.csv                  <- 6561 dòng dữ liệu.
│   │   ├── diemchuan2022_full.csv                  <- 7991 dòng dữ liệu.
│   │   ├── diemchuan2023_full.csv                  <- 7947 dòng dữ liệu.
│   │
│   ├── preprocessing/                              <- Dữ liệu sau khi chạy file `preprocessing.ipynb`
│   │   ├── DGNL.csv
│   │   ├── full.csv
│   │   ├── hocba.csv
│   │   ├── THPT.csv
│   │
│   ├── university/                                 <- Dữ liệu trường đại học (dùng để crawl)
│   │   ├── university.csv
│   │
│   ├── diemchuan_full.csv                          <- Dữ liệu ĐÃ XỬ LÝ GẦN NHƯ HOÀN TẤT.
│
├── crawler_hocmai(bug).ipynb                       <- Code để crawl dữ liệu, chạy được nhưng không xuất được output như ý.
│
├── preprocessing.ipynb                             <- Preprocessing output tách nhỏ 4 file.
│
├── preprocessing2.ipynb                            <- Preprocessing output 1 file hoàn chỉnh.
│
├── README.md                                       <= File này.

```
