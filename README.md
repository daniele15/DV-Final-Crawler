# Crawler - Hocmai

code crawl từ web hocmai 

Cấu trúc thư mục (Thư mục này độc lập với DV-Final-Crawler)



```
CRAWLER-HOCMAI/
├── data/
│   ├── full/                                       <- Data đã crawl về và được cấu trúc lại phù hợp
│   │   ├── diemchuan2018_full.csv                  <- `4289` dòng dữ liệu. File này chưa full lắm (sẽ update sau).
│   │   ├── diemchuan2019_full.csv                  <- 5706 dòng dữ liệu.
│   │   ├── diemchuan2020_full.csv                  <- 4924 dòng dữ liệu.
│   │   ├── diemchuan2021_full.csv                  <- 6561 dòng dữ liệu.
│   │   ├── diemchuan2022_full.csv                  <- 7991 dòng dữ liệu.
│   │   ├── diemchuan2023_full.csv                  <- 7947 dòng dữ liệu.
│   │
│   ├── university/                                 <- Dữ liệu trường đại học (dùng để crawl)
│   │   ├── university.csv                          <- Update 26/06: Bổ sung Mã xét tuyển, Vị trí (Tỉnh) và Vùng miền.
│   │   ├── nhom_nganh.csv                          <- Update 26/06: Danh mục nhóm ngành đào tạo theo thông tư 09/2022/TT-BGDĐT
│   │
│   ├── diemchuan_full.csv                          <- Dữ liệu ĐÃ XỬ LÝ GẦN NHƯ HOÀN TẤT (10 cột).
│   ├── diemchuan_full_nhomnganh.csv                <- Dữ liệu 12 cột (Bổ sung Mã nhóm ngành và Nhóm ngành)
│
├── crawler_hocmai(bug).ipynb                       <- Code để crawl dữ liệu, chạy được nhưng không xuất được output như ý.
│
├── preprocessing.ipynb                             <- Preprocessing output tách nhỏ 4 file.
│
├── preprocessing2.ipynb                            <- Preprocessing output 1 file hoàn chỉnh. Chứa tất cả thông tin cần thiết.
│
├── README.md                                       <= File này.

```
