import random
from rich.console import Console

console = Console()

def usar_visao(jogador):

    if jogador["visoes"] <=0:
        console.print("\n[red]Você força suas têmporas, mas sua mente está exausta. Nenhuma visão se manifesta...[/red]")
        return False
    
    jogador["visoes"] -=1

# essa linha é para adicionar um elemento de sorte: 10% de chance de a visão ser confusa/falhar devido ao ambiente instável
    chance = random.randint(1, 100)

    if chance <=10:
        console.print("\n[yellow]Sua visão se distorce em um mar nebuloso e incomprensível. Você não consegue decifrar o futuro desta vez![/yellow]")
        console.print(f"[dim](Visões restantes: {jogador['visoes']})[/dim]\n")
        return False
    
    console.print(f"\n[purple]👁️ Sua cabeça lateja, dor, dor! seus olhos reviram-se para trás. O véu do tempo se rasga por um breve segundo... ({jogador['visoes']} restantes)[/purple]\n")
    return True
    




