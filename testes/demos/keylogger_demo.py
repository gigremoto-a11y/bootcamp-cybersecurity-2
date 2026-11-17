from pynput import keyboard

def on_press(key):
    try:
        print(f"[AUDITORIA] Tecla pressionada: {key.char}")
    except AttributeError:
        print(f"[AUDITORIA] Tecla especial pressionada: {key}")

def iniciar_monitoramento_local():
    print("--- Demonstração Educacional: Monitoramento Local de Teclado ---")
    print("Pressione algumas teclas (Pressione ESC para encerrar)...")
    
    # Coleta em tempo de execução local (sem salvar em arquivos furtivos, sem envio por rede)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    iniciar_monitoramento_local()
