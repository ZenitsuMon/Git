# **Linear Regression**:

**Mục đích**: Tìm ra một công thức có độ chính xác cao để có thể dự đoán được y khi có x

**Công thức đơn giản**: f(x) = y = ax+b có thể mở rộng lên nhiều ẩn hơn, cơ bản là 2 ẩn y: dependent variable, cũng có nhiều tên khác như output variables

**x**: independent variable cũng có nhiều tên khác như input variables

**b**: constant, số tự do, kh gắn với 1 ẩn nào hết

**a**: parameters, ẩn

**Công thức tổng quát**: dependent = constant + parameter*independent + ...

Để tìm ra đường phù hợp thì phải tính tổng bình phương của khoảng cách từ điểm data chính xác đến điểm data dự đoán gọi là SS(fit) (Khoảng cách từ điểm data chính xác đến điểm data dự đoán gọi là residual)

Và cuối cùng đường thẳng phù hơp nhất là đường thẳng có SUM(residual) nhỏ nhất

**Slope**: Độ dốc của đường thẳng dựa vào a (hệ số trước x)

**R^2**: Tính độ chính xác của công thức

Đưa các điểm data về trùng với trục Oy, tính trung bình của các data point, em nghĩ công thức sẽ là: (x1+x2+...xn)/n, sẽ ra được giá trị trung bình

Tiếp theo tính tổng bình phương khoảng cách từ điểm data đến giá trị trung bình, gọi là SS(mean)

**R^2 = (SS(mean) - SS(fit))/(SS(mean)) với 0 <= R^2 <= 1**

Lúc trước em có tìm hiểu sơ qua về linear progression trong ML thì phải, thì mình sẽ có 1 dataset, mình sẽ chia data ra làm 2 phần: train(2/3dataset) và test(1/3dataset)

Mình sẽ dùng train để tìm ra công thức phù hợp rồi dùng test để test độ chính xác

