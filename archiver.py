import os
import re
import patoolib

files_in_dirrectory = os.listdir()
files_for_acrchive  = []
archives            = []

# Получение файлов для нового архива
for i in files_in_dirrectory:
	extention = os.path.splitext(i)[1]
	if extention != ".rar" and extention != ".py" and extention != ".exe" and extention != ".bat":
		files_for_acrchive.append(i)
	if extention == ".rar":
		archives.append(i)

# for i in files_for_acrchive:
# 	print(i)

# Новый номер для архива
nums = []
for i in archives:
	num = re.search(r"(\d+)", i) # Поиск цифры в названии архива
	if num:
		nums.append(int(num.group(1)))
max_num = max(nums)

# Создание архива
patoolib.create_archive(f"./REPOsaves{int(max_num)+1}.rar", files_for_acrchive)