As the question says sum of a hidden password and the value the main returns and 1 is the password for zip file.

first we check 

strings x86assembly

we get

![image](https://github.com/user-attachments/assets/9f6cc5ca-cdec-4805-9463-76a585c4d5d0)

so the hidden password is 13114119239.

And in ghidra analysing the binary file and decompiling it gives you the c code.

![image](https://github.com/user-attachments/assets/fe98627b-b80b-46af-8cad-2d5e281a95de)


int main(void)

{
  int iVar1;
  
  int local_10;
  
  int local_c;
  
  local_c = 0;
  
  iVar1 = sqt(0x311f5);
  
  for (local_10 = 1; local_10 <= iVar1; local_10 = local_10 + 1)
  {
    if (0x311f5 % local_10 == 0)
    {
      if (local_10 * local_10 == 0x311f5)
      {
        local_c = local_c + local_10;
      }
      else 
      {
        local_c = local_c + local_10 + 0x311f5 / local_10;
      }
    }
  }
  
  return local_c;
}

If the image isn't clear, above is the decomiled code.

Here you can see that it is the sum of factors of the number 0x311f5 which is 201205

Which indeed is 241452.

so the password to open the zip is (241452+13114119239+1)=13114360692

Here is the flag Shaastra{gn!7een!gnE_e$7e^e7}.
