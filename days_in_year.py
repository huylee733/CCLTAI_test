import sys
from datetime import datetime
import calendar

# Thiết lập encoding UTF-8 cho console Windows nếu cần
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Lấy năm hiện tại từ hệ thống
current_year = datetime.now().year

# Kiểm tra năm nhuận để xác định số ngày (năm nhuận có 366 ngày, năm thường có 365 ngày)
is_leap = calendar.isleap(current_year)
total_days = 366 if is_leap else 365

# In kết quả
leap_str = " (năm nhuận)" if is_leap else ""
print(f"Năm hiện tại ({current_year}) có {total_days} ngày{leap_str}.")
