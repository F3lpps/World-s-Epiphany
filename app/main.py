import os 
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from logica import usar_visao

# Inicializa o console do Rich
console = Console()

jogador = {
    "nome": "Prisioneiro 71",
    "vida": 100,
    "visoes": 3,
    "ruina": 0,
    "inventario": []
}

def exibir_titulo():
    # Tive que limprar o terminal com esta função pois meu windows é muito antigo, e console.clear do rich não funciona nele.
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Criando um texto estilizado com Rich
    titulo = Text("World's Epiphany", style="bold red blink", justify="center")
    subtitulo = Text("\nUm mundo decadente abandonado pelas guerras nucleares.", style="italic dim white", justify="center")
    
    # Combinando os dois no painel
    texto_completo = Text.assemble(titulo, subtitulo)
    
    # Exibe o painel na tela
    console.print(Panel(texto_completo, border_style="bright_black", title="[bold white]RPG V1.0[/bold white]"))
    console.print("\n")

def escolha_nome():
    console.print("[green]Passado anos que ninguém o profere, poderia você lembrar do seu nome?[/green]")

    nome = console.input("\n[bold blue]> [/bold blue]").strip()

    if nome:
        console.print(f"[bold_white]Então seu nome é[bold_white] [green]{nome}[/green]...")
        jogador["nome"] = nome
        inicio_cela()
        return


    else:
        console.print("[red]O silêncio ecoa. Você precisa lembrar de algo...[/red]")
        escolha_nome() # Faz a pergunta de novo caso usuario digite enter sem nada
        return   

def inicio_cela():
    exibir_titulo()
    
    # Texto com cores personalizadas usando tags [cor]
    console.print("[bold white]Você acorda no chão frio de concreto de um putrido calabouço maltratado.[/bold white]")
    console.print("Sua mente queima com os restos de uma [bold purple]visão profética[/bold purple]: um moribundo anjo acorrentado, chorando lágrimas de mercúrio em seu desalento.")
    console.print("Um homem sujo e robusto se aproxima da cela batendo o cassetete nas grades.\n")
    
    console.print("[yellow]O que você deseja fazer?[/yellow]")
    console.print("[green]1.[/green] Ficar em silêncio e observar o guarda.")
    console.print(f"[green]2.[/green] Usar uma visão profética ([cyan]{jogador['visoes']} restantes[/cyan]).")
    
    escolha = console.input("\n[bold blue]> [/bold blue]")
    
    if escolha == "1":
        console.print("\n[green]Você escolheu observar...[/green]")
        
    elif escolha == "2":
        console.print("\n[purple]Você força sua mente para enxergar o amanhã...[/purple]")
        teve_visao = usar_visao(jogador)

        if teve_visao:
            console.print("[bold purple]PREMONIÇÃO:[/bold purple] a interminente névoa nebulosa se dissipa em uma visão, Você vê que em instantes o homem robusto vai se distrair limpando suas botas imundas. As chaves estarão vulneráveis por dez segundos.")
            console.input("\n[dim]Aperte Enter para agir no momento certo...[/dim]")
            momento_fuga(usou_visao=True)
            return

        else: 
            console.print("[white]Você perdeu tempo precioso tentando enxergar o amanhã.[/white]")
            momento_fuga(usou_visao=False) # Vai para a fuga sem a dica
            return
        
    else:
        console.print("\n[red]Opção inválida! O guarda se irrita com seu transe.[/red]")
        console.input("[dim]Aperte Enter para tentar novamente...[/dim]")
        inicio_cela()

def momento_fuga(usou_visao: bool):
    exibir_titulo()

    console.print("[bold white]O guarda para em frente à sua cela. Ele cospe no chão e se curva para limpar a lama de suas botas pesadas...[/bold white]\n")
    
    if usou_visao:
        console.print("[purple]Sabendo exatamente o segundo correto graças à sua visão, você estica o braço silenciosamente.[/purple]")
        console.print("[yellow]O que você faz?[/yellow]")
        console.print("[green]1.[/green] Puxar o molho de chaves silenciosamente.")
        console.print("[green]2.[/green] Tentar nocautear o guarda puxando-o contra as grades.")
    else:
        console.print("[yellow]Ele parece distraído, mas você não sabe por quanto tempo essa chance vai durar.[/yellow]")
        console.print("[yellow]O que você faz?[/yellow]")
        console.print("[green]1.[/green] Arriscar esticar o braço e tentar pegar as chaves às cegas.")
        console.print("[green]2.[/green] Esperar por uma oportunidade melhor (Risco: ele pode ir embora).")


    escolha = console.input("\n[bold blue]> [/bold blue]").strip()
    chance = random.randint(1, 100)

    if escolha == "1":
        # Se usou a visão, a chance de falhar limpando a bota é 0%! Se não usou, tem 10% de chance de dar ruim.
        if not usou_visao and chance <= 10:
            console.print("\n[red]As chaves fazem um som retumbante e o guarda rapidamente utiliza seu taser...[/red]")
        
            console.input("\n[dim]Aperte Enter para continuar...[/dim]")
            return 
        else:
            console.print("\n[green]Suas mãos leves capturam aquela chave podre com facilidade...[/green]")
            
            console.input("\n[dim]Aperte Enter para continuar...[/dim]")
            return
            
    elif escolha == "2":
        console.print("\n[yellow]Você decide agir de outra forma...[/yellow]")
        console.input("\n[dim]Aperte Enter para continuar...[/dim]")
        return


if __name__ == "__main__":
    escolha_nome()