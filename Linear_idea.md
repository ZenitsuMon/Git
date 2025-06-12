**Tạo data set**

 >     -> Phải có một danh sách những dữ liệu, và DV,IV phải là những dữ liệu theo cặp 

**Tìm fit line**
	
 >      -> Phải có một công thức (cơ bản nhất là y =ax+b,với y và x lần lượt là DV,IV, a là số đứng trước x, b là hằng số), thay những giá trị của DV,IV vào (K thay hết, chừa 1 số để test)

**Bắt đầu tìm fit line từ đâu**
	
>     -> Nếu như đây là một bài toán vẽ đường, thì sẽ cố vẽ đường ban đầu sao cho nó đi qua nhiều điểm nhất có thể, cũng như trên máy tính thì chọn công thức thỏa mãn nhiều dữ liệu nhất có thể
>      	
>      *Làm sao để biết công thức nào thỏa mãn nhiều dữ liệu nhất?*
>	      
>     -> Mình đang sử dụng công thức y=ax+b, em sẽ chọn 2 dữ liệu để thay vào công thức (chọn ngẫu nhiên, nhưng phải dùng hết tất cả dữ liệu), giải hệ phương trình 2 ẩn, tìm ra a,b.

**Tìm đường fit line**
	
>     Lặp lại việc này sẽ giúp mình có rất nhiều công thức y=ax+b, lúc này ta sẽ chọn dữ liệu IV để thay vào các công thức, tìm ra những dữ liệu DV fit, so sánh với lại dữ liệu DV observed, tìm ra công thức có nhiều DV fit gần bằng với DV observed nhất, sau đó điều chỉnh lại công thức
>  	
>     *Điều chỉnh lại công thức kiểu gì?*
>	
>     -> Phải điều chỉnh lại a,b
>	
>     *Điều chỉnh lại a,b kiểu gì?*
>	
>     -> .....

**Sau khi điều chỉnh lại a, b thì có nghĩa đã tìm ra được đường fit line**
	
>      *Đo khoảng cách từ đường đến điểm dữ liệu thì sẽ dùng Sum of Squares:*
>	
>      -> Công thức: [x(i)-x(mean)]^2 +....
>	
*Khi mà tìm ra được fit line, dùng công thức gì để tính độ chính xác của nó?:*
	
>      -> [SS(mean) - SS(fit)]/SS(mean)

**Tiếp theo sẽ đến giai đoạn test**
	
 >      *Dùng dữ liệu còn lại để test, nếu test xong, làm sao để tăng độ chính xác của nó?:*
> 
>	
 >      -> Tự tạo ra những dữ liệu mới lạ, công thức chưa gặp được, lặp lại qui trình test r sửa
	
 *Tự tạo ra những dữ liệu mới bằng cách gì?, tại sao phải tạo ra những dữ liệu mới?:*
	
 >      ->Tạo ra những dữ liệu mới bằng cách random (tạo ngẫu nhiên), phải tạo ra những dữ liệu mới vì những dữ lệu đó sẽ là những dữ liệu mới, lạ công thức chưa từng gặp nên sẽ có thể kiểm tra độ chính xác của công thức khi đối mặt với những dữ liệu lạ, và có thể dựa vào những dữ liệu mới lạ đó để train lại công thức => tăng độ chính xác


### Cụ thể vô code:

**Chọn dataset là weight và height, tại sao?**

        -> Vì 2 dữ liệu này có mối quan hệ với nhau, mối quan hệ của chúng dễ thấy nhất là height cao thì weight cũng cao, nhưng mà đây là những dữ liệu ngẫu nhiên, kh tỉ lệ thuận hay nghịch theo một hằng số k nào cả

**Tại sao lại chia dataset làm 1/3,2/3?**

        -> Vì cần dùng 2/3 dataset để train, liên tục thay vào công thức tìm ra một công thức đủ chính xác để test

**Tại sao cần phải dùng 2/3 để train:**

        -> Vì em nghĩ 2/3 là con số phù hợp ngta đã kết luận ra từ nhiều lần thử, nếu là 1/2 thì quá ít, còn nếu > 2/3 thì mình đang dùng quá nhiều dữ liệu để train, lúc đó test sẽ kh đủ nhiều để kiểm tra độ chính xác của công thức
