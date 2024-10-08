import base64
import os

print("""
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░         ░▒▓█▓▒░    ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       

pywrap can only compile python scripts that use modules that come with python by default
you must be root to use pywrap
""")

if os.path.exists("/usr/bin/i686-w64-mingw32-gcc"):
    print("gcc already installed")
else:
    print("installing gcc... ")
    os.system("apt install gcc-mingw-w64 -y")

if os.path.exists("/usr/bin/wget"):
    print("wget already installed")
else:
    print("installing wget... ")
    os.system("apt install wget -y")

if os.path.exists("./py.h"):
    print("header file already installed")
else:
    print("installing header file...")
    os.system("wget https://fs7.fastupload.io/4ec90b345eaf1ed0/py.h?download_token=29253a7c0fc64a2b565086e233e035b392968e013576921bdfe747b60ad45f34 -O py.h")

print("\nplease enter the filepath of your python script")

inf = input(": ")
    
print("\nplease enter the desired output filename ")
of = input(": ")
print("\nCOMPILING....")
b64str = "IgojaW5jbHVkZSA8c3lzL3R5cGVzLmg+CiNpbmNsdWRlIDxzeXMvc3RhdC5oPgojaW5jbHVkZSA8d2luZG93cy5oPgojaW5jbHVkZSA8ZGlyZW50Lmg+CiNpbmNsdWRlIDxweS5oPgojaW5jbHVkZSA8c3RkaW8uaD4KCnN0YXRpYyBpbnQgcGFyc2VvY3QoY29uc3QgY2hhciAqcCwgc2l6ZV90IG4pCnsKCWludCBpID0gMDsKCXdoaWxlICgoKnAgPCAnMCcgfHwgKnAgPiAnNycpICYmIG4gPiAwKSB7CgkJKytwOwoJCS0tbjsKCX0KCXdoaWxlICgqcCA+PSAnMCcgJiYgKnAgPD0gJzcnICYmIG4gPiAwKSB7CgkJaSAqPSA4OwoJCWkgKz0gKnAgLSAnMCc7CgkJKytwOwoJCS0tbjsKCX0KCXJldHVybiAoaSk7Cn0KCnN0YXRpYyBpbnQgaXNfZW5kX29mX2FyY2hpdmUoY29uc3QgY2hhciAqcCkKewoJaW50IG47Cglmb3IgKG4gPSA1MTE7IG4gPj0gMDsgLS1uKQoJCWlmIChwW25dICE9ICdcMCcpCgkJCXJldHVybiAoMCk7CglyZXR1cm4gKDEpOwp9CgpzdGF0aWMgdm9pZCBjcmVhdGVfZGlyKGNoYXIgKnBhdGhuYW1lLCBpbnQgbW9kZSkKewoJY2hhciAqcDsKCWludCByOwoJaWYgKHBhdGhuYW1lW3N0cmxlbihwYXRobmFtZSkgLSAxXSA9PSAnLycpCgkJcGF0aG5hbWVbc3RybGVuKHBhdGhuYW1lKSAtIDFdID0gJ1wwJzsKCXIgPSBfbWtkaXIocGF0aG5hbWUsIG1vZGUpOwoJaWYgKHIgIT0gMCkgewoJCXAgPSBzdHJyY2hyKHBhdGhuYW1lLCAnLycpOwoJCWlmIChwICE9IE5VTEwpIHsKCQkJKnAgPSAnXDAnOwoJCQljcmVhdGVfZGlyKHBhdGhuYW1lLCAwNzAwKTsKCQkJKnAgPSAnLyc7CgkJCXIgPSBfbWtkaXIocGF0aG5hbWUsIG1vZGUpOwoJCX0KCX0KfQoKc3RhdGljIEZJTEUgKiBjcmVhdGVfZmlsZShjaGFyICpwYXRobmFtZSwgaW50IG1vZGUpCnsKCUZJTEUgKmY7CglmID0gZm9wZW4ocGF0aG5hbWUsICJ3YisiKTsKCWlmIChmID09IE5VTEwpIHsKCQljaGFyICpwID0gc3RycmNocihwYXRobmFtZSwgJy8nKTsKCQlpZiAocCAhPSBOVUxMKSB7CgkJCSpwID0gJ1wwJzsKCQkJY3JlYXRlX2RpcihwYXRobmFtZSwgMDcwMCk7CgkJCSpwID0gJy8nOwoJCQlmID0gZm9wZW4ocGF0aG5hbWUsICJ3YisiKTsKCQl9Cgl9CglyZXR1cm4gKGYpOwp9CgpzdGF0aWMgaW50IHZlcmlmeV9jaGVja3N1bShjb25zdCBjaGFyICpwKQp7CglpbnQgbiwgdSA9IDA7Cglmb3IgKG4gPSAwOyBuIDwgNTEyOyArK24pIHsKCQlpZiAobiA8IDE0OCB8fCBuID4gMTU1KQoJCQl1ICs9ICgodW5zaWduZWQgY2hhciAqKXApW25dOwoJCWVsc2UKCQkJdSArPSAweDIwOwoJfQoJcmV0dXJuICh1ID09IHBhcnNlb2N0KHAgKyAxNDgsIDgpKTsKfQoKc3RhdGljIHZvaWQgdW50YXIoRklMRSAqYSwgY29uc3QgY2hhciAqcGF0aCkKewoJY2hhciBidWZmWzUxMl07CglGSUxFICpmID0gTlVMTDsKCXNpemVfdCBieXRlc19yZWFkOwoJaW50IGZpbGVzaXplOwoJZm9yICg7OykgewoJCWJ5dGVzX3JlYWQgPSBmcmVhZChidWZmLCAxLCA1MTIsIGEpOwoJCWlmIChieXRlc19yZWFkIDwgNTEyKSB7CgkJCWZwcmludGYoc3RkZXJyLAoJCQkgICAgIlNob3J0IHJlYWQgb24gJXM6IGV4cGVjdGVkIDUxMiwgZ290ICVkXG4iLAoJCQkgICAgcGF0aCwgKGludClieXRlc19yZWFkKTsKCQkJcmV0dXJuOwoJCX0KCQlpZiAoaXNfZW5kX29mX2FyY2hpdmUoYnVmZikpIHsKCQkJcmV0dXJuOwoJCX0KCQlpZiAoIXZlcmlmeV9jaGVja3N1bShidWZmKSkgewoJCQlmcHJpbnRmKHN0ZGVyciwgIkNoZWNrc3VtIGZhaWx1cmVcbiIpOwoJCQlyZXR1cm47CgkJfQoJCWZpbGVzaXplID0gcGFyc2VvY3QoYnVmZiArIDEyNCwgMTIpOwoJCXN3aXRjaCAoYnVmZlsxNTZdKSB7CgkJY2FzZSAnNSc6CgkJCWNyZWF0ZV9kaXIoYnVmZiwgcGFyc2VvY3QoYnVmZiArIDEwMCwgOCkpOwoJCQlmaWxlc2l6ZSA9IDA7CgkJCWJyZWFrOwoJCWNhc2UgJzYnOgoJCQlicmVhazsKCQlkZWZhdWx0OgoJCQlmID0gY3JlYXRlX2ZpbGUoYnVmZiwgcGFyc2VvY3QoYnVmZiArIDEwMCwgOCkpOwoJCQlicmVhazsKCQl9CgkJd2hpbGUgKGZpbGVzaXplID4gMCkgewoJCQlieXRlc19yZWFkID0gZnJlYWQoYnVmZiwgMSwgNTEyLCBhKTsKCQkJaWYgKGJ5dGVzX3JlYWQgPCA1MTIpIHsKCQkJCWZwcmludGYoc3RkZXJyLAoJCQkJICAgICJTaG9ydCByZWFkIG9uICVzOiBFeHBlY3RlZCA1MTIsIGdvdCAlZFxuIiwKCQkJCSAgICBwYXRoLCAoaW50KWJ5dGVzX3JlYWQpOwoJCQkJcmV0dXJuOwoJCQl9CgkJCWlmIChmaWxlc2l6ZSA8IDUxMikKCQkJCWJ5dGVzX3JlYWQgPSBmaWxlc2l6ZTsKCQkJaWYgKGYgIT0gTlVMTCkgewoJCQkJaWYgKGZ3cml0ZShidWZmLCAxLCBieXRlc19yZWFkLCBmKQoJCQkJICAgICE9IGJ5dGVzX3JlYWQpCgkJCQl7CgkJCQkJZnByaW50ZihzdGRlcnIsICJGYWlsZWQgd3JpdGVcbiIpOwoJCQkJCWZjbG9zZShmKTsKCQkJCQlmID0gTlVMTDsKCQkJCX0KCQkJfQoJCQlmaWxlc2l6ZSAtPSBieXRlc19yZWFkOwoJCX0KCQlpZiAoZiAhPSBOVUxMKSB7CgkJCWZjbG9zZShmKTsKCQkJZiA9IE5VTEw7CgkJfQoJfQp9CgpjaGFyIGJhc2U0Nl9tYXBbXSA9IHsnQScsICdCJywgJ0MnLCAnRCcsICdFJywgJ0YnLCAnRycsICdIJywgJ0knLCAnSicsICdLJywgJ0wnLCAnTScsICdOJywgJ08nLCAnUCcsCiAgICAgICAgICAgICAgICAgICAgICdRJywgJ1InLCAnUycsICdUJywgJ1UnLCAnVicsICdXJywgJ1gnLCAnWScsICdaJywgJ2EnLCAnYicsICdjJywgJ2QnLCAnZScsICdmJywKICAgICAgICAgICAgICAgICAgICAgJ2cnLCAnaCcsICdpJywgJ2onLCAnaycsICdsJywgJ20nLCAnbicsICdvJywgJ3AnLCAncScsICdyJywgJ3MnLCAndCcsICd1JywgJ3YnLAogICAgICAgICAgICAgICAgICAgICAndycsICd4JywgJ3knLCAneicsICcwJywgJzEnLCAnMicsICczJywgJzQnLCAnNScsICc2JywgJzcnLCAnOCcsICc5JywgJysnLCAnLyd9OwogICAgICAgICAgICAgICAgICAgICAKY2hhciogYmFzZTY0X2RlY29kZShjaGFyKiBjaXBoZXIpIHsKICAgIGNoYXIgY291bnRzID0gMDsKICAgIGNoYXIgYnVmZmVyWzRdOwogICAgY2hhciogcGxhaW4gPSBtYWxsb2Moc3RybGVuKGNpcGhlcikgKiAzIC8gNCk7CiAgICBpbnQgaSA9IDAsIHAgPSAwOwogICAgZm9yKGkgPSAwOyBjaXBoZXJbaV0gIT0gJ1wwJzsgaSsrKSB7CiAgICAgICAgY2hhciBrOwogICAgICAgIGZvcihrID0gMCA7IGsgPCA2NCAmJiBiYXNlNDZfbWFwW2tdICE9IGNpcGhlcltpXTsgaysrKTsKICAgICAgICBidWZmZXJbY291bnRzKytdID0gazsKICAgICAgICBpZihjb3VudHMgPT0gNCkgewogICAgICAgICAgICBwbGFpbltwKytdID0gKGJ1ZmZlclswXSA8PCAyKSArIChidWZmZXJbMV0gPj4gNCk7CiAgICAgICAgICAgIGlmKGJ1ZmZlclsyXSAhPSA2NCkKICAgICAgICAgICAgICAgIHBsYWluW3ArK10gPSAoYnVmZmVyWzFdIDw8IDQpICsgKGJ1ZmZlclsyXSA+PiAyKTsKICAgICAgICAgICAgaWYoYnVmZmVyWzNdICE9IDY0KQogICAgICAgICAgICAgICAgcGxhaW5bcCsrXSA9IChidWZmZXJbMl0gPDwgNikgKyBidWZmZXJbM107CiAgICAgICAgICAgIGNvdW50cyA9IDA7CiAgICAgICAgfQogICAgfQogICAgcGxhaW5bcF0gPSAnXDAnOwogICAgcmV0dXJuIHBsYWluOwp9CgppbnQgcmVtb3ZlX2RpcmVjdG9yeShjb25zdCBjaGFyICpwYXRoKSAKewogICBESVIgKmQgPSBvcGVuZGlyKHBhdGgpOwogICBzaXplX3QgcGF0aF9sZW4gPSBzdHJsZW4ocGF0aCk7CiAgIGludCByID0gLTE7CiAgIGlmIChkKSAKICAgewogICAgICBzdHJ1Y3QgZGlyZW50ICpwOwogICAgICByID0gMDsKICAgICAgd2hpbGUgKCFyICYmIChwPXJlYWRkaXIoZCkpKSAKICAgICAgewogICAgICAgICAgaW50IHIyID0gLTE7CiAgICAgICAgICBjaGFyICpidWY7CiAgICAgICAgICBzaXplX3QgbGVuOwogICAgICAgICAgaWYgKCFzdHJjbXAocC0+ZF9uYW1lLCAiLiIpIHx8ICFzdHJjbXAocC0+ZF9uYW1lLCAiLi4iKSkKICAgICAgICAgICAgIGNvbnRpbnVlOwogICAgICAgICAgbGVuID0gcGF0aF9sZW4gKyBzdHJsZW4ocC0+ZF9uYW1lKSArIDI7IAogICAgICAgICAgYnVmID0gbWFsbG9jKGxlbik7CgogICAgICAgICAgaWYgKGJ1ZikgCiAgICAgICAgICB7CiAgICAgICAgICAgICBzdHJ1Y3Qgc3RhdCBzdGF0YnVmOwoKICAgICAgICAgICAgIHNucHJpbnRmKGJ1ZiwgbGVuLCAiJXMvJXMiLCBwYXRoLCBwLT5kX25hbWUpOwogICAgICAgICAgICAgaWYgKCFzdGF0KGJ1ZiwgJnN0YXRidWYpKSB7CiAgICAgICAgICAgICAgICBpZiAoU19JU0RJUihzdGF0YnVmLnN0X21vZGUpKQogICAgICAgICAgICAgICAgICAgcjIgPSByZW1vdmVfZGlyZWN0b3J5KGJ1Zik7CiAgICAgICAgICAgICAgICBlbHNlCiAgICAgICAgICAgICAgICAgICByMiA9IHVubGluayhidWYpOwogICAgICAgICAgICAgfQogICAgICAgICAgICAgZnJlZShidWYpOwogICAgICAgICAgfQogICAgICAgICAgciA9IHIyOwogICAgICB9CiAgICAgIGNsb3NlZGlyKGQpOwogICB9CiAgIGlmICghcikKICAgICAgciA9IHJtZGlyKHBhdGgpOwogICByZXR1cm4gcjsKfQoKCnZvaWQgd3J0X2RhdGEoY29uc3QgY2hhciAqZmlsZXBhdGgsIGNvbnN0IGNoYXIgKmRhdGEpCnsKICAgIEZJTEUgKmZwID0gZm9wZW4oZmlsZXBhdGgsICJhYiIpOwogICAgaWYgKGZwICE9IE5VTEwpCiAgICB7CiAgICAgICAgZnB1dHMoZGF0YSwgZnApOwogICAgICAgIGZjbG9zZShmcCk7CiAgICB9Cn0KCmludCBleHRyYWN0KCkKewoJRklMRSAqYTsKCWEgPSBmb3BlbigicHkudGFyIiwgInJiIik7Cgl1bnRhcihhLCAicHkiKTsKCWZjbG9zZShhKTsKCXJldHVybiAoMCk7Cn0KCmludCBwcmNzKCkKewogICAgUFJPQ0VTU19JTkZPUk1BVElPTiBQcm9jZXNzSW5mbzsKICAgIFNUQVJUVVBJTkZPIFN0YXJ0dXBJbmZvOwogICAgY2hhciBjbWRBcmdzW10gPSAiIHB5XFxtYWluLnB5IjsKICAgIFplcm9NZW1vcnkoJlN0YXJ0dXBJbmZvLCBzaXplb2YoU3RhcnR1cEluZm8pKTsKICAgIFN0YXJ0dXBJbmZvLmNiID0gc2l6ZW9mIFN0YXJ0dXBJbmZvIDsKCiAgICBpZihDcmVhdGVQcm9jZXNzKCJweVxccHl0aG9uLmV4ZSIsIGNtZEFyZ3MsIAogICAgICAgIE5VTEwsTlVMTCxGQUxTRSwwLE5VTEwsCiAgICAgICAgTlVMTCwmU3RhcnR1cEluZm8sJlByb2Nlc3NJbmZvKSkKICAgIHsgCiAgICAgICAgV2FpdEZvclNpbmdsZU9iamVjdChQcm9jZXNzSW5mby5oUHJvY2VzcyxJTkZJTklURSk7CiAgICAgICAgQ2xvc2VIYW5kbGUoUHJvY2Vzc0luZm8uaFRocmVhZCk7CgkJQ2xvc2VIYW5kbGUoUHJvY2Vzc0luZm8uaFByb2Nlc3MpOwogICAgfSAgCiAgICBlbHNlCiAgICB7CiAgICAgICAgcHJpbnRmKCJUaGUgcHJvY2VzcyBjb3VsZCBub3QgYmUgc3RhcnRlZC4uLiIpOwogICAgfQoKICAgIHJldHVybiAwOwp9CgoKaW50IG1haW4oKQp7CiAgICBGSUxFICpmaWxlID0gZm9wZW4oInB5LnRhciIsICJ3YiIpOwogICAgaWYgKGZpbGUgPT0gTlVMTCkgewogICAgICAgIHBlcnJvcigiRmFpbGVkIHRvIG9wZW4gZmlsZSIpOwogICAgICAgIHJldHVybiAxOwogICAgfQogICAgc2l6ZV90IHdyaXR0ZW4gPSBmd3JpdGUoZW1iZWRkZWRfZGF0YSwgMSwgZW1iZWRkZWRfZGF0YV9zaXplLCBmaWxlKTsKICAgIGlmICh3cml0dGVuICE9IGVtYmVkZGVkX2RhdGFfc2l6ZSkgewogICAgICAgIHBlcnJvcigiRmFpbGVkIHRvIHdyaXRlIGNvbXBsZXRlIGRhdGEiKTsKICAgICAgICBmY2xvc2UoZmlsZSk7CiAgICAgICAgcmV0dXJuIDE7CiAgICB9CiAgICBmY2xvc2UoZmlsZSk7CglleHRyYWN0KCk7Cgl3cnRfZGF0YSgicHlcXG1haW4ucHkiLGJhc2U2NF9kZWNvZGUoSU4pKTsKCWludCBydW4gPSBwcmNzKCk7CglyZW1vdmVfZGlyZWN0b3J5KCJweSIpOwoJcmVtb3ZlKCJweS50YXIiKTsKfQo="
sect1 = "#define IN \""
sect2 = base64.b64encode(open(inf,"rb").read()).decode()
sect3 = base64.b64decode(b64str.encode()).decode()
open("out.c","w").write(f"{sect1}{sect2}{sect3}")
os.system(f"i686-w64-mingw32-gcc -I./ -o {of} out.c")
os.remove("out.c")
print(f"{of} finished compiling... exiting pywrap...")
