extract the zip file, it contains a image file.
use sleuthkit tool to analyze the disk.

mmls diskkkk.img

we get DOS Partition Table

we have a single data partition.
let's check the partition with the command.

fls -o 2048 diskkkk.img

it has desktop, pictures, music, documents.

each of them has different files, but in pictures we have flag file.
lets save the file using the command

icat -o 2048 diskkkk.img 21 > flag


check the file's data by file command

file flag

which says heif image, hence change the flag's extension to heic format and open it
the image says _the_fl@g}

this looks like last part of the flag.

lets check other file. 

icat -o 2048 diskkkk.img 20 > window.png

open the window.png it does looks like random picture.

let's look into metadata,

exiftool window.jpg


it has a row named owner name which has value that looks like a base 64 encoding.
convert it into ascii. convert it Shaastra{Th!s_1s

We get the flag Shaastra{Th!s_1s_the_fl@g}

![scansurprise2](https://github.com/user-attachments/assets/4096fd61-5112-455a-b2bd-7636c035ebf4)
![Scansurprise1](https://github.com/user-attachments/assets/5403dd49-ad90-4548-87e3-8616dd15bbb2)
