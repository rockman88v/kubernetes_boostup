# Sử dụng hình ảnh Python chính thức
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tệp yêu cầu vào container
COPY requirements.txt requirements.txt

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào container
COPY random-app.py random-app.py

# Mở cổng ứng dụng
EXPOSE 8080

# Chạy ứng dụng
CMD ["python", "random-app.py"]