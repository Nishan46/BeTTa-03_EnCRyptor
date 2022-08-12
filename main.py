from time import sleep
from Resc import Core as Core , styles
from Resc.styles import St as styles
from rich import print

import pyperclip

try:

    styles.Consols("\n[STARTING]\n",colours="blue")
    sleep(1)

    styles.Pointpans()
    que = styles.InputWith_Choice("[yellow]Choose your [green]choice",["1","2"],"1")

    if(que == "1"):
        name = str(styles.Input("Enter Text there "))
        EnCriptor = Core.ENCRYPT(name)
        styles.pansInfo("blue bold",EnCriptor)
        styles.pans("purple bold","Key Genarated ! ","green bold",EnCriptor.Encript())
        pyperclip.copy(EnCriptor.Finaly)
        print("[green bold]copied to clipboard")
    else:
        name = str(styles.Input("Enter Key there "))
        Decryptor = Core.DECRYPT(name)
        styles.pansInfo("blue bold",Decryptor)
        styles.pans("purple bold","Key Restored ! ","green bold",Decryptor.Decrypt())

except KeyboardInterrupt:
    print("[red bold][Program] [Exited][/red bold]")
        
except ValueError as e:
    print(f"\n[red bold]Yor Text is Not Supported !!!![/red bold]\n\n")
    styles.pansInfo("yellow bold",f"[ERROR TYPE]\n\n{e}")

except Exception as e:
    print(f"[red bold][UNHANDLED ERROR]\n\nERROR = {e}")





