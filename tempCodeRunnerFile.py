import json, os, shutil, re
import requests, hashlib
file_list = os.listdir('D:\\douyinVideo\\new')
  # Khi tạo biến đếm
count = 1
  # Lặp qua danh sách các file
for file_name in file_list:
    # Tạo tên mới cho file
    new_file_name = str(count) + '.mp4'
    # Thay đổi tên file
    os.rename(os.path.join('D:\\douyinVideo\\new', file_name), os.path.join('D:\\douyinVideo\\new', new_file_name))
    count += 1