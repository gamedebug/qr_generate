#!/anaconda2/bin/python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyQR import myqr

words = raw_input("请输入二维码内容: ");

myqr.run(
    words,
    save_name = "my_qr.png"
)

