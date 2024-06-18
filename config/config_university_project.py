class ConfigUniversityProject:

    def __init__(self, *args, **kwargs):
        # Đường dẫn đến thư mục cơ sở dữ liệu. Nếu không có trong kwargs, mặc định là '/Users/tuantmtb/Documents/wp/beecost/data/university/2023'
        self.folder_data_base = kwargs.get('folder_data_base',
                                           'C:/Users/letra/Workspace/DV/Crawler-THPTQG')
                                           

    @property
    def folder_output_path(self):
        # Đường dẫn đến thư mục đầu ra của trình thu thập dữ liệu
        return self.folder_data_base + '/crawler/common'

    @property
    def file_university_path(self):
        # Đường dẫn đến tệp tin nén chứa dữ liệu các trường đại học
        return self.folder_output_path + '/university.gz'

    @property
    def file_university_diemchuan_path(self):
        # Đường dẫn đến tệp tin nén chứa dữ liệu điểm chuẩn của các trường đại học
        return self.folder_output_path + '/university_diemchuan.gz'

    def file_diemthi_2020_path(self, provide_id, part):
        # Đường dẫn đến tệp tin nén chứa dữ liệu điểm thi năm 2020, theo mã cung cấp và phần
        return f'{self.folder_output_path}/diemthi_2020/provide_{provide_id}_{part}.gz'

    def file_diemthi_2021_path(self, provide_id, part=None):
        # Đường dẫn đến tệp tin nén chứa dữ liệu điểm thi năm 2021, theo mã cung cấp và phần (nếu có)
        if part is None:
            return f'{self.folder_output_path}/diemthi_2021/provide_{provide_id}.gz'
        return f'{self.folder_output_path}/diemthi_2021/provide_{provide_id}_{part}.gz'

    def file_diemthi_path(self, provide_id, part=None):
        # Đường dẫn đến tệp tin nén chứa dữ liệu điểm thi, theo mã cung cấp và phần (nếu có)
        if part is None:
            return f'{self.folder_output_path}/provide_{provide_id}.gz'
        return f'{self.folder_output_path}/provide_{provide_id}_{part}.gz'

    @property
    def file_major_path(self):
        # Đường dẫn đến tệp tin nén chứa dữ liệu các ngành học
        return self.folder_output_path + '/major.gz'
