#!/anaconda2/bin/python
#!/usr/bin/python

from MyQR import myqr

words = raw_input("Enter your text: ");

myqr.run(
    words,
    save_name = "my_qr.png"
)

