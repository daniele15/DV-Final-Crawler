import gzip, csv
import os
import json
import pathlib
import subprocess
from glob import glob

# Hàm đọc nội dung từ file gzip và trả về dưới dạng chuỗi
def get_content_by_gz(file_path):
    with gzip.open(file_path, 'rt') as f:
        file_content = f.read()
    return file_content

# Hàm đọc nội dung từ file và trả về dưới dạng chuỗi
def get_content(file_path):
    with open(file_path) as f:
        s = f.read()
    return s

# Hàm lấy danh sách các tệp tin trong thư mục cùng với đường dẫn tuyệt đối của chúng
def get_files_in_folder(folder_path):
    files_absolute_path = []
    files_name = None
    for root, dirs, files in os.walk(os.path.abspath(folder_path)):
        files_name = files
        for file in files:
            if '.DS_Store' not in file:  # Loại bỏ tệp .DS_Store nếu có
                files_absolute_path.append(os.path.join(root, file))
    return files_absolute_path, files_name

# Hàm lấy danh sách các tệp tin trong thư mục chỉ với đường dẫn tuyệt đối
def get_files_absolute_in_folder(folder_path):
    """
    Trả về danh sách các đường dẫn tuyệt đối của các tệp tin trong thư mục.

    :param folder_path: Đường dẫn đến thư mục
    :return: Danh sách các đường dẫn tuyệt đối của các tệp tin
    """
    files_absolute_path, files_name = get_files_in_folder(folder_path)
    return files_absolute_path

# Hàm load các đối tượng JSON từ file gzip với mỗi đối tượng trên một dòng
def load_jsonl_from_gz(file_gz_path, min_length_per_line=5):
    """
    Load các đối tượng JSON từ file gzip, mỗi đối tượng trên một dòng.

    :param file_gz_path: Đường dẫn đến file gzip
    :param min_length_per_line: Độ dài tối thiểu của mỗi dòng để xem là một đối tượng hợp lệ
    :return: Danh sách các đối tượng JSON được load từ file
    """
    output_objs = []
    for text in get_content_by_gz(file_gz_path).split('\n'):
        try:
            if len(text) >= min_length_per_line:
                obj = json.loads(text)
                output_objs.append(obj)
        except Exception as e:
            print(e)
    return output_objs

# Hàm load các đối tượng JSON từ file gzip có định dạng timestamp, mỗi đối tượng trên một dòng
def load_timestamp_format_jsonl_from_gz(file_gz_path, data_space_no=1, min_length_per_line=5):
    """
    Load các đối tượng JSON từ file gzip có định dạng timestamp, mỗi đối tượng trên một dòng.

    :param file_gz_path: Đường dẫn đến file gzip
    :param data_space_no: Vị trí dấu cách đánh dấu giữa timestamp và dữ liệu JSON
    :param min_length_per_line: Độ dài tối thiểu của mỗi dòng để xem là một đối tượng hợp lệ
    :return: Danh sách các đối tượng JSON được load từ file
    """
    output_objs = []
    for text in get_content_by_gz(file_gz_path).split('\n'):
        try:
            if text is None or text == '':
                return []
            text_data = ' '.join(text.split(' ')[data_space_no:])
            if len(text_data) >= min_length_per_line:
                obj = json.loads(text_data)
                output_objs.append(obj)
        except Exception as e:
            print(e)
    return output_objs

# Hàm lấy danh sách các thư mục con trong một thư mục
def get_sub_folders_in_folder(folder_path):
    """
    Lấy danh sách các thư mục con trong một thư mục.

    :param folder_path: Đường dẫn đến thư mục
    :return: Danh sách các đường dẫn tuyệt đối của các thư mục con
    """
    sub_folders = glob(folder_path + "/*/")
    return sub_folders

# Hàm tạo thư mục nếu chưa tồn tại
def create_folder_if_not_exist(folder_path):
    """
    Tạo thư mục nếu thư mục chưa tồn tại.

    :param folder_path: Đường dẫn đến thư mục
    """
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

# Hàm lấy danh sách các thư mục con và tên tệp tin trong một thư mục
def get_sub_folders_and_file_name_in_folder(folder_path):
    """
    Lấy danh sách các thư mục con và tên tệp tin trong một thư mục.

    :param folder_path: Đường dẫn đến thư mục
    :return: Danh sách các đường dẫn tuyệt đối của các thư mục con và danh sách tên tệp tin
    """
    sub_folders = glob(folder_path + "/*/")
    files_name = [file_path.split('/')[-2] for file_path in sub_folders]
    return sub_folders, files_name

# Hàm load đối tượng JSON từ file
def load_json(file_path):
    """
    Load đối tượng JSON từ file.

    :param file_path: Đường dẫn đến file
    :return: Đối tượng JSON
    """
    with open(file_path) as f:
        data = json.load(f)
    return data

# Hàm lưu đối tượng JSON vào file
def store_json(object, file_output_path):
    """
    Lưu đối tượng JSON vào file.

    :param object: Đối tượng JSON
    :param file_output_path: Đường dẫn đến file đầu ra
    """
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    with open(file_output_path, 'w') as fp:
        json.dump(object, fp, ensure_ascii=False, sort_keys=True, indent=1)

# Hàm lưu nội dung vào file
def store_file(content, file_output_path):
    """
    Lưu nội dung vào file.

    :param content: Nội dung cần lưu
    :param file_output_path: Đường dẫn đến file đầu ra
    """
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    with open(file_output_path, 'w+') as fh:
        fh.write(str(content))

# Hàm lưu nội dung vào file gzip
def store_gz(content, file_output_path, is_append=False):
    """
    Lưu nội dung vào file gzip.

    :param content: Nội dung cần lưu
    :param file_output_path: Đường dẫn đến file gzip đầu ra
    :param is_append: True nếu muốn thêm vào cuối file, False nếu ghi đè
    """
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    if is_append:
        with gzip.open(file_output_path, 'ab') as f:
            f.write(content.encode('utf-8'))
    else:
        with gzip.open(file_output_path, 'wb') as f:
            f.write(content.encode('utf-8'))

# Hàm lưu đối tượng JSON thành các dòng riêng biệt trong file gzip
def store_jsons_perline_in_file(jsons_obj, file_output_path, is_append=False):
    """
    Lưu các đối tượng JSON thành các dòng riêng biệt trong file gzip.

    :param jsons_obj: Danh sách các đối tượng JSON cần lưu
    :param file_output_path: Đường dẫn đến file gzip đầu ra
    :param is_append: True nếu muốn thêm vào cuối file, False nếu ghi đè
    """
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    if is_append:
        with gzip.open(file_output_path, 'ab') as f:
            for idx, json_obj in enumerate(jsons_obj):
                if idx == 0:
                    f.write((json.dumps(json_obj, ensure_ascii=False)).encode('utf-8'))
                else:
                    f.write(('\n' + json.dumps(json_obj, ensure_ascii=False)).encode('utf-8'))
    else:
        with gzip.open(file_output_path, 'wb') as f:
            for idx, json_obj in enumerate(jsons_obj):
                if idx == 0:
                    f.write((json.dumps(json_obj, ensure_ascii=False)).encode('utf-8'))
                else:
                    f.write(('\n' + json.dumps(json_obj, ensure_ascii=False)).encode('utf-8'))

# Hàm lưu đối tượng JSON thành các dòng riêng biệt trong file không nén
def store_jsons_perline_in_file_non_compress(jsons_obj, file_output_path, is_append=False):
    """
    Lưu các đối tượng JSON thành các dòng riêng biệt trong file không nén.

    :param jsons_obj: Danh sách các đối tượng JSON cần lưu
    :param file_output_path: Đường dẫn đến file đầu ra
    :param is_append: True nếu muốn thêm vào cuối file, False nếu ghi đè
    """
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    if (is_append):
        with open(file_output_path, 'ab') as f:
            for json_obj in jsons_obj:
                f.write((json.dumps(json_obj, ensure_ascii=False) + '\n').encode('utf-8'))
    else:
        with open(file_output_path, 'wb') as f:
            for json_obj in jsons_obj:
                f.write((json.dumps(json_obj, ensure_ascii=False) + '\n').encode('utf-8'))

# Hàm callback để xử lý từng dòng trong file CSV
def get_content_from_csv_callback(file_input_path, process_callback):
    """
    Đọc nội dung từ file CSV và áp dụng hàm callback cho từng dòng.

    :param file_input_path: Đường dẫn đến file CSV
    :param process_callback: Hàm callback được áp dụng cho mỗi dòng của file CSV
    """
    with open(file_input_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            process_callback(row)

# Hàm đọc nội dung từ file CSV và trả về danh sách các dòng
def get_content_from_csv(file_input_path):
    """
    Đọc nội dung từ file CSV và trả về danh sách các dòng.

    :param file_input_path: Đường dẫn đến file CSV
    :return: Danh sách các dòng trong file CSV
    """
    output = []
    with open(file_input_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            output.append(row)
    return output

# Hàm ghi danh sách UID vào file CSV
def list_uid_to_csv(list_uid, file_path):
    """
    Ghi danh sách UID vào file CSV.

    :param list_uid: Danh sách các UID cần ghi vào file
    :param file_path: Đường dẫn đến file CSV đầu ra
    """
    with open(file_path, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for data in list_uid:
            wr.writerow([int(data)])

# Hàm đếm số dòng trong file
def wccount(file_path):
    """
    Đếm số dòng trong file.

    :param file_path: Đường dẫn đến file cần đếm
    :return: Số dòng trong file
    """
    out = subprocess.Popen(['wc', '-l', file_path],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT
                           ).communicate()[0]
    return int(out.partition(b' ')[0])

# Hàm đếm số dòng trong file gzip
def wcgzcount(file_path):
    """
    Đếm số dòng trong file gzip.

    :param file_path: Đường dẫn đến file gzip cần đếm
    :return: Số dòng trong file gzip
    """
    count = 0
    try:
        bashCommand = "zcat " + file_path + " | wc -l"
        out = os.popen(bashCommand)
        data = out.read()
        count = int(data.split('\n')[0])
        out.close()
    except Exception as e:
        print(e)
    return count

# Hàm đếm tổng số dòng của tất cả file gzip trong một thư mục
def count_line_all_gz(folder_path):
    """
    Đếm tổng số dòng của tất cả file gzip trong một thư mục.

    :param folder_path: Đường dẫn đến thư mục chứa các file gzip
    :return: Tổng số dòng của tất cả file gzip trong thư mục
    """
    count = 0
    bashCommand = "zcat " + folder_path + "/*.gz | wc -l"
    try:
        out = os.popen(bashCommand)
        data = out.read()
        count = int(data.split('\n')[0])
        out.close()
    except Exception as e:
        print(e)
    return count

##### MODIFIED 18/06/2024

# Hàm chuyển đổi các đối tượng JSON thành file CSV
def convert_json_to_csv(json_objects, csv_file_path):
    """
    Chuyển đổi các đối tượng JSON thành file CSV.

    :param json_objects: Danh sách các đối tượng JSON cần chuyển đổi
    :param csv_file_path: Đường dẫn đến file CSV đầu ra
    """
    if not json_objects:
        print("No JSON objects to write.")
        return
    
    # Lấy header từ đối tượng JSON đầu tiên
    header = list(json_objects[0].keys())

    try:
        with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for json_obj in json_objects:
                writer.writerow(json_obj)
        print(f"CSV file successfully created at {csv_file_path}")
    except Exception as e:
        print(f"Error writing CSV to {csv_file_path}: {e}")
