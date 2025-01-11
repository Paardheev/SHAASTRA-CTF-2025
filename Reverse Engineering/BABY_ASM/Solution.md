Finding the eax at the end of main.

we run 

gdb ./BABY_ASM

add breakpoint at main  and run

(gdb) break main

(gdb) run

Now disassemble the main function to see return address

(gdb) disassemble main

You see something like this

![image](https://github.com/user-attachments/assets/c43400e8-66a0-49ce-bf81-93869582bd9f)

See the address 0x0000555555555194

(gdb) quit

Again run

gdb ./BABY_ASM

Now add breakpoint with that address and run

(gdb) b *0x0000555555555194

(gdb) run

now see the eax value 

(gdb) info registers eax

It shows 86429

The flag is Shaastra{86429}
