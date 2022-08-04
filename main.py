from time import sleep
from Resc import Core as Core , styles
from Resc.styles import St as styles
from rich import print

# try:
    
# except:
#     if KeyboardInterrupt:
#         print("[red bold][Program] [Exited] !!!![/red bold]")


styles.Consols("\n[STARTING]\n",colours="blue")
sleep(1)

styles.Pointpans()
que = styles.InputWith_Choice("[yellow]Choose your [green]choice",["1","2"],"1")

if(que == "1"):
    name = str(styles.Input("Enter Text there "))
    EnCriptor = Core.ENCRYPT(name)
    styles.pans("purple bold","Key Genarated ! ","green bold",EnCriptor.Encript())
    styles.pansInfo("blue bold",EnCriptor)
else:
    name = str(styles.Input("Enter Key there "))
    styles.pans("green",f"Here we are ...[/green]\n [red]---- Key ----\n{name}[/red]\n [yellow]--- Clear Text ---[/yellow]","green",Core.Decrypt(name))



