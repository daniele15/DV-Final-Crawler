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
│   ├── preprocessing/                                       <- Data đã crawl về và được cấu trúc lại phù hợp
│   │   ├── diemchuan_collapsed.csv                 <- File trước khi explode `Tổ hợp`.
│   │   ├── diemchuan_collapsed.xlsx                <- giống trên.
│   │
│   ├── university/                                 <- Dữ liệu trường đại học 
│   │   ├── university.csv                          <- Update 05/07: Bổ sung 'Khu vực', 'Tỉnh/ Thành phố', 'Mã trường xét tuyển', 'Mã Trường', 'Tên Trường', 'Loại đơn vị'.
│   │   ├── major_info.csv                          <- Update 05/07: Danh mục nhóm ngành đào tạo theo thông tư 09/2022/TT-BGDĐT, Bổ sung tất cả thông tin cần thiết như Mã nhóm ngành, mã phân ngành,...
│   │
│   ├── diemchuan_full.xlsx                         <- Dữ liệu `ĐÃ XỬ LÝ HOÀN TẤT`.
│
├── crawler_hocmai.ipynb                            <- Code để crawl dữ liệu, chạy được nhưng không xuất được output như ý.
│
├── preprocessing.ipynb                             <- Preprocessing output 1 file hoàn chỉnh. Chứa tất cả thông tin cần thiết. ĐÃ CHUYỂN TẤT CẢ XỬ LÝ THỦ CÔNG SANG CODE.
│
├── README.md                                       <= File này.

```
